import random
from factory.CarFactory import CarFactory

a = 32
b = 7
print('Modular = {0}'.format(a % b))
print('OR = {0}'.format(a | b))
print('AND = {0}'.format(a & b))
print('XOR = {0}'.format(a ^ b))

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

print('\n\n')
