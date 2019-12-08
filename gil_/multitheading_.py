import threading


class BadWorker(threading.Thread):
    """
    Bad realization, no possibility to reuse code and hard testing and debugging
    """

    def __init__(self):
        super().__init__()

    def run(self):
        """Some thread logic here"""
        pass


class Worker:
    """
    Good realization, use class as function with method `call`
    """

    def __init__(self, limit):
        self._limit = limit

    def __call__(self, *args, **kwargs):
        for number in range(self._limit):
            print(number)


if __name__ == '__main__':
    worker = Worker(3)

    thread = threading.Thread(target=worker)
    thread.run()

