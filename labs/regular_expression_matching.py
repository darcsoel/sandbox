"""Leet code issue

Given an input string (s) and a pattern (p), implement regular expression
matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

"""


class ComplexSolution:
    """
    Main parser class
    Still not stable, need fix
    """

    def __init__(self):
        self._pattern = self._matches_found = None
        self._search_index = 0
        self._match_char = '#'
        self._error_char = '$'
        self._zero_matches = []

    def _match_single_char(self, index, any_=False):
        try:
            char = self._matches_found[self._search_index]
        except IndexError:
            self._matches_found.append(self._error_char)
            return False

        if any_:
            matches = char.isalpha()
        else:
            matches = char == self._pattern[index]

        matches = self._match_char if matches else self._error_char
        self._matches_found[self._search_index] = matches
        self._search_index += 1
        return True

    def _match_zero_or_more_chars(self, index: int, limit=None):
        try:
            search = self._pattern[index + 1]
        except IndexError:
            return False

        found = 0

        while self._search_index < len(self._matches_found):
            if limit and found >= limit:
                break

            try:
                char = self._matches_found[self._search_index]
            except IndexError:
                return False

            if char == search or (search == '.' and char.isalpha()):
                self._matches_found[self._search_index] = self._match_char
                self._search_index += 1
                found += 1
            elif char != search:
                self._zero_matches.append(self._match_char)
                return False
            else:
                return False

        return True

    def isMatch(self, string_: str, pattern: str):
        """Check if entire string match pattern"""

        if string_.isalpha() and pattern.isalpha():
            return string_ == pattern

        result = []

        for zero_or_many_pattern_limit in list(range(10)) + [None]:
            self._pattern = pattern[::-1]
            self._matches_found = list(string_)
            self._matches_found.reverse()
            self._search_index = 0

            last_pattern = None

            for index, char in enumerate(self._pattern):
                if char == '*':
                    last_pattern = '*'
                    self._match_zero_or_more_chars(index,
                                                   zero_or_many_pattern_limit)
                else:
                    if last_pattern == '*':
                        last_pattern = None
                        continue
                    any_char = char == '.'
                    self._match_single_char(index, any_char)
                    last_pattern = None

            matches = [x == self._match_char for x in self._matches_found]
            result.append(all(matches))

        return any(result)


# perfect solution from leet code
class Solution:
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
