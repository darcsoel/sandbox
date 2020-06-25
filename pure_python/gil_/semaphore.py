import random
import threading
from sys import exit

max_workers = 2
min_number = 10
max_number = 20


class Worker:
    """
    Class demonstrate semaphore functional. While
    """

    def __init__(self, worker_name, number, semaphore=None, event=None):
        self._worker_name = worker_name
        self._number = number
        self._semaphore = None
        self._event = None

        if isinstance(semaphore, threading.BoundedSemaphore):
            self._semaphore = semaphore
        if isinstance(event, threading.Event):
            self._event = event

    def __call__(self, *args, **kwargs):
        if self._semaphore:
            self._semaphore.acquire()

        for i in range(self._number):
            print(f'{self._worker_name} -> {i}\n')

        if self._semaphore:
            self._semaphore.release()


def main():
    semaphore = threading.BoundedSemaphore(max_workers)
    event = threading.Event()
    rand_number = random.randint(min_number, max_number)

    print(f'Max number = {rand_number}')

    thread1 = threading.Thread(target=Worker('worker1', rand_number, semaphore))
    thread2 = threading.Thread(target=Worker('worker2', rand_number, semaphore))
    thread3 = threading.Thread(target=Worker('worker3', rand_number, semaphore))

    thread1.start()
    thread2.start()
    thread3.start()  # sometimes it do not called


if __name__ == '__main__':
    main()
    exit()
