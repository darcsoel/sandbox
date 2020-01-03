class FinalMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)

        for class_ in bases:
            if issubclass(cls, class_):
                raise TypeError(str(class_.__name__) + " is final")


class Inherited(metaclass=FinalMeta):
    def __init__(self, msg):
        self._msg = msg

    def say_hello(self):
        return f'Hello {self._msg}'


# class InheritedMore(Inherited):
#     def say_hello(self):
#         return 'Hello'


if __name__ == '__main__':
    x = Inherited('world')
    print(x.say_hello())

    # Can not create class, error while compiling pycache, class is final

    # try:
    #     y = InheritedMore('test')
    #     print(y.say_hello())
    # except TypeError as err:
    #     print(f'Final metaclass works - {err.args[0]}')
