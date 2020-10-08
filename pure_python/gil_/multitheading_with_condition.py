"""
Learn threading with lock and condition
"""

import sys
import threading


class Worker:
    """
    Thread worker
    Contains name, loop limit
    Class variables are threading lock and condition,
    to delegate work to one thread
    """

    lock: threading.Lock = None
    condition: threading.Condition = None
    storage: list = None

    def __init__(self, name: str):
        if not name or not isinstance(name, str):
            raise ValueError('Wrong thread name. Must be string instance')

        self._name = name

    def __call__(self, *args, **kwargs):
        if not self.lock or not self.condition:
            raise ValueError("Thread worker do not have lock or condition")

        if not self.storage:
            raise ValueError("Thread worker must have common storage")

        if not isinstance(self.storage, list):
            raise ValueError("Thread worker storage must be instance of list")


class ConsumerWorker(Worker):
    def __call__(self, *args, **kwargs):
        super().__call__(*args, **kwargs)

        while self.storage:
            with self.lock:
                print('wait')
                self.condition.wait()

                if len(self.storage) > 1:
                    first_elem = self.storage.pop()
                    second_elem = self.storage.pop()
                    print(f'{self._name} -> {first_elem}, {second_elem}')
                else:
                    break


class ProducerWorker(Worker):
    def __call__(self, *args, **kwargs):
        super().__call__(*args, **kwargs)

        with self.lock:
            print('nofity all')
            self.condition.notify_all()


if __name__ == '__main__':
    worker_lock = threading.Lock()
    worker_condition = threading.Condition(worker_lock)
    worker_storage = list(range(30))

    worker1 = ConsumerWorker('first')
    worker1.lock = worker_lock
    worker1.condition = worker_condition
    worker1.storage = worker_storage

    worker2 = ProducerWorker('second')
    worker2.lock = worker_lock
    worker2.condition = worker_condition
    worker2.storage = worker_storage

    thread1 = threading.Thread(target=worker1)
    thread2 = threading.Thread(target=worker2)

    thread1.start()
    thread2.start()

    sys.exit()
