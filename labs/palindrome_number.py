import sys


def check_if_palindrome(number: int):
    if not isinstance(number, int):
        raise ValueError('Wrong parameter, must be integer')

    if number < 0:
        return False

    temp = number
    rev = 0

    while number > 0:
        dig = number % 10
        rev = rev * 10 + dig
        number //= 10

    return temp == rev


if __name__ == '__main__':
    check_if_palindrome(123)
    sys.exit()
