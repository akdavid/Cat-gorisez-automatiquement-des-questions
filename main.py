import torch
import argparse
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

# Nom du modèle sur Hugging Face
model_name = 'akdavid/bert-multilabel-classification-stackoverflow-tags'

# Sélection automatique du device
if torch.cuda.is_available():
    device = 'cuda'
elif torch.backends.mps.is_available():
    device = 'mps'
else:
    device = 'cpu'
    
print(f"Using device: {device}")

# Charger le tokenizer et le modèle depuis Hugging Face
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.to(device)

# Créer le pipeline de classification de texte
pipe = TextClassificationPipeline(
    model=model, 
    tokenizer=tokenizer, 
    return_all_scores=True, 
    device=0 if device == 'cuda' else -1,  # Utilise 0 pour le GPU ou -1 pour CPU/MPS
    task="multi_label_classification",
    function_to_apply='sigmoid'
)

def pred_ep(text, thresh=0.5, max_answers=10):
    """
    Prédit les tags les plus pertinents pour un texte donné.

    Args:
    - text (str): Le texte d'entrée.
    - thresh (float): Le seuil de score pour sélectionner les tags.
    - max_answers (int): Le nombre maximal de tags à retourner.

    Returns:
    - list: Une liste de tags recommandés.
    """
    global pipe
    
    # Utiliser le pipeline pour obtenir des prédictions
    pipe_output = pipe(text, top_k=max_answers)

    # Filtrer les résultats en fonction du seuil
    recommended_tags = [
        dict_output['label'] for dict_output in pipe_output if dict_output['score'] > thresh
    ]
    
    return recommended_tags

if __name__ == "__main__":
    # Configurer l'analyseur d'arguments
    parser = argparse.ArgumentParser(description="Predict tags for a given text using a BERT model.")
    parser.add_argument('text', type=str, help="The input text to predict tags for.")
    parser.add_argument('--threshold', type=float, default=0.5, help="Score threshold for selecting tags (default: 0.5).")
    parser.add_argument('--max_answers', type=int, default=10, help="Maximum number of tags to return (default: 10).")

    # Analyser les arguments
    args = parser.parse_args()

    # Faire les prédictions
    predictions = pred_ep(args.text, thresh=args.threshold, max_answers=args.max_answers)
    
    # Afficher les prédictions
    print("Predicted Tags:", predictions)