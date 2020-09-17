import sys
from itertools import zip_longest


class Vector:
    def __init__(self, vector):
        self._vector = vector

    @property
    def vector(self):
        return self._vector

    def __add__(self, other):
        if isinstance(other, int):
            return self.__add_integer_to_vector(other)
        elif isinstance(other, Vector):
            return self.__add_vector_to_vector(other)
        else:
            raise ValueError('Wrong adding instance')

    def __add_integer_to_vector(self, other):
        vector_to_int = 0
        modified_vector = []

        for lvl, number in enumerate(self._vector):
            level = lvl + 1
            vector_to_int += number * 10 ** (len(self._vector) - level)

        vector_to_int += other

        # todo not completed logic, fix bug
        while vector_to_int:
            vector_to_int /= 10
            modified_vector.append(vector_to_int)

        self._vector = modified_vector
        return self

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
    number_to_increase = 2
    vector_to_add = Vector([2, 1, 5])

    v = Vector(some_vector)
    v += + number_to_increase

    print(f'Increased vector = {v.vector}')

    v2 = Vector(some_vector)
    v2 += vector_to_add

    print(f'Vector plus vector = {v2.vector}')

    sys.exit()
