import abc


class Component(metaclass=abc.ABCMeta):
    def operation(self):
        raise NotImplementedError


class Composite(Component):
    def __init__(self):
        self.result = None
        self.children = set()

    def operation(self):
        for child in self.children:
            self.result = child.operation()

    def add(self, component: Component):
        self.children.add(component)
        return self

    def remove(self, component: Component):
        self.children.discard(component)
        return self


class AdditionalComponent(Component):
    def __init__(self, first, second):
        self._first = first
        self._second = second

    def operation(self):
        return self._first + self._second


class MultiplyComponent(Component):
    def __init__(self, first, second):
        self._first = first
        self._second = second

    def operation(self):
        return self._first * self._second


if __name__ == '__main__':
    additional = AdditionalComponent(2, 5)
    multiply = MultiplyComponent(2, 3)

    composite = Composite()
    composite.add(additional).add(multiply).operation()

    print(composite.result)
