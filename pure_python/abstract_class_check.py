import abc


class AbsTest(abc.ABC):
    def __init__(self):
        self.__x = 2

    @property
    def x(self):
        return self.__x


x = AbsTest()
print(x.x)
