"""
Calculator should be based on generators/coroutines

"""


import re

expression_to_evaluate = '1 + 2 * 3 - 4'


class Parser:
    patterns = [
        r'P<PLUS>\+',
        r'P<MINUS>\-',
    ]

    def __init__(self, expression):
        self._expression = expression

    def parse(self):
        for k, v in re.Scanner([self._expression], re.MULTILINE | re.DOTALL):
            pass


parser = Parser(expression_to_evaluate)
parser.parse()
