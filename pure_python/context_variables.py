"""Contextvars feature test"""

# import asyncio
import contextvars
import sys

buffer = contextvars.ContextVar('buffer_str')


async def reciever():
    pass


async def producer():
    pass


if __name__ == '__main__':
    producer()

    test_var = contextvars.ContextVar('test', default='zero')

    x = test_var.get()

    sys.exit()
