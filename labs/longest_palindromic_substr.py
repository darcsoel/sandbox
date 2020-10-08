import sys


def check_if_polindrome(chars: list):
    if len(chars) == 1:
        return chars

    median = int(round(len(chars) / 2))

    if len(chars) % 2 == 0:
        return False

    first = chars[:median + 1]
    second = reversed(chars[median:])

    for i, j in zip(first, second):
        if i != j:
            return False

    return True


def find_palindromic(long_string: str):
    results = []

    for char_index, _ in enumerate(long_string):
        result = []
        for index in range(char_index, len(long_string)):
            result.append(long_string[index])

            if check_if_polindrome(result):
                results.append(''.join(result))

    return max(results, key=len)


if __name__ == '__main__':
    palindromic_strings = ['babad', 'cbbd', 'a', 'ac']

    for s in palindromic_strings:
        print(s, ' is palindromic ', find_palindromic(s))

    sys.exit()
