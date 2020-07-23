class Base:
    def __init__(self, number):
        self._number = number

    def retrieve(self):
        return f'Your number {self._number}'

