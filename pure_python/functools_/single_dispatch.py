import functools


@functools.singledispatch
def add(a: int, b: int):
    return a + b


@add.register(str)
def _(a: str, b: str):
    return f'{a} --- {b}'


first_number = 1
second_number = 3

first_str = 'hello'
second_str = 'world'

print(add(first_number, second_number))

print(add(first_str, second_str))
