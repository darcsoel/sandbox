import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('../../titanic.csv')

x = data[['Pclass', 'Fare', 'Age', 'Sex', 'Survived']].replace('male', 2).replace('female', 1).dropna()
y = x['Survived']
x.drop(columns=['Survived'], axis=1, inplace=True)

tree = DecisionTreeClassifier(random_state=241)
tree.fit(x, y)

res = tree.predict([[1, 60.5, 35, 1]])
print(res)

res = tree.predict([[1, 10.5, 35, 2]])
print(res)
