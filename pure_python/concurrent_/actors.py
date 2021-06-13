from collections import deque

_register = {}
_queue = deque()


def actor(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        _register[func.__name__] = gen

    return wrapper


def send(name, msg):
    _queue.append((name, msg))


def run():
    while _queue:
        name, msg = _queue.popleft()
        _register[name].send(msg)


def ping():
    while True:
        msg = yield
        print(f'Ping - {msg}')
