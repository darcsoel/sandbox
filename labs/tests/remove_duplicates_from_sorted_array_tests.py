import unittest

from labs.remove_duplicates_from_sorted_array import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        original = [1, 1, 2]
        self.assertEqual(Solution().removeDuplicates(original), 2)

    def test_2(self):
        original = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        self.assertEqual(Solution().removeDuplicates(original), 5)

    def test_3(self):
        original = [1, 1]
        self.assertEqual(Solution().removeDuplicates(original), 1)


if __name__ == '__main__':
    unittest.main()
