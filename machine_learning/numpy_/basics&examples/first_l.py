import sys
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sbr

sbr.set()

if __name__ == '__main__':
    rand = np.random.RandomState()

    mean = [0, 0]
    covariance = [[1, 2], [2, 5]]

    x = rand.multivariate_normal(mean, covariance, 100)
    print(x.shape)

    plt.scatter(x[:, 0], x[:, 1], alpha=0.3)

    indexes = np.random.choice(x.shape[0], 20, replace=False)
    print(indexes.shape)

    selection = x[indexes]
    print(selection.shape)

    plt.scatter(selection[:, 0], selection[:, 1],
                s=200, facecolor='blue', alpha=0.25)
    plt.show()

    sys.exit()
