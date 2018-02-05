import numpy as np

x = np.arange(9)
print(x)
y = x.reshape([3, 3])
print(y)

z = x ** 2
print(z)

v = np.add.reduce(x)
print(v)

n = np.random.random_integers(0, 10, 10)
print(n)
sum_n = sum(n)
print(sum_n)
