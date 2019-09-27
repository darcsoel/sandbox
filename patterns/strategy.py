import abc


class AbstractStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def strategy_call(self):
        print('call')


class Context:
    def __init__(self, strategy):
        self.__strategy = strategy

    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self, strategy):
        self.__strategy = strategy

    def request(self):
        try:
            self.__strategy.strategy_call()
        except AttributeError:
            print('attr err')


class StrategyLight(AbstractStrategy):
    def strategy_call(self):
        print('light method')


class StrategyHard(AbstractStrategy):
    def strategy_call(self):
        print('hard method')


strategy_l = StrategyLight()
strategy_h = StrategyHard()

context = Context(strategy_l)
context.request()
context.strategy = strategy_h
context.request()
