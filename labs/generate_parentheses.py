class Solution:
    def __init__(self):
        self._generated = []
        self._result = []

    def generate(self, n):
        if len(self._generated) == 2 * n:
            if self.valid():
                self._result.append("".join(self._generated))
        else:
            self._generated.append('(')
            self.generate(n)
            self._generated.pop()
            self._generated.append(')')
            self.generate(n)
            self._generated.pop()

    def valid(self):
        bal = 0
        for c in self._generated:
            if c == '(':
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False

        return not bal

    def generateParenthesis(self, n):
        self.generate(n)
        return self._result
