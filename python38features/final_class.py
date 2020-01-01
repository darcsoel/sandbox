from typing import final


@final
class Bar:
    def __init__(self, val):
        self._val = val

    @final
    def prettify(self):
        return f'Value {self._val}'


class Foo(Bar):
    def prettify(self):
        return f'Overridden {self._val}'


x = Bar('hello')
print(x.prettify())

y = Foo('hello')
print(y.prettify())
