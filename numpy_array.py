import numpy as np

x = np.arange(9)
print(x)
y = x.reshape([3, 3])
print(y)

z = x ** 2
print(z)

v = np.add.reduce(x)
print(v)

print("\n")
n = np.random.random_integers(0, 10, 10)
print(n)
sum_n = np.sum(n)
print(sum_n)
print(np.max(n))
print(np.min(n))
print(np.average(n))

print("\n")
first = np.arange(1, 4)
second = np.arange(4, 7)

res = np.multiply.outer(first, second)
print(first)
print(second)
print(res)
