"""TDD"""

import unittest

from labs.longest_common_prefix import prefix_search


class LongestCommonPrefixTestCase(unittest.TestCase):
    def test_with_existing_prefix(self):
        self.assertEqual(prefix_search(["flower", "flow", "flight"]), 'fl')

    def test_without_existing_prefix(self):
        self.assertEqual(prefix_search(["sea", "flight"]), '')

    def test_with_empty_data(self):
        self.assertEqual(prefix_search([]), '')


class LongestCommonPrefixInvalidTestCase(unittest.TestCase):
    def test_with_str_numbers(self):
        with self.assertRaises(ValueError):
            prefix_search(["flower", "f1231low"])

    def test_with_numbers(self):
        with self.assertRaises(ValueError):
            prefix_search(["flower", 123])

    def test_with_uppercase(self):
        with self.assertRaises(ValueError):
            prefix_search(["Flower", "flight"])


if __name__ == '__main__':
    unittest.main()
