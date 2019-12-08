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

    def __init__(self, name: str, limit: int):
        self._name = name
        self._limit = limit

    def __call__(self, *args, **kwargs):
        for number in range(self._limit):
            print(f'{self._name} -> {number}')


if __name__ == '__main__':
    worker1 = Worker('first', 10)
    worker2 = Worker('second', 10)

    thread1 = threading.Thread(target=worker1)
    thread2 = threading.Thread(target=worker2)
    thread1.start()

    # method join will wait for thread finish
    # thread1.join()

    thread2.start()

