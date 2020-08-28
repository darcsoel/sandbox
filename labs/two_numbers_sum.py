"""Add two numbers with bin operators"""

import sys

first = 2
second = 2


def summarize(x, y):
    """Use binary operators instead arithmetic"""

    while y:
        carry = x & y
        x = x ^ y
        y = carry << 1

    return x


print(summarize(first, second))
print(first, second)

sys.exit()
