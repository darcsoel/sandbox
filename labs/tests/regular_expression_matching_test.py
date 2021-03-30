import unittest

from labs.regular_expression_matching import Solution


class CorrectRegExSearchTestCase(unittest.TestCase):
    def test_single_character(self):
        self.assertTrue(Solution().isMatch('t', '.'))

    def test_zero_or_more_character(self):
        self.assertTrue(Solution().isMatch('tt', 't*'))

    def test_zero_or_more_character2(self):
        self.assertTrue(Solution().isMatch('aaa', 'a*a'))

    def test_mixed_pattern_case(self):
        self.assertTrue(Solution().isMatch('ab', '.*'))

    def test_mixed_pattern_case2(self):
        self.assertTrue(Solution().isMatch('aaa', 'a.a'))

    def test_zero_or_more_complex_pattern_case(self):
        self.assertTrue(Solution().isMatch('aab', 'c*a*b'))

    def test_zero_or_more_complex_pattern_case2(self):
        self.assertTrue(Solution().isMatch('mississippi', 'mis*is*ip*.'))

    def test_zero_or_more_complex_pattern_case3(self):
        self.assertTrue(Solution().isMatch('bbbba', '.*a*a'))

    def test_zero_or_more_complex_pattern_case4(self):
        self.assertTrue(Solution().isMatch("aaa", "ab*ac*a"))

    def test_zero_or_more_complex_pattern_case5(self):
        self.assertTrue(Solution().isMatch("aaa", "ab*a*c*a"))

    def test_zero_or_more_complex_pattern_case6(self):
        self.assertTrue(Solution().isMatch("aasdfasdfasdfasdfas",
                                           "aasdf.*asdf.*asdf.*asdf.*s"))

    def test_non_pattern_string(self):
        self.assertTrue(Solution().isMatch('test', 'test'))


class IncorrectRegExSearchTestCase(unittest.TestCase):
    def test_non_pattern_string(self):
        self.assertFalse(Solution().isMatch('mississippi', 'mis*is*p*.'))

    def test_single_character_without_mask(self):
        self.assertFalse(Solution().isMatch('aa', 'a'))

    def test_single_character_without_mask2(self):
        self.assertFalse(Solution().isMatch('aaa', 'aaaa'))

    def test_mixed_pattern_case2(self):
        self.assertFalse(Solution().isMatch('ab', '.*c'))

    def test_zero_or_more_complex_pattern(self):
        self.assertFalse(Solution().isMatch("aaa", "ab*a"))


if __name__ == '__main__':
    unittest.main()
