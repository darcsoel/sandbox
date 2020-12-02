# import string
import sys


class PhoneLetters:
    empty_cells = (1,)
    bigger_cells = (7, 9)

    def __init__(self, number: [int, str]):
        if not isinstance(number, (int, str)):
            raise ValueError('number should be instance of int or str')

        self.cells = self._build_cells()
        self._phone_number = number

    def _build_cells(self):
        # chars = string.ascii_letters

        for number in range(10):
            pass


if __name__ == '__main__':
    sys.exit()
