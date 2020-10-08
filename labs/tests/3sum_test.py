import unittest

from labs.three_sum import ThreeElementsSum


class ThreeElementsBaseTestCase(unittest.TestCase):
    def compare_element_pairs(self, result, expected):
        """Common method for compare list of elements"""
        for res, exp in zip(result, expected):
            res.sort()
            exp.sort()
            self.assertListEqual(res, exp)


class ThreeElementsSumValidTestCase(ThreeElementsBaseTestCase):
    def test_valid_pairs(self):
        result = ThreeElementsSum([-1, 0, 1, 2, -1, -4]).find()
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.compare_element_pairs(result, expected)

    def test_valid_empty_list(self):
        result = ThreeElementsSum([0]).find()
        expected = []
        self.compare_element_pairs(result, expected)


class ThreeElementsSumInvalidTestCase(ThreeElementsBaseTestCase):
    def test_invalid_pairs(self):
        with self.assertRaises(ValueError):
            ThreeElementsSum([1, 34, 's'])

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            ThreeElementsSum('[1, 34, 1]')


if __name__ == '__main__':
    unittest.main()
