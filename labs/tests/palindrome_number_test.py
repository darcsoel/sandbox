import unittest
from labs.palindrome_number import check_if_palindrome


class CorrectPalindromeNumberTestCase(unittest.TestCase):
    def test_integer_unsigned(self):
        self.assertTrue(check_if_palindrome(121))


class IncorrectPalindromeNumberTestCase(unittest.TestCase):
    def test_integer_not_palindrome(self):
        self.assertFalse(check_if_palindrome(123))

    def test_string_value(self):
        with self.assertRaises(ValueError):
            check_if_palindrome('Test')

    def test_list_value(self):
        with self.assertRaises(ValueError):
            check_if_palindrome([1, 2, 1])


if __name__ == '__main__':
    unittest.main()
