from array import array
from factory.CarFactory import CarFactory
import numpy as np


# system beep, don`t work on MAC
print("\a")

# userInput = []
# while True:
#     var = input('Enter a word\n')
#     if len(var) == 0:
#         break
#     else:
#         userInput.append(var)
#
# print('Yoy entered - {0}'.format(userInput))

firstArray = ['first', 'second', 'third']
print(firstArray)

firstArray.append('fourth')
print(firstArray)

firstArray.insert(0, 'fifth')
print(firstArray)

firstArray.sort()
print(firstArray)

print("\n")

firstArray.reverse()
print(firstArray)

secondArray = firstArray[:]

print('Array length = {0}'.format(len(firstArray)))

firstArray.remove('first')
print(firstArray)

del firstArray[0]
print(firstArray)

firstArray.pop()
print(firstArray)

print("\n\n")

for elem in secondArray:
    print('Elem - {0}'.format(elem.title()))
    print('Elem - {0}'.format(elem.upper()))
    print('Elem - {0}'.format(elem.lower()))

print("\n")

someVal = 'ten'
if someVal not in secondArray:
    print('Value \'{0}\' is not in array {1}'.format(someVal, secondArray))

firstStr = 'first'
if firstStr in secondArray:
    print('Value \'{0}\' is in {1}'.format(firstStr, secondArray))

print("\n")

for _ in range(1, 5):
    print("Hello")

print("\n")

for index in range(1, 5):
    print('Hello {0} : {1}'.format(index, index ** 2))

thirdArray = []
if thirdArray:
    print('Not empty array')
else:
    print('Empty array')

thirdArray.append('cat')
thirdArray.append('dog')
thirdArray.append('parrot')
thirdArray.append('dog')
thirdArray.append('dog')

print(thirdArray)

while 'dog' in thirdArray:
    thirdArray.remove('dog')

print(thirdArray)
print('\n\n')

firstArrayForMerge = ['some', 'val']
secondArrayForMerge = ['to', 'merge']

print(firstArrayForMerge + secondArrayForMerge)

print("\n\n")

firstDictionary = {}
print(firstDictionary)
firstDictionary['key1'] = 'val1'
firstDictionary['key2'] = 'val2'
firstDictionary['key3'] = 'val3'
print(firstDictionary)

# .items() .values() .keys() methods
for key, value in firstDictionary.items():
    print('Key - {0} : Value - {1}'.format(key, value))

a = 32
b = 7
print('Modular = {0}'.format(a % b))
print('OR = {0}'.format(a | b))
print('AND = {0}'.format(a & b))
print('XOR = {0}'.format(a ^ b))

strictArray = array('i', [1, 2, 3, 4])
print(strictArray)
strictArray.append(1)
print(strictArray)


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

list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3, 4]
list_3 = [1, 2, 3, 4]
list_4 = [1, 2, 3, 4]

for _, item in enumerate(list_1):
    del item

for _, item in enumerate(list_2):
    list_2.remove(item)

for _, item in enumerate(list_3[:]):
    list_3.remove(item)

for idx, item in enumerate(list_4):
    list_4.pop(idx)

print(list_1)
print(list_2)
print(list_3)
print(list_4)


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

long_array = np.array(range(1, 100, 2))

print(long_array)

