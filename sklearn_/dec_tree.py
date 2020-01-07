import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('../titanic.csv')

features = data[['Pclass', 'Fare', 'Age', 'Sex', 'Survived']].replace('male', 2).replace('female', 1).dropna()
result = features['Survived']
features.drop(columns=['Survived'], axis=1, inplace=True)

tree = DecisionTreeClassifier(random_state=241)
tree.fit(features, result)

res = tree.predict([[1, 60.5, 35, 1]])
print(res)

res = tree.predict([[1, 10.5, 35, 2]])
print(res)
