import unittest
from labs.string_to_int import str_to_int


class CorrectParamsTestCase(unittest.TestCase):
    def _check_number_valid(self, parsed, expected):
        return self.assertEqual(str_to_int(parsed), expected)

    def test_unsigned_int(self):
        self._check_number_valid('10', 10)

    def test_signed_int(self):
        self._check_number_valid('-10', -10)

    def test_unsigned_int_with_spaces(self):
        self._check_number_valid(' 10 ', 10)

    def test_signed_int_with_spaces(self):
        self._check_number_valid(' -10 ', -10)


class IncorrectParamsTestCase(unittest.TestCase):
    def test_number_with_chars(self):
        with self.assertRaises(ValueError):
            str_to_int("10a")

    def test_number_with_punctuation(self):
        with self.assertRaises(ValueError):
            str_to_int("#10")

    def test_number_with_dash(self):
        with self.assertRaises(ValueError):
            str_to_int("-10-")


if __name__ == '__main__':
    unittest.main()
