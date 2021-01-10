import asyncio
import random
import sys

# ANSI colors
# "\033[0m",  # End of color

c = (
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
    "\033[92m",  # Green
    "\033[96m",  # Cyan
)

random_min_number = 1
random_max_number = 10


async def random_color_print(index, color_index_max=7):
    print(c[index] + 'Initialized')
    rnd = random.randint(random_min_number, random_max_number)

    while rnd < color_index_max:
        print(c[index] + f'random print {index}')
        await asyncio.sleep(1)
        rnd = random.randint(random_min_number, random_max_number)

    return index


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    main = asyncio.gather(*(random_color_print(i) for i in range(5)))
    loop.run_until_complete(main)

    sys.exit()
