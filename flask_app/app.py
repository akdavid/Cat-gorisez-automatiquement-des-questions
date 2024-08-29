from flask import Flask, request, jsonify
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
    return '''
        <h1>Tag Prediction with BERT</h1>
        <form action="/predict" method="post">
            <label for="text">Enter your text:</label><br>
            <textarea id="text" name="text" rows="4" cols="50"></textarea><br>
            <input type="submit" value="Predict Tags">
        </form>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Utiliser le pipeline pour obtenir des prédictions
    predictions = pipe(text)

    # Print the predictions to inspect their structure
    print("Predictions:", predictions)

    # Filtrer les résultats en fonction du seuil
    threshold = 0.5

    # Handle different formats of predictions
    recommended_tags = []
    for pred in predictions:
        if isinstance(pred, list):
            for output in pred:
                if output['score'] > threshold:
                    recommended_tags.append(output['label'])
        elif isinstance(pred, dict):
            if pred['score'] > threshold:
                recommended_tags.append(pred['label'])

    return jsonify({
        "input_text": text,
        "predicted_tags": recommended_tags
    })

if __name__ == "__main__":
    app.run(debug=True)