# Projet de Détection de Fraude

Ce projet implémente un système de détection de fraude basé sur des techniques de machine learning.

## Structure du Projet

```
ML/
├── Data/                      # Dossier contenant les jeux de données
├── env/                       # Environnement virtuel Python
├── templates/                 # Templates pour l'interface web
│   └── index.html             # Page principale de l'interface
├── .gitignore                 # Configuration des fichiers à ignorer par Git
├── app.py                     # Application principale (probablement Flask ou Streamlit)
├── fraud_detection.pkl        # Modèle de détection de fraude sérialisé
├── fraud-detection.ipynb      # Notebook Jupyter pour l'exploration et le développement
├── Rapport_détection_de_fraude.pdf  # Documentation détaillée du projet
├── README.md                  # Ce fichier
└── requirements.txt           # Dépendances Python requises
```

## Description

Ce projet vise à détecter des activités frauduleuses à l'aide de techniques d'apprentissage automatique. Il comprend à la fois le développement du modèle (dans le notebook Jupyter) et une application web pour utiliser le modèle (via app.py).

## Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/tokosel/fraud_detection
cd fraud_detection
```

2. Créez et activez un environnement virtuel (optionnel mais recommandé) :
```bash
python -m venv env
# Sur Windows
env\Scripts\activate
# Sur macOS/Linux
source env/bin/activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

### Exécution de l'application web
```bash
python app.py
```
Accédez ensuite à l'application dans votre navigateur (généralement à l'adresse http://localhost:5000 ou celle indiquée dans la console).

### Exploration des données et du modèle
Vous pouvez explorer le processus de création du modèle en ouvrant le notebook Jupyter :
```bash
jupyter notebook fraud-detection.ipynb
```

## Documentation

Pour une documentation complète du projet, consultez le fichier `Rapport_détection_de_fraude.pdf`.

## Fonctionnalités

- Prétraitement des données financières
- Modèles de machine learning pour la détection d'anomalies
- Interface web pour l'analyse en temps réel
- Visualisation des résultats et des métriques de performance

## Technologies Utilisées

- Python
- Scikit-learn
- Flask / Vue JS / Html & tailwindcss
- Pandas, NumPy
- Matplotlib / Seaborn pour la visualisation
