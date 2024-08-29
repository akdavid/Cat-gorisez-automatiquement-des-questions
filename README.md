# Projet OpenClassrooms : Catégorisez automatiquement des questions

## Description

Ce projet vise à développer des modèles de classification multilabel capables de prédire des tags pour des questions StackOverflow. Différentes approches de traitement du langage naturel (NLP) sont explorées, notamment BERT, Word2Vec, et l’Universal Sentence Encoder (USE).

## Contenu du Dépôt

- 01_scrapping_stack_api.ipynb : Script pour scrapper des données depuis l’API StackOverflow.
- 02_preprocessing.ipynb : Prétraitement des données pour préparer les questions et les tags pour l’entraînement.
- 03.1_OneVsRest_v1.ipynb, 03.2_OneVsRest_v2.ipynb, 03.3_OneVsRest_v3.ipynb : Implémentations de modèles de classification multilabel en utilisant une approche OneVsRest.
- 04_LDA.ipynb : Analyse par Latent Dirichlet Allocation (LDA) pour comprendre les sujets des questions.
- 05_USE_v0.ipynb, 05_USE_v1.ipynb : Utilisation de l’Universal Sentence Encoder pour l’embedding des questions.
- 06_Word2Vec_v0.ipynb, 06_Word2Vec_v1.ipynb, 06_Word2vec_v2.ipynb : Approches basées sur Word2Vec pour l’embedding des questions.
- 07_BERT_training.ipynb : Entraînement du modèle BERT pour la classification multilabel.
- 08_BERT_predict.ipynb : Notebook pour faire des prédictions de tags à l’aide du modèle BERT entraîné.
- main.py : Script principal pour faire des prédictions à partir du modèle BERT hébergé sur Hugging Face depuis la ligne de commande.
- flask_app/ : Application Flask pour déployer une interface web permettant de suggérer des tags pour des questions StackOverflow.
  - app.py : Script Flask principal pour l’application web.
  - static/ : Dossier contenant les fichiers CSS et JavaScript pour styliser et dynamiser l’interface web.
    - style.css : Feuille de style pour le thème et l’apparence de l’application.
    - app.js : Fichier JavaScript pour la gestion du mode sombre et des interactions utilisateur.
    - favicon.png : Icône du site web pour l’application Flask.
  - templates/ : Dossier contenant les fichiers HTML pour l’interface utilisateur.
    - index.html : Page principale de l’application web.
- requirements.txt : Liste des dépendances Python nécessaires pour exécuter le projet.
- tests/ : Dossier contenant les tests unitaires pour le projet.
  - test_fake_model.py : Tests pour les modèles factices.
  - test_main.py : Tests pour le script main.py.
