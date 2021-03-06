import sys
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


def plot_kmeans(kmeans, features, ax=None):
    labels = kmeans.fit_predict(features)

    ax = ax or plt.gca()
    ax.axis('equal')
    ax.scatter(features[:, 0], features[:, 1], c=labels, s=40, cmap='viridis',
               zorder=2)

    centers = kmeans.cluster_centers_
    radii = [cdist(features[labels == i], [center]).max()
             for i, center in enumerate(centers)]

    for c, r in zip(centers, radii):
        ax.add_patch(plt.Circle(c, r, fc='#CCCCCC', lw=3, alpha=0.3, zorder=1))


X, y_true = make_blobs(n_samples=400, centers=4, cluster_std=0.60,
                       random_state=0)
X = X[:, ::-1]  # flip axes for better plotting

kmeans_model = KMeans(n_clusters=4, random_state=0)
plot_kmeans(kmeans_model, X)

plt.show()
sys.exit()
