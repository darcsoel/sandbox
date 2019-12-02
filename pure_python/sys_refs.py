import sys

x = 13132


def foo(x):
    y = x
    return y


print(sys.getrefcount(x))
foo(x)
print(sys.getrefcount(x))
z = x
print(sys.getrefcount(x))
exit()
