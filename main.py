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

userInput = []
while(True):
    var = input('Enter a word\n')
    if len(var) == 0:
        break
    else:
        userInput.append(var)

print('Yoy entered - {0}'.format(userInput))
