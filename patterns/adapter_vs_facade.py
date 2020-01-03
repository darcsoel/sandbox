import math


class Legacy:
    def __init__(self):
        self._x = 1
        self._y = 2

    def calculate_hypotenuse(self):
        return math.sqrt(self._x ** 2 + self._y ** 2)

    def double_x(self):
        self._x **= 2

    def double_y(self):
        self._y **= 2

    def calculate_hypotenuse_simple(self):
        return math.sqrt(self._x + self._y)


class CustomAdapter:
    def __init__(self):
        self.legacy = Legacy()

    def request(self):
        return self.legacy.calculate_hypotenuse()


class CustomFacade:
    def __init__(self):
        self.legacy = Legacy()

    def request(self):
        self.legacy.double_x()
        self.legacy.double_y()
        return self.legacy.calculate_hypotenuse_simple()


t1 = CustomAdapter()
print(t1.request())

t2 = CustomFacade()
print(t2.request())
