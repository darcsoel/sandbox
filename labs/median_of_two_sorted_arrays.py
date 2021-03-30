import sys


def median(first: list, second: list):
    first.sort()
    second.sort()

    result = first + second
    result.sort()

    summary_length = len(result)

    if summary_length % 2 == 0:
        first_elem = result[int(summary_length / 2)-1]
        second_elem = result[round(summary_length / 2)]
        return (first_elem + second_elem) / 2
    else:
        return result[int(summary_length / 2)]


if __name__ == '__main__':
    first_list = [1, 3]
    second_list = [2]

    third_list = [1, 2]
    forth_list = [3, 4]

    print(median(first_list, second_list))

    print(median(third_list, forth_list))

    sys.exit()
