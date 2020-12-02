import sys
from itertools import zip_longest

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE

if __name__ == '__main__':
    data = pd.read_csv('../../../../titanic.csv', index_col=['PassengerId'])
    data.drop(columns=['Name', 'Ticket', 'Cabin'], inplace=True)

    data.loc[data['Sex'] == 'male', 'Sex'] = 1
    data.loc[data['Sex'] == 'female', 'Sex'] = 0

    data['Age'] = data['Age'].fillna(0)
    data['Embarked'] = data['Embarked'].fillna('zero')
    data.loc[data['Embarked'] == 'S', 'Embarked'] = 1
    data.loc[data['Embarked'] == 'C', 'Embarked'] = 2
    data.loc[data['Embarked'] == 'Q', 'Embarked'] = 3
    data.loc[data['Embarked'] == 'zero', 'Embarked'] = 0

    X = data.copy()
    X.drop(columns=['Survived'], inplace=True)
    y = data['Survived']

    model = RandomForestClassifier().fit(X, y)

    rfe = RFE(model, 4)
    rfe.fit(X, y)

    for i, j in zip_longest(list(X.columns), rfe.support_):
        print(f'{i} => {j}')

    sys.exit()
