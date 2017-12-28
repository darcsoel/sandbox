import numpy as np

array1 = np.random.randint(10, size=6)  # generate random array
array2 = np.random.randint(10, size=(6, 6))
array3 = np.random.randint(10, size=(6, 6, 6))

print(array1)
print("\n")
print(array2)
print("\n-----------------#############----------")
print(array3)

zero_array = np.zeros(10, dtype='int16')  # default - float

print("\nZero`s array")
print(zero_array)
