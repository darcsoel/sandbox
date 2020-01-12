from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

model = Pipeline([
    PolynomialFeatures, LinearRegression
])


def build_dataset():
    x = list(range(100))