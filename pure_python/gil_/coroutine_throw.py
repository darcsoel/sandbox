from sys import exit


def coroutine(initial_value=None):
    enter_value = None

    try:
        enter_value = yield enter_value

        if not enter_value:
            enter_value = initial_value

        print(f'Coroutine inner value = {enter_value}')

    except GeneratorExit:
        print('Job stopped successfully')


def coroutine_modern(initial_value=None):
    enter_value = None

    try:
        enter_value = yield from enter_value

        if not enter_value:
            enter_value = initial_value

        print(f'Coroutine inner value = {enter_value}')

    except GeneratorExit:
        print('Job stopped successfully')


if __name__ == '__main__':
    worker = coroutine('test')
    x1 = next(worker)
    print(f'Coroutine outer value = {x1}')

    try:
        worker.throw(ValueError)
    except ValueError:
        print('Raise error from coroutine')
    finally:
        worker.close()

    worker = coroutine_modern('test new')
    x1 = next(worker)
    print(f'Coroutine outer value = {x1}')

    worker.throw(ValueError)
    worker.close()

    exit()
