import itertools

if __name__ == '__main__':
    some_numbers = range(30)

    iterator_slice = itertools.islice(some_numbers, 2, 10)

    print(list(iterator_slice))
