import sys
from sktime.datasets import load_airline
from sktime.forecasting.model_selection import temporal_train_test_split
from sktime.utils.plotting.forecasting import plot_ys
import matplotlib.pyplot as plt

if __name__ == '__main__':
    y = load_airline()
    y_train, y_test = temporal_train_test_split(y)
    plot_ys(y_train, y_test, labels=["y_train", "y_test"])
    plt.show()
    sys.exit()
