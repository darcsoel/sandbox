import unittest

from labs.letter_combination_of_phone_number import Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        digits = "23"
        result = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(Solution().letterCombinations(digits), result)

    def test_2(self):
        digits = "5678"
        result = ["jmpt", "jmpu", "jmpv", "jmqt", "jmqu", "jmqv", "jmrt",
                  "jmru", "jmrv", "jmst", "jmsu", "jmsv", "jnpt", "jnpu",
                  "jnpv", "jnqt", "jnqu", "jnqv", "jnrt", "jnru", "jnrv",
                  "jnst", "jnsu", "jnsv", "jopt", "jopu", "jopv", "joqt",
                  "joqu", "joqv", "jort", "joru", "jorv", "jost", "josu",
                  "josv", "kmpt", "kmpu", "kmpv", "kmqt", "kmqu", "kmqv",
                  "kmrt", "kmru", "kmrv", "kmst", "kmsu", "kmsv", "knpt",
                  "knpu", "knpv", "knqt", "knqu", "knqv", "knrt", "knru",
                  "knrv", "knst", "knsu", "knsv", "kopt", "kopu", "kopv",
                  "koqt", "koqu", "koqv", "kort", "koru", "korv", "kost",
                  "kosu", "kosv", "lmpt", "lmpu", "lmpv", "lmqt", "lmqu",
                  "lmqv", "lmrt", "lmru", "lmrv", "lmst", "lmsu", "lmsv",
                  "lnpt", "lnpu", "lnpv", "lnqt", "lnqu", "lnqv", "lnrt",
                  "lnru", "lnrv", "lnst", "lnsu", "lnsv", "lopt", "lopu",
                  "lopv", "loqt", "loqu", "loqv", "lort", "loru", "lorv",
                  "lost", "losu", "losv"]
        self.assertEqual(Solution().letterCombinations(digits), result)


if __name__ == '__main__':
    unittest.main()
