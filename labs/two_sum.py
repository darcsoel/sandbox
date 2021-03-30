import sys


def add_two(int_list, target):
    """Brute force all elements to find solution"""
    for index, value in enumerate(int_list):
        check = target - value
        try:
            second = int_list.index(check, index + 1)
        except IndexError:
            continue
        except ValueError:
            continue
        return [index, second]


if __name__ == '__main__':
    some_integers = [3, 2, 4]
    result = 6

    print(add_two(some_integers, result))

    sys.exit()
