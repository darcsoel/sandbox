"""Leet code task"""

import sys
from collections import OrderedDict


class IntegerToRoman:
    """Take integer and convert to roman system"""

    number_compatibility_multiplexer = 1

    def __init__(self, number: int):
        if not isinstance(number, int):
            raise ValueError('Wrong input parameter')

        self.roman_numbers = OrderedDict({1: 'I',
                                          4: 'IV',
                                          5: 'V',
                                          9: 'IX',
                                          10: 'X',
                                          40: 'XL',
                                          50: 'L',
                                          90: 'XC',
                                          100: 'C',
                                          400: 'CD',
                                          500: 'D',
                                          900: 'CM',
                                          1000: 'M'})
        self._number = number
        self._roman_number = []

    def convert(self):
        """
        convert integer number to roman variation
        save list representation to instance
        """

        while self._number:
            integer, roman = self.roman_numbers.popitem()

            if self._number / integer < self.number_compatibility_multiplexer:
                continue

            self._roman_number.extend([roman] * (self._number // integer))
            self._number -= (integer * (self._number // integer))

        return ''.join(self._roman_number)


if __name__ == '__main__':
    # converter = IntegerToRoman(34)
    converter = IntegerToRoman(90)
    converter.convert()
    sys.exit()
