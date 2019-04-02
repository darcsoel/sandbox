from array import array
from random import randint

if __name__ == '__main__':
    numbers = array('b', [randint(1, 5) for _ in range(0, 10)])
    print(numbers)
