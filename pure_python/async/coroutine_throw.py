from sys import exit


def coroutine():
    while True:
        enter_value = yield
        yield enter_value


def test_generator(iterable):
    yield iterable


def coroutine_modern():
    while True:
        enter_value = yield
        yield from enter_value


if __name__ == '__main__':
    worker = coroutine()
    next(worker)
    x1 = worker.send('test1')
    print(f'Coroutine outer value = {x1}')

    try:
        worker.throw(ValueError)
    except ValueError:
        print('Raise error from coroutine\n')
    finally:
        worker.close()

    worker = coroutine_modern()
    next(worker)
    x1 = worker.send(['test new', 'test new 2'])

    while True:
        try:
            if not x1:
                break
            print(f'[Coroutine modern] outer value = {x1}')
            x1 = next(worker)
        except StopIteration:
            break

    worker.close()

    exit()
