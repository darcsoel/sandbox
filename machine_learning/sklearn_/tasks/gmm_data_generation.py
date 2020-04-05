from sys import exit

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture


def plot_digits(digits):
    fig, axes = plt.subplots(4, 10, figsize=(10, 4), subplot_kw={'xticks': [], 'yticks': []})

    for i, ax in enumerate(axes.flat):
        try:
            ax.imshow(digits[i].reshape(8, 8), cmap='binary', interpolation='nearest')
        except IndexError:
            continue

    plt.show()


def plot_gmm_model_components_aic(data):
    n_components = np.arange(40, 250, 10)

    models = [GaussianMixture(n, covariance_type='full', random_state=0) for n in n_components]
    aic_data = [model.fit(data).aic(data) for model in models]

    plt.plot(n_components, aic_data)
    plt.show()


def main():
    digits, _ = load_digits(return_X_y=True)

    plot_digits(digits)

    pca_model = PCA(0.99, whiten=True)
    data = pca_model.fit_transform(digits)

    plot_gmm_model_components_aic(data)

    gmm_model = GaussianMixture(150, covariance_type='full', random_state=0)  # from plot_gmm_model_components_aic
    gmm_model.fit(data)

    new_digits = gmm_model.sample(n_samples=40)
    generated = pca_model.inverse_transform(new_digits[0])

    plot_digits(generated)
    print(f'Generated labels = {new_digits[1]}')


if __name__ == '__main__':
    main()
    exit()
