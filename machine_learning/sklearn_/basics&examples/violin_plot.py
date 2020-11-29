import sys

import matplotlib.pyplot as plt
import seaborn

if __name__ == '__main__':
    x = [[1, 2, 3], [1, 2, 1], [3, 4, 5, 4], [3, 4, 3, 2]]
    fig, plot = plt.subplots(figsize=(8, 6))
    # діаграма розмаху
    seaborn.violinplot(data=x)

    plt.show()

    sys.exit()
