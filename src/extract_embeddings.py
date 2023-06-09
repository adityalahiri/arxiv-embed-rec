from transformers import AutoTokenizer, AutoModel
import torch
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Function to get embeddings from abstracts
def get_embeddings(abstracts):

    # Load a pre-trained model and tokenizer
    model_name = "bert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    embeddings = []

    for abstract in abstracts:
        # Tokenize the abstract
        inputs = tokenizer(abstract, return_tensors="pt", padding=True, truncation=True)

        # Get the output from the model
        with torch.no_grad():
            outputs = model(**inputs)

        # Extract the embedding (CLS token)
        embedding = outputs.last_hidden_state[:, 0, :].numpy()
        embeddings.append(embedding)

    return embeddings
