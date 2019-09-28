import abc


class Context:
    pass


class AbstractState(metaclass=abc.ABCMeta):
    pass


class StateFirst(AbstractState):
    pass


class StateSecond(AbstractState):
    pass


