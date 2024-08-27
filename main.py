import torch
import argparse
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

# Define the model path
model_path = '/Users/anthonydavid/Workspace/Openclassrooms/projet_5/2024-08-19_15-10-53-bert-model'

# Automatic device selection
if torch.cuda.is_available():
    device = 'cuda'
elif torch.backends.mps.is_available():
    device = 'mps'
else:
    device = 'cpu'
    
print(f"Using device: {device}")

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
model = AutoModelForSequenceClassification.from_pretrained(model_path)
model.to(device)

# Create the text classification pipeline
pipe = TextClassificationPipeline(
    model=model, 
    tokenizer=tokenizer, 
    return_all_scores=True, 
    device=0 if device == 'cuda' else -1,  # Use 0 for GPU or -1 for CPU/MPS
    task="multi_label_classification",
    function_to_apply='sigmoid'
)

def pred_ep(text, thresh=0.5, max_answers=10):
    """
    Predicts the most relevant tags for a given text.

    Args:
    - text (str): The input text.
    - thresh (float): The score threshold for selecting tags.
    - max_answers (int): The maximum number of tags to return.

    Returns:
    - list: A list of recommended tags.
    """
    global pipe
    
    # Use the pipeline to get predictions
    pipe_output = pipe(text, top_k=max_answers)

    # Filter the results based on the threshold
    recommended_tags = [
        dict_output['label'] for dict_output in pipe_output if dict_output['score'] > thresh
    ]
    
    return recommended_tags

if __name__ == "__main__":
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Predict tags for a given text using a BERT model.")
    parser.add_argument('text', type=str, help="The input text to predict tags for.")
    parser.add_argument('--threshold', type=float, default=0.5, help="Score threshold for selecting tags (default: 0.5).")
    parser.add_argument('--max_answers', type=int, default=10, help="Maximum number of tags to return (default: 10).")

    # Parse the arguments
    args = parser.parse_args()

    # Make predictions
    predictions = pred_ep(args.text, thresh=args.threshold, max_answers=args.max_answers)
    
    # Print the predictions
    print("Predicted Tags:", predictions)