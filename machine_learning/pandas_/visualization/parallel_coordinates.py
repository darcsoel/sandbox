import sys

import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import parallel_coordinates

if __name__ == '__main__':
    fig, ax = plt.subplots(figsize=(8, 8))

    x = pd.DataFrame(pd.read_csv('titanic.csv'))
    x.drop(columns=['Name', 'Ticket', 'Cabin', 'Embarked', 'PassengerId'],
           inplace=True)
    x['Sex'].replace({'male': 1, 'female': 0}, inplace=True)

    parallel_coordinates(x, 'Survived', ax=ax, colormap='autumn', alpha=0.5)
    plt.show()
    sys.exit()
