def merge_sort(array):
    if len(array) == 1:
        return array

    midpoint = len(array) // 2
    first = merge_sort(array[:midpoint])
    second = merge_sort(array[midpoint:])
    result = []

    while len(first) > 0 and len(second) > 0:
        if first[0] > second[0]:
            result.append(second[0])
            del second[0]
        else:
            result.append(first[0])
            del first[0]

    while len(first) > 0:
        result.append(first[0])
        del first[0]

    while len(second) > 0:
        result.append(second[0])
        del second[0]

    return result


m_array = [1, 4, 82, 41, 32, 45, 2, 54, 12, 5, 34, 21, 78, 451, 65]

print('Count of elements = \t{0}'.format(len(m_array)))
print('Unsorted array - \t\t{0}'.format(m_array))
print('Sorted array - \t\t\t{0}'.format((merge_sort(m_array))))
