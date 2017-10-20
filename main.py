from factory.CarFactory import CarFactory
import random

# system beep, don`t work on MAC
print("\a")

for _ in range(1, 5):
    print("Hello")

print("\n")

for index in range(1, 5):
    print('Hello {0} : {1}'.format(index, index ** 2))

a = 32
b = 7
print('Modular = {0}'.format(a % b))
print('OR = {0}'.format(a | b))
print('AND = {0}'.format(a & b))
print('XOR = {0}'.format(a ^ b))


def fibonacci(number):
    if number == 0 or number == 1:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


def fibonacci_numbers(limit):
    numbers = []
    for i in range(0, limit + 1):
        numbers.append(fibonacci(i))
    return numbers


fibonacciLimit = 9
print('Fibonacci of {0} = {1}'.format(fibonacciLimit, fibonacci(fibonacciLimit)))
print(f"Fibonacci {fibonacci(fibonacciLimit)}")
print('Fibonacci numbers = {0}'.format(fibonacci_numbers(fibonacciLimit)))


def mersenne(number):
    if number == 0 or number == 1:
        return number
    else:
        return 2 ** number - 1


def mersenne_numbers(limit):
    numbers = []
    for i in range(0, limit + 1):
        numbers.append(mersenne(i))
    return numbers


mersenneNumber = 7

print('Mersenne of {0} = {1}'.format(mersenneNumber, mersenne(mersenneNumber)))
print('Mersenne numbers = {0}'.format(mersenne_numbers(mersenneNumber)))

car = 'Audi'
print(CarFactory.create(car))


def to_upper_case(fn):
    def wrapped():
        return '<upper>' + fn() + '<upper/>'

    return wrapped()


@to_upper_case
def print_hello():
    return 'hello'


# text = print_hello()
# print(text)

numberToConvert = 12
print('Number to string -> {0}'.format(str(numberToConvert)))
print('Octal system -> {0}'.format(oct(numberToConvert)))
print('Hex octal system -> {0}'.format(hex(numberToConvert)))

someWord = 'someword'
firstVersion = someWord[:]
anagram = ''

while someWord:
    pos = random.randrange(len(someWord))
    anagram += someWord[pos]
    someWord = someWord[:pos] + someWord[pos + 1:]

del someWord

print('{0} -> {1}'.format(firstVersion, anagram))

generatedArray = [x for x in range(1, 100, 3)]
print(generatedArray)

generatedArray2 = [x for x in range(1, 100, 3) if x % 4 != 0]
print(generatedArray2)

dic = {'John': 1200, 'Paul': 1000, 'Jones': 1850, 'Dorothy': 950}
print("\n".join(["%s = %d" % (name, salary) for name, salary in dic.items()]))


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
    for fillslot in range(len(alist) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[position_of_max]:
                position_of_max = location

        temp = alist[fillslot]
        alist[fillslot] = alist[position_of_max]
        alist[position_of_max] = temp


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
list_for_merge_sort = alist[:]
selection_sort(alist)
print(alist)

print('------------------\n')


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


print(list_for_merge_sort)
print(merge_sort(list_for_merge_sort))
