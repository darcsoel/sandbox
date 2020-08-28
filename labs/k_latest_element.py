numbers = [1, 3, 4, 2]


def find_latest_k(numbers, latest):
    if not latest:
        raise ValueError('Wrong index value')

    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[latest - 1]


index = 1

print(find_latest_k(numbers, index))

numbers = [9, 3, 2, 4, 8]
index = 3

print(find_latest_k(numbers, index))
