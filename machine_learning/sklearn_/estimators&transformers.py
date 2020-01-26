import pandas as pd
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='median')

dataset = pd.read_csv('../../titanic.csv')
dataset.drop('Cabin', axis=1, inplace=True)

imputer.fit(dataset)

x = imputer.transform(dataset)

new_dataset = pd.DataFrame(x, columns=dataset.columns)
