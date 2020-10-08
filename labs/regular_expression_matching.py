"""Leet code issue - self made regular expression matcher"""

import string
import sys


class RegEx:
    """Main parser class"""

    def __init__(self, search: str, target: str):
        self._reg_ex_patterns = {'.': self._match_any_single_char,
                                 '*': self._match_zero_or_more_chars}

        # true if move one step forward
        self._reg_ex_patterns_step_rule = {'.': False,
                                           '*': True}

        self._search = self._validate_search(search)
        self._target = self._validate_target(target)

    @staticmethod
    def _validate_search(search: str):
        if not isinstance(search, str):
            raise ValueError("Search must be string")

        if (search != search.lower()) or not search.isalpha():
            raise ValueError("Search must can contain only lowercase letters")

        return search

    def _validate_target(self, target: str):
        if not isinstance(target, str):
            raise ValueError("Target must be string")

        denied_chars = [x for x in string.punctuation
                        if x not in self._reg_ex_patterns.keys()]

        denied_chars.extend(string.digits)

        for char in denied_chars:
            if char in target:
                raise ValueError(f'Target must contain only '
                                 f'lowercase letters and'
                                 f' {self._reg_ex_patterns.keys()}')

        return target

    def _match_any_single_char(self, index: int):
        return True

    def _match_zero_or_more_chars(self, index: int):
        try:
            self._target[index - 1]
        except IndexError:
            raise ValueError("Wrong regex, matching `zero or more` symbol "
                             "could not be last")

        return True

    def match(self):
        """Check if entire string match pattern"""

        if self._search == self._target:
            return True

        # move backward on string, check next symbol after regex pattern
        # split search after each target regex found

        for index, char in enumerate(reversed(self._target)):
            if char in self._reg_ex_patterns:
                self._reg_ex_patterns[char](index)

                if self._reg_ex_patterns_step_rule[char]:
                    continue

        return False


if __name__ == '__main__':
    search_string = 'test'
    target_pattern = 't.'

    r = RegEx(search_string, target_pattern)

    print(r.match())

    sys.exit()
