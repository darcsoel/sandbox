from sys import exit


class SingletonMeta(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)

        return cls.__instances[cls]


class SingletonImpl(metaclass=SingletonMeta):
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data


if __name__ == '__main__':
    first = SingletonImpl('first')
    second = SingletonImpl('second')

    print(first.data)
    print(second.data)

    exit()
