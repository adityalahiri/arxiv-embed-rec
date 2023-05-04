from fetch import fetch_abstracts_and_related
from extract_embeddings import get_embeddings
from reduce_emb_dims import pca_embeddings, plot_embeddings,plot_embeddings_plotly
from recommend import get_most_similar_papers
import re
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from plotly import graph_objects as go
import feedparser
if __name__=="__main__":
    # Given paper URLs
    paper_urls = [
        "https://arxiv.org/abs/1802.03888",
        "https://arxiv.org/abs/2206.07087",
        "https://arxiv.org/abs/2303.16199",
        "https://arxiv.org/abs/2212.10554",
    ]

    # Extract paper IDs from URLs
    all_abstracts = []
    all_titles = []
    paper_ids = [re.search(r"(\d+\.\d+)", url).group(0) for url in paper_urls]
    for paper_id in paper_ids:
        paper_info = feedparser.parse(f"http://export.arxiv.org/api/query?id_list={paper_id}")
        paper = paper_info.entries[0]
        all_abstracts.append(paper.summary)
        all_titles.append(paper.title)
    all_urls = paper_urls
    # Fetch abstracts and related papers' abstracts
    for paper_id in paper_ids:
        related_papers=fetch_abstracts_and_related(paper_id,max_related=5)
        abstracts = [paper.summary for paper in related_papers]
        #print(paper_id)
        for each in abstracts:
            print("THIS ABSTRACT",each)
            print("-----")
        urls = [paper.link for paper in related_papers]
        titles = [paper.title for paper in related_papers]
        all_abstracts.extend(abstracts)
        all_titles.extend(titles)
        all_urls.extend(urls)
    # Get embeddings for abstracts
    embeddings = get_embeddings(all_abstracts)
    all_pca_embeddings = pca_embeddings(embeddings, n_components=20)
    #plot_embeddings_plotly(all_pca_embeddings, all_titles)
    rec=get_most_similar_papers(all_urls[0], all_urls, all_pca_embeddings, top_n=3)
    print(rec)
    #plot_embeddings(all_pca_embeddings, labels=all_titles)