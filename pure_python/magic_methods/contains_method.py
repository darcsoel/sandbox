class Container:
    def __init__(self, iterable):
        self.__iterable = iterable

    def __contains__(self, item):
        return item in self.__iterable


test_list = [1, 2, 3, 5]
container = Container(test_list)
print(1 in container)
print(4 in container)


class DictContainer:
    def __init__(self, iterable: dict):
        self.__iterable = iterable

    def __contains__(self, item):
        return item in self.__iterable.keys()


test_dict = {1: 'a', 2: 'b', 3: 'c'}
container = DictContainer(test_dict)
print(1 in container)
print(4 in container)
