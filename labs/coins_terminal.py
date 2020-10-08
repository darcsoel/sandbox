"""Practice task from Python position interview"""


import datetime
import sys


def exec_time(func):
    """Calculate command execution time"""

    def wrap(*args):
        """Inner wrapper for logging"""
        now_start = datetime.datetime.now()
        result = func(*args)
        now_final = datetime.datetime.now()

        execution_time = now_final - now_start
        print(f'Execution time = {execution_time}')

        return result

    return wrap


class Terminal:
    """Emulate coins terminal"""

    coins = [1, 2, 5, 10, 25, 50]

    def __init__(self, sum_to_return):
        self._sum = sum_to_return
        self._result = []

    @exec_time
    def give_coins(self):
        """return coins list"""

        sum_ = self._sum

        for coin in reversed(self.coins):
            count = sum_ // coin

            self._result.extend([coin] * count)
            sum_ -= coin * count

            if sum(self._result) == self._sum:
                break

        return self._result


sum_list_to_return = [199, 74, 52, 24, 4, 1]

if __name__ == '__main__':
    for sum_ in sum_list_to_return:
        term = Terminal(sum_)

        coins = term.give_coins()
        print(f'Sum to return = {sum_}. Returned coins = {coins}')

    sys.exit()
