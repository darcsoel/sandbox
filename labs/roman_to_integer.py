"""Leet code task"""

import sys
from collections import OrderedDict


class RomanToInteger:
    """Take integer and convert to decimal system"""

    roman_numbers = OrderedDict({'M': 1000,
                                 'CM': 900,
                                 'D': 500,
                                 'CD': 400,
                                 'C': 100,
                                 'XC': 90,
                                 'L': 50,
                                 'XL': 40,
                                 'X': 10,
                                 'IX': 9,
                                 'V': 5,
                                 'IV': 4,
                                 'I': 1})

    def __init__(self, number: str):
        if not isinstance(number, str):
            raise ValueError('Wrong input parameter')

        self._number = 0
        self._roman_number = number

    def convert(self):
        """
        convert integer number to roman variation
        save list representation to instance
        """

        for roman, integer in self.roman_numbers.items():
            while True:
                try:
                    index = self._roman_number.index(roman)
                    if index != 0:
                        break
                except ValueError:
                    break

                self._number += integer
                self._roman_number = self._roman_number[len(roman):]

        return self._number


if __name__ == '__main__':
    converter = RomanToInteger('IX')
    converter.convert()
    sys.exit()
