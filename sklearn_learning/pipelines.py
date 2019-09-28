from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import Normalizer, StandardScaler

model = Pipeline([
    ('normalizer', Normalizer()),
    ('classifier', MultinomialNB())
])
