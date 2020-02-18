import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures


def main():
    """create main func to create variables in local scope"""

    rng = np.random.RandomState(1)
    x_train = 10 * rng.rand(50)
    y_train = np.sin(x_train) + 0.1 * rng.randn(50)

    x_test = 10 * rng.rand(10)

    model = make_pipeline(PolynomialFeatures(6), LinearRegression())
    model.fit(x_train[:, np.newaxis], y_train)

    y_test = model.predict(x_test[:, np.newaxis])

    plt.scatter(x_train, y_train)
    plt.plot(x_test, y_test)
    plt.show()


if __name__ == '__main__':
    main()
    exit()
