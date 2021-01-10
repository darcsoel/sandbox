"""Primitive df creation example"""


import sys

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

if __name__ == '__main__':
    np.random.seed(0)

    numbers = np.random.rand(25).reshape((5, 5))

    df = pd.DataFrame(numbers, index=[f'row{i}' for i in range(5)],
                      columns=[f'column{i}' for i in range(5)])

    print(df.head())

    df.plot()
    plt.show()

    df.plot(kind='bar')
    plt.show()

    plt.pie(df['column1'])
    plt.show()

    sys.exit()
