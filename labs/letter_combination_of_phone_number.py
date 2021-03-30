from string import ascii_lowercase
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        default_length = 3
        large_length = 4
        large_numbers = (7, 9)
        letters = list(ascii_lowercase)
        numbers = {'1': [''], '0': [' ']}

        for i in range(2, 10):
            length = large_length if i in large_numbers else default_length
            numbers[f'{i}'] = letters[0:length]
            letters = letters[length:]

        res = []
        for d in digits:
            res.append(numbers[d])

        result = []
        while res:
            first = res.pop(0)
            if not result:
                result.extend(first)
            else:
                temp = []
                for r in result:
                    for f in first:
                        temp.append(f"{r}{f}")
                result = temp

        return result
