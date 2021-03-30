import unittest

from labs.four_sum import Solution


class FourElementsBaseTestCase(unittest.TestCase):
    def compare_element_pairs(self, result, expected):
        """Common method for compare list of elements"""
        for res, exp in zip(result, expected):
            res.sort()
            exp.sort()
            self.assertListEqual(res, exp)


class FourElementsSumValidTestCase(FourElementsBaseTestCase):
    def test_1(self):
        result = Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
        expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        self.compare_element_pairs(result, expected)

    def test_2(self):
        result = Solution().fourSum([2, 2, 2, 2, 2], 0)
        expected = [[2, 2, 2, 2]]
        self.compare_element_pairs(result, expected)


if __name__ == '__main__':
    unittest.main()
