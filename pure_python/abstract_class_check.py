import abc


class AbcTest(abc.ABC):
    def __init__(self):
        self.__x = 2

    @property
    def x(self):
        return self.__x

    @abc.abstractmethod
    def abstract(self):
        pass


class Realization(AbcTest):
    def abstract(self):
        return 'hello'


if __name__ == '__main__':
    # can not initialize, raise TypeError
    # x = AbcTest()
    # print(x.x)
    # x.abstract()

    y = Realization()
    print(y.abstract())
    print(y.x)
