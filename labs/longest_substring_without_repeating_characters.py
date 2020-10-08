import sys

long_string = 'aabcabcbbaabcabcbb'


def find_longest_substr(string):
    """Search longest substring without char repetition"""

    results = []

    for index, _ in enumerate(string):
        result = []

        for char_index in range(index, len(string)):
            if string[char_index] in result:
                break
            else:
                result.append(string[char_index])

        results.append(result)

    stringify = []

    for r in results:
        stringify.append(''.join(r))

    return max(stringify, key=len)


if __name__ == '__main__':
    print(find_longest_substr(long_string))
    sys.exit()
