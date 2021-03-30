from functools import reduce
from operator import mul
from typing import List


class Solution:
    def __init__(self):
        self.result = []

    @classmethod
    def factorial(cls, n):
        return reduce(mul, range(1, n + 1))

    @classmethod
    def calculate_max_combinations(cls, n):
        return cls.factorial(2) / (cls.factorial(n - 2) * cls.factorial(2))

    def generateParenthesis(self, n: int) -> List[str]:
        # max_combination = self.calculate_max_combinations(n)

        return []
