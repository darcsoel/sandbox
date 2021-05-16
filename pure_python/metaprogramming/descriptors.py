class Descriptor:
    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value


class Integer(Descriptor):
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('value should be integer')

        super().__set__(instance, value)


class PositiveNumber(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('value should be positive number')

        super().__set__(instance, value)


class PositiveInteger(Integer, PositiveNumber):
    pass


class Structure:
    number = PositiveInteger()


structure = Structure()
structure.number = 12
print(structure.number)

try:
    structure.number = -21
except ValueError as er:
    print(er.args[0])

try:
    structure.number = 'qweqwe'
except ValueError as er:
    print(er.args[0])
