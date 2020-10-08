import sys


def reverse_int(number: int):
    if not isinstance(number, int):
        raise ValueError('Wrong data! Must be integer')

    reversed = 0
    result = []
    signed = True if number >= 0 else False
    decimal_count = 1 if number > 0 else 0
    number = abs(number)

    while number:
        if number // 10:
            decimal_count += 1
            result.append(number % 10)
            number = int(number // 10)
        else:
            result.append(number % 10)
            break

    for index, n in enumerate(result):
        reversed += n * 10 ** (len(result) - index - 1)

    return reversed if signed else -reversed


if __name__ == '__main__':
    nums_to_reverse = [1, 123, -123, 120, 0]

    for num in nums_to_reverse:
        print(num, ' reversed ', reverse_int(num))

    sys.exit()
