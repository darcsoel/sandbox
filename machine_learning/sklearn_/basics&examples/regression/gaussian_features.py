import matplotlib.pyplot as plt
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.pipeline import make_pipeline


class GaussianFeatures(BaseEstimator, TransformerMixin):
    """Uniformly spaced Gaussian features for one-dimensional input"""

    def __init__(self, centers_count, width_factor=2.0):
        self._centers_count = centers_count
        self._width_factor = width_factor
        self._centers, self._width = None, None

    @staticmethod
    def _gauss_basis(gauss_x, gauss_y, width, axis=None):
        arg = (gauss_x - gauss_y) / width
        return np.exp(-0.5 * np.sum(arg ** 2, axis))

    def fit(self, fit_x, fit_y=None):
        self._centers = np.linspace(fit_x.min(), fit_x.max(), self._centers_count)
        self._width = self._width_factor * (self._centers[1] - self._centers[0])
        return self

    def transform(self, fit_x):
        return self._gauss_basis(fit_x[:, :, np.newaxis], self._centers, self._width, axis=1)


dataset_length = 50
rng = np.random.RandomState(1)

x = 10 * rng.rand(dataset_length)
y = np.sin(x) + 0.1 * rng.randn(dataset_length)

gauss_model = make_pipeline(GaussianFeatures(20), LinearRegression())
gauss_model.fit(x[:, np.newaxis], y)

x_fit = np.linspace(0, 10, dataset_length)
y_fit = gauss_model.predict(x_fit[:, np.newaxis])

plt.subplot(3, 1, 1)
plt.scatter(x, y)
plt.plot(x_fit, y_fit)
plt.xlim(0, 10)

gauss_model = make_pipeline(GaussianFeatures(20), Ridge(alpha=0.1))
gauss_model.fit(x[:, np.newaxis], y)

x_fit = np.linspace(0, 10, dataset_length)
y_fit = gauss_model.predict(x_fit[:, np.newaxis])

plt.subplot(3, 1, 2)
plt.scatter(x, y)
plt.plot(x_fit, y_fit)
plt.xlim(0, 10)

gauss_model = make_pipeline(GaussianFeatures(20), Lasso(alpha=0.01))
gauss_model.fit(x[:, np.newaxis], y)

x_fit = np.linspace(0, 10, dataset_length)
y_fit = gauss_model.predict(x_fit[:, np.newaxis])

plt.subplot(3, 1, 3)
plt.scatter(x, y)
plt.plot(x_fit, y_fit)
plt.xlim(0, 10)

plt.show()
exit()
