import unittest

from labs.container_with_most_water import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        check = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
        self.assertEqual(check, 49)

    def test_2(self):
        check = Solution().maxArea([1, 1])
        self.assertEqual(check, 1)

    def test_3(self):
        check = Solution().maxArea([4, 3, 2, 1, 4])
        self.assertEqual(check, 16)

    def test_4(self):
        check = Solution().maxArea([1, 2, 1])
        self.assertEqual(check, 2)

    def test_5(self):
        check = Solution().maxArea([2, 3, 10, 5, 7, 8, 9])
        self.assertEqual(check, 36)

    def test_6(self):
        check = Solution().maxArea([2, 3, 4, 5, 18, 17, 6])
        self.assertEqual(check, 17)

    def test_7(self):
        check = Solution().maxArea([1, 2, 3, 4, 5, 25, 24, 3, 4])
        self.assertEqual(check, 24)

    def test_8(self):
        check = Solution().maxArea([1, 3, 2, 5, 25, 24, 5])
        self.assertEqual(check, 24)


if __name__ == '__main__':
    unittest.main()
