import abc


class AbstractState(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        pass


class StateFirst(AbstractState):
    def run(self):
        print('Start service 1')

    def stop(self):
        print('Stop service 1')


class StateSecond(AbstractState):
    def run(self):
        print('Start service 2')

    def stop(self):
        print('Stop service 2')


class Context:
    def __init__(self):
        self.__state = StateFirst()

    def check_first_service(self):
        self.__state = StateFirst()

    def check_second_service(self):
        self.__state = StateSecond()

    def start_service(self):
        self.__state.run()

    def stop_service(self):
        self.__state.stop()


context = Context()
context.check_first_service()
context.start_service()
context.stop_service()
context.check_second_service()
context.start_service()
context.stop_service()
