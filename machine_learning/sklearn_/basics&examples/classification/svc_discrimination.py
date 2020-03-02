import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.svm import SVC


def show_model_discrimination(model):
    ax = plt.gca()
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
    samples_count = 50

    X, y = make_blobs(n_samples=samples_count, centers=2)

    svc_model = SVC(kernel='linear', C=1e10)
    svc_model.fit(X, y)

    plt.scatter(X[:, 0], X[:, 1], c=y, s=samples_count, alpha=0.4, cmap='winter')
    show_model_discrimination(svc_model)
    plt.show()


if __name__ == '__main__':
    main()
    exit()
