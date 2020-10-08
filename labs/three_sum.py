import sys
import typing as t


class ThreeElementsSum:
    """
    Search unique triplets with zero sum
    """

    def __init__(self, elements: t.Union[list, tuple, set]):
        if not isinstance(elements, (list, tuple, set)):
            raise ValueError('elements must be instance of list or tuple')

        for e in elements:
            if not isinstance(e, int):
                raise ValueError("all elements must be int instance")

        self._elements = elements
        self._elements.sort()
        self._result = []

    def find(self):
        for i in range(len(self._elements) - 2):
            if i > 0 and self._elements[i] == self._elements[i - 1]:
                continue
            left, right = i + 1, len(self._elements) - 1

            while left < right:
                sum_ = self._elements[i] + self._elements[left] + \
                       self._elements[right]

                if sum_ == 0:
                    self._result.append([self._elements[i],
                                         self._elements[left],
                                         self._elements[right]])

                    left += 1
                    right -= 1

                    while left < right and \
                            self._elements[left] == self._elements[left - 1]:
                        left += 1
                    while left < right and \
                            self._elements[right] == self._elements[right + 1]:
                        right -= 1

                elif sum_ < 0:
                    left += 1
                else:
                    right -= 1

        return self._result


if __name__ == '__main__':
    example_elements = [-1, 0, 1, 2, -1, -4]

    print(ThreeElementsSum(example_elements).find())

    sys.exit()
