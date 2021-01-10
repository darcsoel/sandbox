import sys

import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

if __name__ == '__main__':
    random_numbers = np.random.rand(10).reshape(-1, 1)
    random_numbers *= 10

    plt.plot(random_numbers)
    plt.show()

    scaled = StandardScaler().fit_transform(random_numbers)

    plt.plot(scaled)
    plt.show()

    scaled = MinMaxScaler().fit_transform(random_numbers)

    plt.plot(scaled)
    plt.show()

    print(random_numbers)
    print(scaled)

    sys.exit()
