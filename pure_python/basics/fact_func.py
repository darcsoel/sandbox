from functools import reduce
from operator import mul


def fact(num: int) -> int:
    return reduce(mul, range(1, num + 1))


print(fact(1))
print(fact(4))
