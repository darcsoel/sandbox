class Solution:
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    def isValid(self, s: str) -> bool:
        while '{}' in s or '[]' in s or '()' in s:
            s = s.replace('{}', '').replace('()', '').replace('[]', '')

        return not bool(s)
