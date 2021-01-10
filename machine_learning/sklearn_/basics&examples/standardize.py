import sys

import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import scale

if __name__ == '__main__':
    random_numbers = np.random.rand(10).reshape(-1, 1)
    random_numbers *= 10

    plt.plot(random_numbers)
    plt.show()

    standardized = scale(random_numbers)

    plt.plot(standardized)
    plt.show()

    sys.exit()
