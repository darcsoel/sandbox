def quick_sort(array):
    arr_len = len(array)

    if arr_len <= 1:
        return array

    pivot = array[0]
    less = [element for element in array[1:] if element <= pivot]
    more = [element for element in array[1:] if element > pivot]

    return quick_sort(less) + [pivot] + quick_sort(more)


q_array = [0, 5, 5, 35, 2, 65, 32, 4, 3, 23, 95, 50, 1, 45, 6]

print('Number of elements - \t{0}'.format(len(q_array)))
print('Non-sorted array - \t\t{0}'.format(q_array))
print('Sorted array - \t\t\t{0}'.format(quick_sort(q_array)))
