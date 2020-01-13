from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_classification

model = make_pipeline(
    StandardScaler, LinearRegression
)

x, y = make_classification(random_state=42)
