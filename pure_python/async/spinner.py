import asyncio
import itertools
import sys


@asyncio.coroutine
def spinner():
    write, flush = sys.stdout.write, sys.stdout.flush

    for char in itertools.cycle('|/-\\'):
        write(char)
        flush()
        write('\x08')

        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(spinner())

    loop.close()
    sys.exit()
