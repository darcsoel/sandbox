import numpy as np
import pickle, shelve

for _ in range(1, 5):
    print("Hello")

print("\n")

for index in range(1, 5):
    print('Hello {0} : {1}'.format(index, index ** 2))

userInput = []
# while True:
    # var = input('Enter a word\n')
    # if len(var) == 0:
    #     break
    # else:
    #     userInput.append(var)

print('Yoy entered - {0}'.format(userInput))

print('\n')

long_array = np.array(range(1, 100, 2))

print(long_array)

print('\n')

third_array = []
if third_array:
    print('Not empty array')
else:
    print('Empty array')

third_array.append('cat')
third_array.append('dog')
third_array.append('parrot')
third_array.append('dog')
third_array.append('dog')
third_array.extend(['dog2', 'cat2', 'some3'])

print(third_array)

while 'dog' in third_array:
    third_array.remove('dog')

print(third_array)
print('\n\n')

first_array_for_merge = ['some', 'val']
second_array_for_merge = ['to', 'merge']

print(first_array_for_merge + second_array_for_merge)

print("\n\n")

first_dictionary = {}
print(first_dictionary)
first_dictionary['key1'] = 'val1'
first_dictionary['key2'] = 'val2'
first_dictionary['key3'] = 'val3'
print(first_dictionary)

# .items() .values() .keys() methods
for key, value in first_dictionary.items():
    print('Key - {0} : Value - {1}'.format(key, value))

flip_revert_dictionary = {value: key for key, value in first_dictionary.items()}

for key, value in flip_revert_dictionary.items():
    print('Key - {0} : Value - {1}'.format(key, value))


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

generatedArray = [x for x in range(1, 100, 3)]
print(generatedArray)

generatedArray2 = [x for x in range(1, 100, 3) if x % 4 != 0]
print(generatedArray2)

dic = {'John': 1200, 'Paul': 1000, 'Jones': 1850, 'Dorothy': 950}
print("\n".join(["%s = %d" % (name, salary) for name, salary in dic.items()]))

someFile = open('arrayReadline.txt', 'r')
# read() - read file as one line
# readline() - read one line
# readlines() - read all file as list of lines
# write() - write line to file
# writelines() - wrine list of lines to array
lines = someFile.readlines()
print(lines)
someFile.close()
print('\n')

someDumpFile = open('dumpFile.txt', 'wb')
pickle.dump(lines, someDumpFile)
someDumpFile.close()
readDumpFile = open('dumpFile.txt', 'rb')
print('Loaded binary files\n')
print(pickle.load(readDumpFile))
readDumpFile.close()

# someDumpFile = shelve.open('dumpFile.txt')
# someDumpFile[] = ['dfsfdsf', 'dasdasd', 'qeqqeqqe']
# someDumpFile.sync()
# someDumpFile.close()
