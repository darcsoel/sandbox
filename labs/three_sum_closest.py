import typing as t
import sys


class ThreeElementsSumClosest:
    """
    Find element, where three-sum of nearest most closest to target
    """

    def __init__(self, numbers: t.List[int], target: int = None):
        if not isinstance(numbers, list):
            raise ValueError("numbers must be list instance")

        for number in numbers:
            if not isinstance(number, int):
                raise ValueError('each number must be int')

        if len(numbers) < 3:
            raise ValueError('numbers must be at least three')

        if target is not None and not isinstance(target, int):
            raise ValueError('target must be int')

        self.numbers = numbers
        self.target = target

    def find(self, target: int = None):
        """Main method"""

        if target is None and self.target is None:
            raise ValueError('you must provide target')

        if target is not None and not isinstance(target, int):
            raise ValueError('target must be int')

        target = target or self.target

        result = 0
        sorted_numbers = sorted(self.numbers)
        diff = sorted_numbers[-1] - sorted_numbers[0]

        for i in range(1, len(self.numbers) - 1):
            sum_ = self.numbers[i - 1] + self.numbers[i] + self.numbers[i + 1]

            if abs(sum_ - target) < diff:
                diff = abs(sum_ - target)
                result = self.numbers[i]

        return result


if __name__ == '__main__':
    sys.exit()
