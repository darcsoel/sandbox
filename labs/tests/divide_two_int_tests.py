import unittest

from labs.divide_two_integers import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().divide(10, 3), 3)

    def test_2(self):
        self.assertEqual(Solution().divide(7, -3), -2)

    def test_3(self):
        self.assertEqual(Solution().divide(0, 1), 0)

    def test_4(self):
        self.assertEqual(Solution().divide(-1, -1), 1)

    def test_5(self):
        self.assertEqual(Solution().divide(1, 2), 0)

    def test_6(self):
        self.assertEqual(Solution().divide(-2147483648, -1), 2147483647)


if __name__ == '__main__':
    unittest.main()
