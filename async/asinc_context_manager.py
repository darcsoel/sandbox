import asyncio


class AsyncContextManager:
    def __init__(self, iterable):
        self._iterable = iterable

    @property
    def iterable(self):
        return self._iterable

    async def __aenter__(self):
        return self._iterable

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self._iterable = []


async def main():
    context_manager = AsyncContextManager([1, 2, 3, 4])

    async with context_manager:
        for i in context_manager.iterable:
            print(i)


if __name__ == '__main__':
    asyncio.run(main())
