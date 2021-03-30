import unittest

from labs.three_sum import Solution


class ThreeElementsBaseTestCase(unittest.TestCase):
    def compare_element_pairs(self, result, expected):
        """Common method for compare list of elements"""
        for res, exp in zip(result, expected):
            # res.sort()
            # exp.sort()
            self.assertListEqual(res, exp)


class ThreeElementsSumValidTestCase(ThreeElementsBaseTestCase):
    def test_valid_pairs(self):
        result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.compare_element_pairs(result, expected)

    def test_valid_empty_list(self):
        result = Solution().threeSum([0])
        expected = []
        self.compare_element_pairs(result, expected)


if __name__ == '__main__':
    unittest.main()
