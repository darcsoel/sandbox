import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.svm import SVC

plot_blocks = 2
plot_cols = 1

X, y = make_blobs(n_samples=200, n_features=3, centers=3)

plt.subplot(plot_blocks, plot_cols, 1)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, alpha=0.4, cmap='winter')
plt.show()

model = SVC(kernel='linear', C=1e10)
model.fit(X, y)


def show_model_discrimination():
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    grid_x = np.linspace(xlim[0], xlim[1])
    grid_y = np.linspace(ylim[0], ylim[1])



exit()
