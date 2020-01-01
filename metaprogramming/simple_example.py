class CustomMeta(type):
    """Make all attributes in uppercase"""

    def __new__(mcs, name, bases, attrs):

        attrs = ((name, value) for name, value in attrs.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)

        return type.__new__(name, bases, uppercase_attr)


class CustomClass(metaclass=CustomMeta):
    pass
