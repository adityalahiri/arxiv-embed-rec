import numpy as np
from sklearn.decomposition import PCA
import plotly.graph_objs as go
import plotly.io as pio
# Example embeddings

def pca_embeddings(embeddings):
    """embeddings = [
        np.random.rand(1, 768),
        np.random.rand(1, 768),
        np.random.rand(1, 768),
    ]"""

    # Convert list of embeddings to a single numpy array
    embeddings_array = np.vstack(embeddings)

    # Apply PCA to reduce dimensions
    n_components = 2  # Desired number of dimensions
    pca = PCA(n_components=n_components)
    reduced_embeddings = pca.fit_transform(embeddings_array)

    return reduced_embeddings
# Print reduced embeddings

import matplotlib.pyplot as plt

# Function to plot reduced embeddings
def plot_embeddings(embeddings, labels=None):
    plt.figure(figsize=(8, 6))

    if labels is not None:
        for idx, label in enumerate(labels):
            plt.scatter(embeddings[idx, 0], embeddings[idx, 1], label=label)
        plt.legend(loc='best')
    else:
        plt.scatter(embeddings[:, 0], embeddings[:, 1])

    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('PCA-Reduced Embeddings')
    plt.show()

"""# Example labels (optional)
labels = ['Abstract 1', 'Abstract 2', 'Abstract 3']

# Plot reduced embeddings
plot_embeddings(reduced_embeddings, labels=labels)"""

# Function to plot reduced embeddings with hover information
def plot_embeddings_plotly(embeddings, titles):
    trace = go.Scatter(
        x=embeddings[:, 0],
        y=embeddings[:, 1],
        mode='markers',
        marker=dict(size=10),
        text=titles,
        hovertemplate='%{text}<extra></extra>'
    )

    layout = go.Layout(
        title='PCA-Reduced Embeddings',
        xaxis_title='Principal Component 1',
        yaxis_title='Principal Component 2',
        hovermode='closest'
    )

    fig = go.Figure(data=[trace], layout=layout)
    pio.show(fig)
