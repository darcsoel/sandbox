"""TDD"""

import unittest

from labs.roman_to_integer import RomanToInteger


class IntegerToRomanCorrectTestCase(unittest.TestCase):
    def test_3_number(self):
        self.assertEqual(RomanToInteger('III').convert(), 3)

    def test_4_number(self):
        self.assertEqual(RomanToInteger('IV').convert(), 4)

    def test_5_number(self):
        self.assertEqual(RomanToInteger('V').convert(), 5)

    def test_7_number(self):
        self.assertEqual(RomanToInteger('VII').convert(), 7)

    def test_8_number(self):
        self.assertEqual(RomanToInteger('VIII').convert(), 8)

    def test_9_number(self):
        self.assertEqual(RomanToInteger('IX').convert(), 9)

    def test_27_number(self):
        self.assertEqual(RomanToInteger('XXVII').convert(), 27)

    def test_58_number(self):
        self.assertEqual(RomanToInteger('LVIII').convert(), 58)

    def test_90_number(self):
        self.assertEqual(RomanToInteger('XC').convert(), 90)

    def test_94_number(self):
        self.assertEqual(RomanToInteger('XCIV').convert(), 94)

    def test_1994_number(self):
        self.assertEqual(RomanToInteger('MCMXCIV').convert(), 1994)


if __name__ == '__main__':
    unittest.main()
