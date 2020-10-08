import sys


class ItemGetterSetter:
    def __init__(self):
        self.value1 = 'value11'
        self.value2 = 'value22'

    def __repr__(self):
        return f'Value1 = {self.value1}; Value2 = {self.value2}'

    def __getattr__(self, item):
        if item == 'test':
            return 'test value called'

        raise AttributeError

    def __setattr__(self, key, value):
        if value == 'test':
            self._test = 'super-long-value'
        else:
            super().__setattr__(key, value)


holder = ItemGetterSetter()

print(holder.value1)

holder.test = 'test1'

print(holder.test)

sys.exit()
