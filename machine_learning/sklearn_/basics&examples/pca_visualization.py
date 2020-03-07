import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.decomposition import PCA


def print_vector(v0, v1):
    ax = plt.gca()
    props = dict(arrowstyle='<-', linewidth=2, shrinkA=0, shrinkB=0, color='black')
    ax.annotate('', v0, v1, arrowprops=props)


def main():
    sns.set()

    rnd = np.random.RandomState(1)
    X = np.dot(rnd.rand(2, 2), rnd.randn(2, 200)).T

    plt.subplot(2, 1, 1)
    plt.scatter(X[:, 0], X[:, 1], alpha=0.5)

    model = PCA(n_components=2)
    model.fit(X)

    for length, vector in zip(model.explained_variance_, model.components_):
        v = vector * 3 * np.sqrt(length)
        print_vector(model.mean_, model.mean_ + v)

    plt.axis('equal')

    plt.subplot(2, 1, 2)

    one_dim_model = PCA(n_components=1)
    one_dim_model.fit(X)

    new_X = one_dim_model.transform(X)
    one_dim_x = one_dim_model.inverse_transform(new_X)
    plt.scatter(one_dim_x[:, 0], one_dim_x[:, 1], alpha=0.5)

    plt.show()


if __name__ == '__main__':
    main()
