import functools
import time


def time_dec(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f'Running time - {finish - start}')
        return result

    return wrapper


def fib(number: int):
    if number < 2:
        return number

    return fib(number - 1) + fib(number - 2)


@functools.lru_cache()
def fib_cached(number: int):
    if number < 2:
        return number

    return fib(number - 1) + fib(number - 2)


print('Compare fibonacci functions for 10 numbers')
print(fib(10))
print(fib_cached(10))

print('\nCompare fibonacci functions for 30 numbers')
print(fib(30))
print(fib_cached(30))
