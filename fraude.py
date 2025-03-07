import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import warnings as wr
wr.filterwarnings(action="ignore")
import seaborn as sns

# Chargement des différentes bases de données
account = pd.read_csv("/Data/Customer Profiles/account_activity.csv")
customer = pd.read_csv("/Data/Customer Profiles/customer_data.csv")
fraud = pd.read_csv("/Data/Fraudulent Patterns/fraud_indicators.csv")
suspision = pd.read_csv("/Data/Fraudulent Patterns/suspicious_activity.csv")
merchant = pd.read_csv("/Data/Merchant Information/merchant_data.csv")
tran_cat = pd.read_csv("/Data/Merchant Information/transaction_category_labels.csv")
amount = pd.read_csv("/Data/Transaction Amounts/amount_data.csv")
anamoly = pd.read_csv("/Data/Transaction Amounts/anomaly_scores.csv")
tran_data = pd.read_csv("/Data/Transaction Data/transaction_metadata.csv")
tran_rec = pd.read_csv("/Data/Transaction Data/transaction_records.csv")

# Affichage des premières lignes de chaque dataset
for df in [account, customer, fraud, suspision, merchant, tran_cat, amount, anamoly, tran_data, tran_rec]:
    print(df.head())

# Fusion des bases de données pour constituer un dataset client
customer_data = pd.merge(customer, account, on='CustomerID')
customer_data = pd.merge(customer_data, suspision, on='CustomerID')

# Fusion des bases de données pour constituer un dataset transactionnel
transaction_data1 = pd.merge(fraud, tran_cat, on="TransactionID")
transaction_data2 = pd.merge(amount, anamoly, on="TransactionID")
transaction_data3 = pd.merge(tran_data, tran_rec, on="TransactionID")
transaction_data = pd.merge(transaction_data1, transaction_data2, on="TransactionID")
transaction_data = pd.merge(transaction_data, transaction_data3, on="TransactionID")

# Fusion des données clients et transactionnelles
final_data = pd.merge(transaction_data, customer_data, on="CustomerID")

# Exploration des données
print(final_data.info())  # Information générale sur les colonnes et types de données
print(final_data.shape)  # Dimensions du dataset
print(final_data.describe())  # Statistiques descriptives
print(final_data.columns)  # Liste des colonnes

# Séparation des variables numériques et catégoriques
numerical_features = final_data.select_dtypes(include=['number']).columns.tolist()
categorical_features = final_data.select_dtypes(include=['object']).columns.tolist()
print(numerical_features)
print(categorical_features)

# Visualisation des variables catégoriques
for column in categorical_features:
    top_10_values = final_data[column].value_counts().head(10)
    plt.figure(figsize=(10, 5))
    sns.countplot(x=column, data=final_data, order=top_10_values.index)
    plt.title(f'Distribution de {column}')
    plt.xticks(rotation=90)
    plt.show()

# Visualisation des variables numériques via des boxplots
num_cols = len(numerical_features)
num_rows = (num_cols // 2) + (num_cols % 2)
fig, axes = plt.subplots(num_rows, 2, figsize=(12, 6*num_rows))
fig.suptitle("Boxplots des variables numériques")

for i, column in enumerate(numerical_features):
    row = i // 2
    col = i % 2
    sns.boxplot(x=final_data[column], ax=axes[row, col])
    axes[row, col].set_title(column)

if num_cols % 2 != 0:
    fig.delaxes(axes[num_rows-1, 1])

plt.tight_layout()
plt.subplots_adjust(top=0.95)
plt.show()

# Analyse de la variable cible (FraudIndicator)
sns.countplot(x='FraudIndicator', data=final_data, palette='Set2')
plt.title('Répartition des fraudes')
plt.show()

# Matrice de corrélation
plt.figure(figsize=(12, 8))
sns.heatmap(final_data[numerical_features].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matrice de corrélation des variables numériques')
plt.show()

# Suppression des colonnes non pertinentes
columns_to_drop = ['TransactionID', 'MerchantID', 'CustomerID', 'Name', 'Age', 'Address']
data_cleaned = final_data.drop(columns=columns_to_drop)

# Feature engineering : création de nouvelles variables
data_cleaned['Timestamp'] = pd.to_datetime(data_cleaned['Timestamp'])
data_cleaned['Hour'] = data_cleaned['Timestamp'].dt.hour
data_cleaned['LastLogin'] = pd.to_datetime(data_cleaned['LastLogin'])
data_cleaned['GapDays'] = (data_cleaned['Timestamp'] - data_cleaned['LastLogin']).dt.days.abs()

# Préparation des données pour le modèle
X = data_cleaned.drop(['FraudIndicator', 'Timestamp', 'LastLogin'], axis=1)
Y = data_cleaned['FraudIndicator']

# Encodage des variables catégoriques
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
X['Category'] = label_encoder.fit_transform(X['Category'])

# Division des données en ensemble d'entraînement et de test
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Entraînement d'un modèle de classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
model = DecisionTreeClassifier()
model.fit(X_train, Y_train)
y_pred = model.predict(X_test)

# Évaluation du modèle
print("Accuracy:", accuracy_score(Y_test, y_pred))
print("Precision:", precision_score(Y_test, y_pred))
print("Recall:", recall_score(Y_test, y_pred))
print("F1 Score:", f1_score(Y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(Y_test, y_pred))
