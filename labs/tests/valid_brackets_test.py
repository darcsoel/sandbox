import unittest

from labs.valid_brackets import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertTrue(Solution().isValid('()'))

    def test_2(self):
        self.assertTrue(Solution().isValid('{[]}'))

    def test_3(self):
        self.assertTrue(Solution().isValid('()[]{}'))

    def test_4(self):
        self.assertFalse(Solution().isValid('([)]'))

    def test_5(self):
        self.assertFalse(Solution().isValid('(]'))

    def test_6(self):
        self.assertFalse(Solution().isValid("(){}}{"))


if __name__ == '__main__':
    unittest.main()
