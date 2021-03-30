def prop_factory(prop):
    def getter(instance):
        return instance.__dict__[prop]

    def setter(instance, value):
        instance.__dict__[prop] = value

    return property(getter, setter)


class Foo:
    bar = prop_factory('bar')

    def __init__(self, bar):
        self.bar = bar


if __name__ == '__main__':
    x = Foo('test')
    print(x.bar)
