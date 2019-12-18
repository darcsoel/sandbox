import contextlib


class Context:
    def __init__(self):
        self.__x = 0

    def __enter__(self):
        self.__x = 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__x = -1

    @property
    def x(self):
        return self.__x


context = Context()

print(context.x)

with context as c:
    print(context.x)

print(context.x)


@contextlib.contextmanager
def func_context_manager(func):
    print('start context manager')
    yield func()
    print('finish context manager')


def some_def():
    print('running func')


with func_context_manager(some_def):
    print('running')
