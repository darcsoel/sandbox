import sys
from itertools import zip_longest


class Vector:
    def __init__(self, vector):
        self._vector = vector

    @property
    def vector(self):
        return self._vector

    def __add__(self, other):
        if isinstance(other, Vector):
            return self.__add_vector_to_vector(other)
        else:
            raise ValueError('Wrong adding instance')

    def __add_vector_to_vector(self, other):
        if not len(self._vector) or not len(other.vector):
            raise ValueError('Vector can not be empty')

        result = []

        for first, second in zip_longest(self._vector, other.vector):
            result.append(first + second)

        self._vector = result
        return self


if __name__ == '__main__':
    some_vector = [1, 4, 9]
    vector_to_add = Vector([2, 1, 5])

    v2 = Vector(some_vector)
    v2 += vector_to_add

    print(f'Vector plus vector = {v2.vector}')

    sys.exit()
