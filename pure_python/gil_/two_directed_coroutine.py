from sys import exit


def coroutine(initial_value=None):
    enter_value = None

    try:
        while True:
            enter_value = yield enter_value

            if not enter_value:
                enter_value = initial_value

            print(f'Coroutine inner value = {enter_value}')

    except GeneratorExit:
        print('Job stopped successfully')


if __name__ == '__main__':
    worker = coroutine('test')
    x1 = next(worker)
    print(f'Coroutine outer value = {x1}')

    check = worker.send('worker')
    print(f'Send method check = {check}')

    x2 = next(worker)
    print(f'Coroutine outer value = {x2}')

    worker.send('worker')

    x3 = next(worker)
    print(f'Coroutine outer value = {x3}')

    worker.close()
    exit()
