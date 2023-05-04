from transformers import AutoTokenizer, AutoModel
import torch
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# List of abstracts
abstracts = [
    "Abstract 1",
    "Abstract 2",
    "Abstract 3",
]

# Load a pre-trained model and tokenizer
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Function to get embeddings from abstracts
def get_embeddings(abstracts):
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

"""# Get embeddings for abstracts
embeddings = get_embeddings(abstracts)

# Print embeddings
for idx, embedding in enumerate(embeddings):
    print(f"Embedding {idx + 1}:\n{embedding}\n")"""
