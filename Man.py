from abc import ABCMeta, abstractmethod


class Alive():
    __metaclass__ = ABCMeta

    @abstractmethod
    def backbone(self):
        pass


class Man(Alive):
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def __eq__(self, other):
        if not isinstance(other, Man):
            return False

        return self.first_name == other.first_name and self.first_name == other.first_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    def backbone(self):
        print('I have backbone')


if __name__ == '__main__':
    first = Man('john', 'doe')
    second = Man('john', 'doe')

    print(first == second)
