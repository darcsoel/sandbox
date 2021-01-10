import numpy as np

import sys

if __name__ == '__main__':
    first = np.random.rand(3, 3)
    second = np.random.rand(3, 3)

    result = first * second
    print(result)

    sys.exit()
