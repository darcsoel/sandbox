"""
Write a program to find the n-th ugly number.
"""
import sys


def find_ugly_number_by_position_index(index):
    """
    Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
    """

    result = 0
    searched_index = 1

    while searched_index != index:
        result += 1

        if result % 2 == 0 or result % 3 == 0 or result % 5 == 0:
            searched_index += 1

    return result


if __name__ == '__main__':
    for i in [9, 10]:
        ugly = find_ugly_number_by_position_index(i)
        print(f'Input = {i}. Output = {ugly}')

    sys.exit()
