import unittest

from labs.three_sum_closest import ThreeElementsSumClosest


class ThreeElementsSumValidTestCase(unittest.TestCase):
    def test_valid_pairs(self):
        result = ThreeElementsSumClosest([-1, 2, 1, -4], 1).find()
        self.assertEqual(result, 2)

    def test_valid_pairs_pass_target_in_method(self):
        result = ThreeElementsSumClosest([-1, 2, 1, -4]).find(1)
        self.assertEqual(result, 2)


class ThreeElementsSumInvalidTestCase(unittest.TestCase):
    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            ThreeElementsSumClosest([1, 34, 's'], 1).find()

    def test_too_short_list(self):
        with self.assertRaises(ValueError):
            ThreeElementsSumClosest([1, 34], 1).find()


if __name__ == '__main__':
    unittest.main()
