def some_func(a, b, /, c, d, e):
    print(f'{a}, {b}')
    print(f'{c}-{d}-{e}')


some_func(1, 2, d=3, c=4, e=5)

some_func(1, 2, 4, 3, 5)

some_func(1, 2, 4, 1, 5)
