import matplotlib.pyplot as plt
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.pipeline import make_pipeline


class SquareFeatures(BaseEstimator, TransformerMixin):
    """Uniformly spaced square features for one-dimensional input"""

    def __init__(self, centers_count, width_factor=2.0):
        self._centers_count = centers_count
        self._width_factor = width_factor
        self._centers, self._width = None, None

    @staticmethod
    def _square_features(square_x, square_y, width, axis=None):
        arg = (square_x - square_y) / width
        return np.sqrt(1 + np.sum(arg ** 2, axis))

    def fit(self, fit_x, fit_y=None):
        self._centers = np.linspace(fit_x.min(), fit_x.max(), self._centers_count)
        self._width = self._width_factor * (self._centers[1] - self._centers[0])
        return self

    def transform(self, fit_x):
        return self._square_features(fit_x[:, :, np.newaxis], self._centers, self._width, axis=1)


dataset_length = 50
rng = np.random.RandomState(1)

x = 10 * rng.rand(dataset_length)
y = np.sin(x) + 0.1 * rng.randn(dataset_length)

square_model = make_pipeline(SquareFeatures(20), LinearRegression())
square_model.fit(x[:, np.newaxis], y)

x_fit = np.linspace(0, 10, dataset_length)
y_fit = square_model.predict(x_fit[:, np.newaxis])

plt.subplot(3, 1, 1)
plt.scatter(x, y)
plt.plot(x_fit, y_fit)
plt.xlim(0, 10)

square_model = make_pipeline(SquareFeatures(20), Ridge(alpha=0.1))
square_model.fit(x[:, np.newaxis], y)

x_fit = np.linspace(0, 10, dataset_length)
y_fit = square_model.predict(x_fit[:, np.newaxis])

plt.subplot(3, 1, 2)
plt.scatter(x, y)
plt.plot(x_fit, y_fit)
plt.xlim(0, 10)

square_model = make_pipeline(SquareFeatures(20), Lasso(alpha=0.001))
square_model.fit(x[:, np.newaxis], y)

x_fit = np.linspace(0, 10, dataset_length)
y_fit = square_model.predict(x_fit[:, np.newaxis])

plt.subplot(3, 1, 3)
plt.scatter(x, y)
plt.plot(x_fit, y_fit)
plt.xlim(0, 10)

plt.show()
exit()
