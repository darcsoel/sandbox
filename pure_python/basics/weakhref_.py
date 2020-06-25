import weakref


def fin():
    print('Destroy')


if __name__ == '__main__':
    first = {1, 2, 3}
    second = first

    checker = weakref.finalize(first, fin)
    print(checker.alive)

    second = '1'
    print(checker.alive)

    del first
    print(checker.alive)
    exit()
