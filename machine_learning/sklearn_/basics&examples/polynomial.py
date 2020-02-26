import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures


def main():
    """create main func to create variables in local scope"""

    dataset_length = 100

    rng = np.random.RandomState(1)
    x_train = 10 * rng.rand(dataset_length)
    y_train = np.sin(x_train) + 0.1 * rng.randn(dataset_length)

    x_test = np.linspace(0, 10, dataset_length)

    model = make_pipeline(PolynomialFeatures(6), LinearRegression())
    model.fit(x_train[:, np.newaxis], y_train)

    y_test = model.predict(x_test[:, np.newaxis])

    plt.scatter(x_train, y_train)
    plt.plot(x_test, y_test)
    plt.show()


if __name__ == '__main__':
    main()
    exit()
