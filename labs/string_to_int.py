import sys


def str_to_int(number: str):
    """Convert string-like number to integer"""

    if not isinstance(number, str):
        raise ValueError("Wrong parameter, must be string")

    number = number.replace(' ', '')

    if number.startswith('-'):
        signed = True
        number = number.replace('-', '', 1)
    else:
        signed = False

    if not number.isnumeric():
        raise ValueError("Wrong symbols passed")

    result = 0
    zero_code = ord('0')

    for index, symbol in enumerate(number, 1):
        result += (ord(symbol) - zero_code) * 10 ** (len(number) - index)

    return result if not signed else -result


if __name__ == '__main__':
    numbers = ('  10', '-14', '2')

    for num in numbers:
        print(str_to_int(num))

    sys.exit()
