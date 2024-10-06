
# Catégorisez automatiquement des questions

## Description

Ce projet vise à développer des modèles de classification multilabel capables de prédire des tags pour des questions StackOverflow. Différentes approches de traitement du langage naturel (NLP) sont explorées, notamment BERT, Word2Vec, et l’Universal Sentence Encoder (USE).

## Contenu du Dépôt

- **01_scrapping_stack_api.ipynb** : Script pour scrapper des données depuis l’API StackOverflow.
- **02_preprocessing.ipynb** : Prétraitement des données pour préparer les questions et les tags pour l’entraînement.
- **03.1_OneVsRest_v1.ipynb, 03.2_OneVsRest_v2.ipynb, 03.3_OneVsRest_v3.ipynb** : Implémentations de modèles de classification multilabel en utilisant une approche OneVsRest.
- **04_LDA.ipynb** : Analyse par Latent Dirichlet Allocation (LDA) pour comprendre les sujets des questions.
- **05_USE_v0.ipynb, 05_USE_v1.ipynb** : Utilisation de l’Universal Sentence Encoder pour l’embedding des questions.
- **06_Word2Vec_v0.ipynb, 06_Word2Vec_v1.ipynb, 06_Word2vec_v2.ipynb** : Approches basées sur Word2Vec pour l’embedding des questions.
- **07_BERT_training.ipynb** : Entraînement du modèle BERT pour la classification multilabel.
- **08_BERT_predict.ipynb** : Notebook pour faire des prédictions de tags à l’aide du modèle BERT entraîné.
- **main.py** : Script principal pour faire des prédictions à partir du modèle BERT hébergé sur Hugging Face depuis la ligne de commande.
- **flask_app/** : Application Flask pour déployer une interface web permettant de suggérer des tags pour des questions StackOverflow.
  - **app.py** : Script Flask principal pour l’application web.
  - **static/** : Dossier contenant les fichiers CSS et JavaScript pour styliser et dynamiser l’interface web.
    - **style.css** : Feuille de style pour le thème et l’apparence de l’application.
    - **app.js** : Fichier JavaScript pour la gestion du mode sombre et des interactions utilisateur.
    - **favicon.png** : Icône du site web pour l’application Flask.
  - **templates/** : Dossier contenant les fichiers HTML pour l’interface utilisateur.
    - **index.html** : Page principale de l’application web.
- **requirements.txt** : Liste des dépendances Python nécessaires pour exécuter le projet.
- **tests/** : Dossier contenant les tests unitaires pour le projet.
  - **test_fake_model.py** : Tests pour les modèles factices.
  - **test_main.py** : Tests pour le script main.py.

## Installation

Cette section explique comment installer toutes les dépendances nécessaires pour exécuter l'ensemble des notebooks, scripts et l'application Flask.

### 1. Prérequis
- Python **testé avec la version 3.11**.
- **Conseillé** : Créez un environnement virtuel pour isoler les dépendances du projet. Vous pouvez le faire en utilisant les commandes suivantes :

  ```bash
  python3 -m venv venv  # Créer un environnement virtuel nommé "venv"
  source venv/bin/activate  # Sur Linux/Mac
  venv\Scripts\activate  # Sur Windows
  ```

### 2. Installation des dépendances
Installez toutes les dépendances nécessaires listées dans `requirements.txt` :
```bash
pip install -r requirements.txt
```

## Utilisation du script principal

Le fichier `main.py` vous permet de prédire des tags pour une question StackOverflow directement depuis la ligne de commande.

### Exemple d'utilisation
Supposons que vous vouliez obtenir des tags pour la question suivante : 
`"How to generate a dataframe in python?"`.

Utilisez la commande suivante :

```bash
python main.py "How to generate a dataframe in python?"
```

Cela devrait retourner des tags comme : 
```
python, pandas
```

### Paramètres disponibles

Le script offre deux paramètres optionnels :

- **--threshold** : Ce paramètre définit le seuil de score minimum pour sélectionner les tags. Chaque tag prédit a un score de confiance compris entre 0 et 1, et seul un score supérieur au seuil défini sera pris en compte. Le seuil par défaut est de **0.5**.
  
  Exemple :
  ```bash
  python main.py "How to generate a dataframe in python?" --threshold 0.7
  ```
  Ici, seuls les tags avec un score de confiance supérieur à 0.7 seront retournés.

- **--max_answers** : Ce paramètre détermine le nombre maximal de tags à retourner. Le nombre par défaut est de **10**.
  
  Exemple :
  ```bash
  python main.py "How to generate a dataframe in python?" --max_answers 5
  ```
  Cela retournera au maximum 5 tags pertinents pour la question.

Ces paramètres permettent de personnaliser la prédiction des tags en fonction du contexte ou du niveau de confiance souhaité.

## Utilisation de l'application Flask

L'application Flask permet de déployer une interface web pour suggérer des tags pour des questions StackOverflow. Voici comment l'utiliser :

### 1. Lancer l'application Flask
Rendez-vous dans le répertoire `flask_app/` :
```bash
cd flask_app
```
Ensuite, lancez l'application Flask :
```bash
flask run
```
ou
```bash
python app.py
```

### 2. Accéder à l'interface web
Une fois l'application démarrée, vous pouvez accéder à l'interface web via votre navigateur à l'adresse :
```
http://127.0.0.1:5000/
```

### 3. Utiliser l'application
- Entrez une question StackOverflow dans le champ de texte.
- Cliquez sur "Predict Tags" pour obtenir les tags suggérés.

### 4. Mode développement (optionnel)
Pour activer le mode développement de Flask (avec rechargement automatique et affichage des erreurs), exécutez la commande suivante avant de lancer l'application :
```bash
export FLASK_ENV=development  # Sur Linux/Mac
set FLASK_ENV=development     # Sur Windows
```

