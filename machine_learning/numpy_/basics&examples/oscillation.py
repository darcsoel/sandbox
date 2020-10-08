import sys
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)
    x3 = np.linspace(0.0, 5.0)

    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)
    y3 = np.cos(3 * np.pi * x1) * np.exp(-x1)

    plt.subplot(3, 1, 1)
    plt.plot(x1, y1, 'o-')
    plt.title('A tale of 3 subplots of oscillations')
    plt.ylabel('Damped')

    plt.subplot(3, 1, 2)
    plt.plot(x2, y2, '.-')
    plt.xlabel('time (s)')
    plt.ylabel('Undamped')

    plt.subplot(3, 1, 3)
    plt.plot(x3, y3, '.-')
    plt.xlabel('time (s)')
    plt.ylabel('Damped 2')

    plt.show()

    sys.exit()
