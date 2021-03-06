import asyncio
import itertools
import sys


async def spinner():
    write, flush = sys.stdout.write, sys.stdout.flush

    for char in itertools.cycle('|/-\\'):
        write(char)
        flush()

        try:
            await asyncio.sleep(.1)
            write('\x08')
        except asyncio.CancelledError:
            write('\x08')
            break


async def supervisor():
    sp = asyncio.create_task(spinner())
    await asyncio.sleep(4)
    sp.cancel()
    return True


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    try:
        result = loop.run_until_complete(supervisor())
    finally:
        loop.close()

    sys.exit()
