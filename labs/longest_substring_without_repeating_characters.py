import sys

long_string = 'aabcabcbbaabcabcbb'


def find_longest_substr(string):
    result = []

    for i in string:
        for j in range(i, len(string)):
            pass

    return result


if __name__ == '__main__':
    print(find_longest_substr(long_string))
    sys.exit()
