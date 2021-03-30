import unittest

from labs.generate_parentheses import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        result = Solution().generateParenthesis(2)
        check = ["(())", "()()"]
        self.assertEqual(result, check)

    def test_2(self):
        result = Solution().generateParenthesis(3)
        check = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertEqual(result, check)


if __name__ == '__main__':
    unittest.main()
