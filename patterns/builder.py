import sys


class Director:
    def __init__(self, builder):
        self.builder = builder

    def build(self):
        self.builder.method1()
        self.builder.method2()
        return self

    def get_obj(self):
        return self.builder.obj


class Builder:
    def __init__(self):
        self.obj = {}

    def method1(self):
        self.obj['field1'] = 'value1'

    def method2(self):
        self.obj['field2'] = 'value2'


if __name__ == '__main__':
    builder = Builder()
    director = Director(builder)
    print(director.build().get_obj())
    sys.exit()
