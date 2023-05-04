Take a seed set of topics and arxiv paper links.
Get related papers, pass them into pretrained LM
Plot in reduced dimension
Propagate and obtain more relevant papers and
strive to get a better recommender system for papers.

Modular options 

[paper fetch] : co-authors, same domain, by time, custom
[embeddings] : BERT, GPT, custom-model
[dim-reduction] : PCA, t-SNE, Embedding layer
[similarity-measure] : cosine, jaccard, euclidean, manhattan