import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor


# copied helper function from PythonDataScienceHandbook github
def visualize_tree(estimator, X, y, xlim=None, ylim=None, ax=None):
    """
    copied helper function from PythonDataScienceHandbook github

    :param estimator: fitted estimator
    :param X: features
    :param y: labels
    :param xlim:
    :param ylim:
    :param ax:
    :return:
    """
    ax = ax or plt.gca()

    # Plot the training points
    ax.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap='viridis', clim=(y.min(), y.max()), zorder=3)
    ax.axis('tight')
    ax.axis('off')
    if xlim is None:
        xlim = ax.get_xlim()
    if ylim is None:
        ylim = ax.get_ylim()

    xx, yy = np.meshgrid(np.linspace(*xlim, num=200), np.linspace(*ylim, num=200))
    Z = estimator.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    n_classes = len(np.unique(y))
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.3, levels=np.arange(n_classes + 1) - 0.5, cmap='viridis')

    ax.set(xlim=xlim, ylim=ylim)
    plt.show()


def main():
    x, y = make_blobs(n_samples=300, centers=4)

    ensemble = RandomForestRegressor(verbose=3)
    ensemble.fit(x, y)

    visualize_tree(ensemble, x, y)


if __name__ == '__main__':
    main()
