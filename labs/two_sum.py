import sys


def add_two(int_list, target):
    """Brute force all elements to find solution"""

    if len(int_list) != len(set(int_list)):
        raise ValueError("List contain duplicates")

    for i_i, i in enumerate(int_list):
        for i_j, j in enumerate(int_list):
            if i_i == i_j:
                continue

            if i + j == target:
                return [i_i, i_j]


if __name__ == '__main__':
    some_integers = [1, 4, 6, 3, 9]
    result = 7

    print(add_two(some_integers, result))

    sys.exit()
