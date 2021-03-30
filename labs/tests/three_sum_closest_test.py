import unittest

from labs.three_sum_closest import Solution


class ThreeElementsSumValidTestCase(unittest.TestCase):
    def test_valid_pairs(self):
        result = Solution().threeSumClosest([-1, 2, 1, -4], 1)
        self.assertEqual(result, 2)

    def test_little_batch(self):
        numbers = [0, 1, 2]
        self.assertEqual(Solution().threeSumClosest(numbers, 0), 3)

    def test_little4_batch(self):
        numbers = [1, 1, 1, 1]
        self.assertEqual(Solution().threeSumClosest(numbers, -100), 3)

    def test_4(self):
        numbers = [0, 2, 1, -3]
        self.assertEqual(Solution().threeSumClosest(numbers, 1), 0)

    def test_5(self):
        numbers = [1, 1, 1, 0]
        self.assertEqual(Solution().threeSumClosest(numbers, -100), 2)


if __name__ == '__main__':
    unittest.main()
