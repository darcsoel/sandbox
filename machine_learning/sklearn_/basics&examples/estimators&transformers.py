import sys
import pandas as pd
from sklearn.impute import SimpleImputer

if __name__ == '__main__':
    imputer = SimpleImputer(strategy='median')

    dataset = pd.read_csv('titanic.csv')
    dataset.drop(['Cabin', 'Name', 'Sex', 'Ticket', 'Embarked', 'Cabin'],
                 axis=1, inplace=True)

    imputer.fit(dataset)

    x = imputer.transform(dataset)

    new_dataset = pd.DataFrame(x, columns=dataset.columns)

    sys.exit()
