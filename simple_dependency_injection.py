class Item:
    def __init__(self):
        self.x = 1

    def run(self):
        self.x = 2


class CustomItem(Item):
    pass


class MockItem(Item):
    def run(self):
        self.x = 3


class Context(CustomItem, MockItem):
    pass


test = Context()
test.run()
print(test.x)
