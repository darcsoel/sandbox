"""
Demo example of super() method usage
Nice feature for DI
"""

from sys import exit


class Base:
    """Some base class"""

    def __init__(self, number):
        self._number = number

    def retrieve(self):
        return f'Your number {self._number}'


class Reader(Base):
    """Standard realization"""

    def retrieve(self):
        return super().retrieve()


class ReaderMock(Base):
    """Make some mock"""

    def retrieve(self):
        return f'Your mocked number {self._number}'


class NewReader(Reader, ReaderMock):
    """Use mock on standard reader"""
    pass


if __name__ == '__main__':
    reader = Reader(1)
    new_reader = NewReader(1)

    print(reader.retrieve())
    print(new_reader.retrieve())

    help(new_reader)

    exit()
