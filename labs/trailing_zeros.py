import random
import sys
from functools import reduce
from operator import mul


def fact(num: int) -> int:
    return reduce(mul, range(1, num + 1))


def correct_result(number):
    number = fact(number)
    return str(number).count('0')


def trailing_zeros(number):
    return correct_result(number) == number


if __name__ == '__main__':
    numbers_to_compare = [5] + random.sample(range(2, 100), 15)

    for n in numbers_to_compare:
        correct = correct_result(n)
        result = trailing_zeros(n)
        print(f'Number {n} giving {result}. Count is {correct}')

    print('Done')
    sys.exit()
