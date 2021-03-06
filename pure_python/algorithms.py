def _fibonacci(number):
    if number == 0 or number == 1:
        return number
    else:
        return _fibonacci(number - 1) + _fibonacci(number - 2)


def fibonacci(limit):
    numbers = []
    for i in range(0, limit + 1):
        numbers.append(_fibonacci(i))
    return numbers


fibonacci_limit = 9
print('Fibonacci of {} = {}'.format(fibonacci_limit, _fibonacci(fibonacci_limit)))


def fibonacci_simple(num: int) -> int:
    a, b = 0, 1
    for i in range(num):
        a, b = b, a + b

    return a


fib_sim = fibonacci_simple(fibonacci_limit)
print(f'Fibonacci of {fibonacci_limit} = {fib_sim}')


def _mersenne(number):
    if number == 0 or number == 1:
        return number
    else:
        return 2 ** number - 1


def mersenne(limit):
    numbers = []
    for i in range(0, limit + 1):
        numbers.append(_mersenne(i))
    return numbers


mersenne_number = 7

print('Mersenne of {0} = {1}'.format(mersenne_number, _mersenne(mersenne_number)))
print('Mersenne numbers = {0}'.format(mersenne(mersenne_number)))


def greatest_common_divisor(first, second):
    """Calculate greatest common divisor"""
    while first != 0:
        first, second = second % first, first
    return second


def least_common_multiple(first, second):
    """Calculate least common multiple with GCD"""
    return int(first / greatest_common_divisor(first, second) * second)


print(greatest_common_divisor.__doc__)
print(greatest_common_divisor(54, 24))
print(least_common_multiple.__doc__)
print(least_common_multiple(840, 396))


def selection_sort(alist):
    for slot in range(len(alist) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, slot + 1):
            if alist[location] > alist[position_of_max]:
                position_of_max = location

        temp = alist[slot]
        alist[slot] = alist[position_of_max]
        alist[position_of_max] = temp


print('\n\n')

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
list_for_merge_sort = alist[:]
print(list_for_merge_sort)
selection_sort(alist)
print(alist)


def merge(a, b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


def merge_sort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = int(len(x) / 2)
        a = merge_sort(x[:middle])
        b = merge_sort(x[middle:])
        return merge(a, b)


print('\n\n')

print(list_for_merge_sort)
print(merge_sort(list_for_merge_sort))
