from sys import exit

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.image import imread
from sklearn.manifold import MDS
from sklearn.metrics import pairwise_distances

sns.set()


def make_hello(N=1000, rand_seed=42):
    fig, ax = plt.subplots(figsize=(4, 1))
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    ax.axis('off')
    ax.text(0.5, 0.4, 'hello', va='center', ha='center', weight='bold', size=85)
    fig.savefig('hello.png')
    plt.close(fig)

    data = imread('hello.png')[::-1, :, 0].T
    rng = np.random.RandomState(rand_seed)
    X = rng.rand(4 * N, 2)
    i, j = (X * data.shape).astype(int).T

    mask = (data[i, j] < 1)
    X = X[mask]

    X[:, 0] *= (data.shape[0] / data.shape[1])
    X = X[:N]

    return X[np.argsort(X[:, 0])]


def rotate(X, angle):
    theta = np.deg2rad(angle)
    R = [[np.cos(theta), np.sin(theta)], [-np.sign(theta), np.cos(theta)]]
    return np.dot(X, R)


def render_hello_image(X, color_params):
    plt.scatter(X[:, 0], X[:, 1], **color_params)
    plt.show()


def render_pairwise_distances(X):
    D = pairwise_distances(X)
    plt.imshow(D, zorder=2, interpolation='nearest')
    plt.colorbar()
    plt.show()


def convert_image_for_3d(X):
    rand = np.random.RandomState(42)
    C = rand.randn(3, 3)
    _, V = np.linalg.eigh(np.dot(C, C.T))
    return np.dot(X, V[:, X.shape[1]])


def main():
    X = make_hello()
    rotate_X = rotate(X, 20)
    color_params = dict(c=X[:, 0], cmap=plt.cm.get_cmap('rainbow', 10))

    render_hello_image(X, color_params)
    render_hello_image(rotate_X, color_params)

    render_pairwise_distances(X)
    render_pairwise_distances(rotate_X)

    model = MDS(n_components=2, dissimilarity='precomputed', random_state=1)
    result = model.fit_transform(pairwise_distances(X))

    render_hello_image(result, color_params)

    variant_3d = convert_image_for_3d(X)

    ax = plt.axes(projection='3d')
    ax.scatter3D(variant_3d[:, 0], variant_3d[:, 1], variant_3d[:, 2], color_params)
    plt.show()


if __name__ == '__main__':
    main()
    exit()
