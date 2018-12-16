from functools import reduce

array = [1, 3, 2, 4, 5, 3, 2, 4, 3, 1]

add_10 = list(map(lambda x: x + 10, array))
add_10_2 = [x + 10 for x in array]

print(array)
print(add_10)
print(add_10_2)

filter_odd = list(filter(lambda x: x % 2 == 0, array))
filter_odd_2 = [x for x in array if x % 2 == 0]

print(filter_odd)
print(filter_odd_2)

reduce_f = reduce(lambda x, y: x + y, array)
print(reduce_f)
