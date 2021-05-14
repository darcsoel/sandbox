class Foo:
    def __init__(self, *args, some_arg, **kwargs):
        self.arg = some_arg


x = Foo(1, 2, 3, some_arg='asdfsdf')
print(x.__dict__)


class Bar:
    def __init__(self, *args, some_arg=None):
        self.arg = some_arg


y = Bar()
print(y.__dict__)
