from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_most_similar_papers(input_url, paper_urls, reduced_embeddings, top_n=3):
    # Find the index of the input paper URL
    input_index = paper_urls.index(input_url)

    # Compute cosine similarity between the input paper's embedding and all other embeddings
    input_embedding = reduced_embeddings[input_index].reshape(1, -1)
    similarities = cosine_similarity(input_embedding, reduced_embeddings)
    print(similarities,"similarities")
    # Get indices of the top_n most similar papers (excluding the input paper itself)
    sorted_indices = np.argsort(similarities[0])[::-1]
    top_indices = [idx for idx in sorted_indices if idx != input_index][:top_n]
    print(top_indices,"top indices")
    # Return the URLs of the most similar papers
    return [paper_urls[idx] for idx in top_indices]

"""# Example input paper URL
input_paper_url = "https://arxiv.org/abs/1905.07533"

# Recommend most similar papers
recommended_papers = get_most_similar_papers(input_paper_url, paper_urls, reduced_embeddings)
print("Recommended papers:")
for paper_url in recommended_papers:
    print(paper_url)"""