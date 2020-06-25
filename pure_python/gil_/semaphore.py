import random
import threading
from sys import exit

max_workers = 2
min_number = 7
max_number = 15


class Worker:
    """
    Class demonstrate semaphore functional. While
    """

    def __init__(self, worker_name, number, semaphore=None):
        self._worker_name = worker_name
        self._number = number
        self._semaphore = None

        if isinstance(semaphore, threading.BoundedSemaphore):
            self._semaphore = semaphore

    def __call__(self, *args, **kwargs):
        self._semaphore.acquire()

        for i in range(self._number):
            print(f'{self._worker_name} -> {i}\n')

        self._semaphore.release()


def main():
    semaphore = threading.BoundedSemaphore(max_workers)
    rand_number = random.randint(min_number, max_number)

    print(f'Max number = {rand_number}')

    thread1 = threading.Thread(target=Worker('worker1', rand_number, semaphore))
    thread2 = threading.Thread(target=Worker('worker2', rand_number, semaphore))
    thread3 = threading.Thread(target=Worker('worker3', rand_number, semaphore))

    thread1.start()
    thread2.start()
    thread3.start()


if __name__ == '__main__':
    main()
    exit()
