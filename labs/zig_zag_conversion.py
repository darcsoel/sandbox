import sys


def convert(string_to_convert: str, row_num: int):
    if not isinstance(string_to_convert, str):
        raise ValueError("First param must be string")

    if not isinstance(row_num, int):
        raise ValueError("Second param must be int")

    i_len = round(len(string_to_convert) / row_num) + row_num - 1
    matrix = [['' for _ in range(row_num)] for _ in range(i_len)]
    i_index, j_index = 0, 0
    go_up = True

    for i in string_to_convert:
        matrix[i_index][j_index] = i

        if go_up:
            j_index += 1
        else:
            i_index += 1
            j_index -= 1

        if j_index == row_num - 1:
            go_up = False
        elif j_index == 0:
            go_up = True

    matrix = [[matrix[j][i] for j in range(len(matrix))]
              for i in range(len(matrix[0]))]

    matrix = [''.join(x) for x in matrix]

    return ''.join(j for j in matrix)


if __name__ == '__main__':
    string_to_convert = 'PAYPALISHIRING'
    print(convert(string_to_convert, 3))
    sys.exit()
