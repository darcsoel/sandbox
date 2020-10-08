import random
import sys
import tracemalloc

from pympler import asizeof

# import matplotlib.pyplot as plt
# import seaborn

if __name__ == '__main__':
    tracemalloc.start()

    list_long = [random.randint(1, x) for x in range(5, 500)]

    trace = tracemalloc.take_snapshot()

    tracemalloc.stop()

    print(asizeof.asizeof(list_long))

    sys.exit()
