"""TDD"""

import unittest

from labs.integer_to_roman import IntegerToRoman


class IntegerToRomanCorrectTestCase(unittest.TestCase):
    def test_3_number(self):
        self.assertEqual(IntegerToRoman(3).convert(), 'III')

    def test_4_number(self):
        self.assertEqual(IntegerToRoman(4).convert(), 'IV')

    def test_5_number(self):
        self.assertEqual(IntegerToRoman(5).convert(), 'V')

    def test_7_number(self):
        self.assertEqual(IntegerToRoman(7).convert(), 'VII')

    def test_8_number(self):
        self.assertEqual(IntegerToRoman(8).convert(), 'VIII')

    def test_9_number(self):
        self.assertEqual(IntegerToRoman(9).convert(), 'IX')

    def test_58_number(self):
        self.assertEqual(IntegerToRoman(58).convert(), 'LVIII')

    def test_90_number(self):
        self.assertEqual(IntegerToRoman(90).convert(), 'XC')

    def test_94_number(self):
        self.assertEqual(IntegerToRoman(94).convert(), 'XCIV')

    def test_1994_number(self):
        self.assertEqual(IntegerToRoman(1994).convert(), 'MCMXCIV')


if __name__ == '__main__':
    unittest.main()
