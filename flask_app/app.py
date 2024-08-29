from flask import Flask, request, render_template, jsonify
from transformers import pipeline

app = Flask(__name__)

# Nom du modèle sur Hugging Face
model_name = 'akdavid/bert-multilabel-classification-stackoverflow-tags'

# Créer le pipeline de classification de texte depuis Hugging Face
pipe = pipeline(
    "text-classification", 
    model=model_name, 
    tokenizer=model_name, 
    return_all_scores=True, 
    function_to_apply='sigmoid'
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Utiliser le pipeline pour obtenir des prédictions
    predictions = pipe(text)

    # Filtrer les résultats en fonction du seuil
    threshold = 0.5
    recommended_tags = [
        output['label'] for output in predictions[0] if output['score'] > threshold
    ]

    return jsonify({
        "input_text": text,
        "predicted_tags": recommended_tags
    })

if __name__ == "__main__":
    app.run(debug=True)