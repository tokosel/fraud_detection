from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

# Charger le modèle
model_path = "fraud_detection.pkl"
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    print(f"Erreur: Le fichier modèle '{model_path}' n'a pas été trouvé!")

# Définir les colonnes d'entrée requises par le modèle
columns = ['Category', 'TransactionAmount', 'AnomalyScore', 'Amount', 
           'AccountBalance', 'SuspiciousFlag', 'Hour', 'gap']

@app.route('/')
def index():
    """Afficher la page d'accueil"""
    # Passer result=None pour que le template puisse gérer le cas où result n'existe pas
    return render_template('index.html', result=None)

@app.route('/predict', methods=['POST'])
def predict():
    """Point de terminaison API pour faire des prédictions"""
    try:
        # Récupérer les données JSON de la requête
        data = request.json
        
        # Créer un DataFrame avec les données d'entrée
        input_data = pd.DataFrame([
            [
                int(data.get('Category', 0)),
                float(data.get('TransactionAmount', 0)),
                int(data.get('AnomalyScore', 0)),
                float(data.get('Amount', 0)),
                float(data.get('AccountBalance', 0)),
                int(data.get('SuspiciousFlag', 0)),
                int(data.get('Hour', 0)),
                int(data.get('gap', 0))
            ]
        ], columns=columns)
        
        # Faire une prédiction
        prediction = model.predict(input_data)        
        # Préparer la réponse
        result = {
            'prediction': int(prediction[0]),
            'label': "Fraude" if prediction[0] == 1 else "Transaction normale"
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)