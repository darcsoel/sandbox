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
