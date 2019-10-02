class Item:
    def __init__(self):
        self._x = 1

    def run(self):
        self._x = 2

    @property
    def x(self):
        return self._x


class CustomItem(Item):
    pass


class MockItem(Item):
    def run(self):
        self._x = 3


class Context(CustomItem, MockItem):
    pass


test = Context()
test.run()
print(test.x)
