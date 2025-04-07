# Jeu de Données pour la Détection de Fraude  

## 🔒 Description du Jeu de Données  
Le jeu de données sur la détection des fraudes financières contient des informations relatives aux transactions financières et aux schémas frauduleux. Il est conçu pour entraîner et évaluer des modèles de machine learning dédiés à la détection de fraude.  

## 📁 Structure du Jeu de Données  
Le jeu de données est organisé dans le dossier **`data`** et comprend plusieurs sous-dossiers contenant des fichiers CSV spécifiques aux transactions financières, aux profils clients, aux schémas frauduleux, aux montants des transactions et aux informations sur les commerçants.  

### 📂 `data`  
#### 📂 Données des Transactions  
- **`transaction_records.csv`** : Contient les enregistrements de transactions avec des détails tels que l’ID de la transaction, la date, le montant et l’ID du client.  
- **`transaction_metadata.csv`** : Contient des métadonnées supplémentaires pour chaque transaction.  

#### 📂 Profils Clients  
- **`customer_data.csv`** : Comprend les profils des clients avec des informations telles que le nom, l’âge, l’adresse et les coordonnées.  
- **`account_activity.csv`** : Fournit des détails sur l’activité des comptes clients, y compris le solde, l’historique des transactions et le statut du compte.  

#### 📂 Schémas Frauduleux  
- **`fraud_indicators.csv`** : Contient des indicateurs de fraude et des activités suspectes.  
- **`suspicious_activity.csv`** : Fournit des détails spécifiques sur les transactions signalées comme suspectes.  

#### 📂 Montants des Transactions  
- **`amount_data.csv`** : Contient les montants des transactions pour chaque opération.  
- **`anomaly_scores.csv`** : Fournit des scores d’anomalie pour les montants des transactions, indiquant un risque potentiel de fraude.  

#### 📂 Informations sur les Commerçants  
- **`merchant_data.csv`** : Contient des informations sur les commerçants impliqués dans les transactions.  
- **`transaction_category_labels.csv`** : Fournit des catégories pour différents types de transactions.  

### 📂 `src`  
- **`data.py`** : Fichier Python contenant le code permettant de générer le jeu de données à partir de données réelles. 