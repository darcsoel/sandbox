import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
from sklearn.datasets import make_circles
from sklearn.svm import SVC

mplot3d.Axes3D  # just for IDE keep import after 'optimize imports'


def show_model_discrimination(model, ax):
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    x = np.linspace(xlim[0], xlim[1], 30)
    y = np.linspace(ylim[0], ylim[1], 30)

    Y, X = np.meshgrid(y, x)
    xy = np.vstack([X.ravel(), Y.ravel()]).T
    P = model.decision_function(xy).reshape(X.shape)

    ax.contour(X, Y, P, levels=[-1, 0, 1], alpha=0.5, linstyles=['--', '-', '--'])
    ax.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=300)

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)


def main():
    dataset_len = 100
    n_rows = 2
    n_cols = 2

    X, y = make_circles(100, factor=.1, noise=.1)

    plt.subplot(n_rows, n_cols, 1)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=dataset_len, alpha=0.4, cmap='winter')

    r = np.exp((-X ** 2).sum(1))  # add projection

    ax = plt.subplot(n_rows, n_cols, 2, projection='3d')
    ax.scatter3D(X[:, 0], X[:, 1], r, c=y, s=dataset_len, alpha=0.4, cmap='spring')

    model = SVC(kernel='rbf', C=1e6)
    model.fit(X, y)

    ax = plt.subplot(n_rows, n_cols, 3)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=dataset_len, alpha=0.4, cmap='summer')
    show_model_discrimination(model, ax)
    plt.show()


if __name__ == '__main__':
    main()
    exit()
