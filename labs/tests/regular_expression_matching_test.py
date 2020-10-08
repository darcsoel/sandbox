import unittest
from labs.regular_expression_matching import RegEx


class CorrectRegExSearchTestCase(unittest.TestCase):
    def test_single_character(self):
        self.assertEqual(True, RegEx('test', 't.').match())

    def test_zero_or_more_character(self):
        self.assertEqual(True, RegEx('test', 't*').match())

    def test_mixed_pattern_case(self):
        self.assertEqual(True, RegEx('test', 't*.').match())

    def test_non_pattern_string(self):
        self.assertEqual(True, RegEx('test', 'test').match())


class IncorrectRegExSearchTestCase(unittest.TestCase):
    def test_non_pattern_string(self):
        self.assertEqual(False, RegEx('test', 't').match())

    def test_search_str_with_num(self):
        with self.assertRaises(ValueError):
            RegEx("sdfdsfs3", 'fsdf*')

    def test_search_str_with_uppercase(self):
        with self.assertRaises(ValueError):
            RegEx("sdfdsSDFSW", 'fsdf*')

    def test_target_str_with_num(self):
        with self.assertRaises(ValueError):
            RegEx("sdfds", 'fsdf123')

    def test_target_str_with_wrong_pattern(self):
        with self.assertRaises(ValueError):
            RegEx("sdfds", 'fsdf*$%')


if __name__ == '__main__':
    unittest.main()
