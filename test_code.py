# 1,2,5,10,25,50

from datetime import datetime


def exec_time(func):
    def wrap(*args):
        now_start = datetime.now()
        result = func(*args)
        now_final = datetime.now()
        print(now_final - now_start)
        print(result)

    return wrap


class Terminal:
    coins = [1, 2, 5, 10, 25, 50]

    def __init__(self, sum_):
        self._sum = sum_
        self._result = []

    @exec_time
    def give_coins(self):
        sum_ = self._sum

        for coin in reversed(self.coins):
            count = sum_ // coin

            self._result.extend([coin] * count)

            sum_ -= coin * count

            if sum(self._result) == sum_:
                break

        return self._result


sum__ = 199

term = Terminal(sum__)
term.give_coins()

