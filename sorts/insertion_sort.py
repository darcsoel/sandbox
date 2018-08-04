def insertion_sort(array):
    for index in range(1, len(array)):
        while 0 < index and array[index] < array[index - 1]:
            array[index], array[index - 1] = array[index - 1], array[index]
            index -= 1

    return array


i_array = [1, 4, 82, 41, 32, 45, 2, 54, 12, 5, 34, 21, 78, 451, 65]

print('Count of elements = \t{0}'.format(len(i_array)))
print('Unsorted array - \t\t{0}'.format(i_array))
print('Sorted array - \t\t\t{0}'.format((insertion_sort(i_array))))
