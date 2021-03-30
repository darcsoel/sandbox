"""TDD"""

import unittest

from labs.longest_common_prefix import Solution


class LongestCommonPrefixTestCase(unittest.TestCase):
    def test_with_existing_prefix(self):
        self.assertEqual(
            Solution().longestCommonPrefix(["flower", "flow", "flight"]), 'fl')

    def test_without_existing_prefix(self):
        self.assertEqual(Solution().longestCommonPrefix(["sea", "flight"]), '')

    def test_with_empty_data(self):
        self.assertEqual(Solution().longestCommonPrefix([]), '')


if __name__ == '__main__':
    unittest.main()
