import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA


def plot_digits(digits, label):
    fig, axes = plt.subplots(4, 10, figsize=(10, 4), subplot_kw={'xticks': [], 'yticks': []})

    for i, ax in enumerate(axes.flat):
        ax.imshow(digits[i].reshape(8, 8), cmap='binary', interpolation='nearest')
        ax.text(0, 7, str(label[i]))

    plt.show()


def main():
    digits, labels = load_digits(return_X_y=True)

    np.random.seed(42)
    noise = np.random.normal(digits, 4)

    plot_digits(noise, labels)

    pca = PCA(0.5)
    pca.fit(noise)

    trained = pca.transform(noise)
    filtered = pca.inverse_transform(trained)
    plot_digits(filtered, labels)


if __name__ == '__main__':
    main()
