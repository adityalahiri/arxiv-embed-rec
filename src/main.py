from fetch import fetch_abstracts_and_related
from extract_embeddings import get_embeddings
from reduce_emb_dims import pca_embeddings, plot_embeddings,plot_embeddings_plotly
import re
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from plotly import graph_objects as go
if __name__=="__main__":
    # Given paper URLs
    paper_urls = [
        "https://arxiv.org/abs/1905.07533",
        "https://arxiv.org/abs/2104.03353",
        "https://arxiv.org/abs/2303.16199",
        "https://arxiv.org/abs/2212.10554",
    ]

    # Extract paper IDs from URLs
    paper_ids = [re.search(r"(\d+\.\d+)", url).group(0) for url in paper_urls]
    all_abstracts = []
    all_titles = []
    # Fetch abstracts and related papers' abstracts
    for paper_id in paper_ids:
        related_papers=fetch_abstracts_and_related(paper_id,max_related=10)
        abstracts = [paper.summary for paper in related_papers]
        titles = [paper.title for paper in related_papers]
        all_abstracts.extend(abstracts)
        all_titles.extend(titles)
    
    # Get embeddings for abstracts
    embeddings = get_embeddings(all_abstracts)
    all_pca_embeddings = pca_embeddings(embeddings)
    plot_embeddings_plotly(all_pca_embeddings, all_titles)
    #plot_embeddings(all_pca_embeddings, labels=all_titles)