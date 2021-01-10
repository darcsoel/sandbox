def simple_coroutine():
    getted = yield
    print(getted * 2)


def filter_coroutine(search):
    try:
        while True:
            entities = (yield)

            if search in entities:
                print(f'Found {search} in {entities}')
    except GeneratorExit:
        print('Stopping...')


if __name__ == '__main__':
    print('Simple coroutine\n')

    c = simple_coroutine()
    next(c)

    try:
        x = c.send(2)
    except StopIteration:
        x = 0

    print(x)

    print('\n\nSearching coroutine\n')

    f = filter_coroutine('hello')
    next(f)
    f.send('world')
    f.send('hello world')
    f.close()
