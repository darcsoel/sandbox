"""Lasso regression visualization"""

import sys

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LassoLarsCV

if __name__ == '__main__':
    X, y = make_regression(noise=4.0, random_state=0)
    model = LassoLarsCV(cv=5, max_n_alphas=5).fit(X, y)

    fig, ax = plt.subplots(figsize=(8, 8))

    color_map = iter(plt.get_cmap('tab20')(np.linspace(0, 1, X.shape[1])))

    for i in range(X.shape[1]):
        c = next(color_map)
        ax.plot(model.alphas_, model.coef_path_.T[:, i], c=c, alpha=0.8)

    ax.axvline(model.alpha_, linestyle='-', c='k', label='alpha')

    plt.ylabel('regression coefficients')
    plt.xlabel('alpha')
    plt.title('regression coefficients for lasso')

    plt.show()
    sys.exit()
