import multiprocessing
import random
import threading
from sys import exit

import redis


class AbstractProcess:
    """Abstract class for process"""

    stopping_element = -1
    redis_connection_params = {'host': 'localhost', 'port': 6379, 'db': 1}
    redis_list_name = 'multi_threading_processing'

    def __init__(self, numbers: list, queue, process_name=None):
        self._numbers = numbers
        self._queue = queue

        if isinstance(process_name, str):
            self._process_name = process_name
        else:
            self._process_name = 'default'

    def __call__(self, *args, **kwargs):
        raise NotImplementedError


class CreatorProcess(AbstractProcess):
    """This one create data for queue"""

    def __call__(self, *args, **kwargs):
        for number in self._numbers:
            print(f'{self._process_name}: Created number = {number}')
            self._queue.rpush(self.redis_list_name, number)


class ConsumerProcess(AbstractProcess):
    """This one pull data and making some actions"""

    def __call__(self, *args, **kwargs):
        while True:
            number = self._queue.lpop(self.redis_list_name)
            try:
                number = int(number)
            except TypeError:
                break

            if number == self.stopping_element:
                break

            print(f'{self._process_name}: Retrieved number = {number}')


class MultiprocessingWorker:
    """Run few processes in current thread"""

    def __init__(self, random_numbers, process_count=None, is_creator=False, redis_connector=None):
        if not isinstance(random_numbers, list):
            raise ValueError('Numbers must be list instance')

        self._numbers = random_numbers

        if process_count is None:
            process_count = random.randint(2, 5)

        if process_count <= 0:
            raise ValueError('Process count can not be less than 1')

        if not isinstance(process_count, int):
            raise ValueError('Process count must be integral integer')

        if not process_count:
            process_count = 1

        self._process_count = process_count

        if not isinstance(is_creator, bool):
            raise ValueError('is_creator param must be bool type')

        self._is_creator = is_creator

        if not isinstance(redis_queue, redis.Redis):
            raise ValueError('redis param must be instance of redis.Redis class')

        if is_creator:
            self._worker_name = 'creator_worker'
        else:
            self._worker_name = 'consumer_worker'

        self._redis = redis_connector
        self._processes = []

    def __call__(self, *args, **kwargs):
        for index in range(self._process_count):
            if self._is_creator:
                name = f'{self._worker_name}-creator-{index}'
                process = multiprocessing.Process(target=CreatorProcess(self._numbers, self._redis, f'{name}'))
            else:
                name = f'{self._worker_name}-consumer-{index}'
                process = multiprocessing.Process(target=ConsumerProcess(self._numbers, self._redis, f'{name}'))

            self._processes.append(process)

        for process in self._processes:
            process.start()

        for process in self._processes:
            process.join()

        for process in self._processes:
            process.kill()


if __name__ == '__main__':
    random_list = random.sample(range(10, 30), 10)
    random_list.append(AbstractProcess.stopping_element)

    redis_queue = redis.Redis(**AbstractProcess.redis_connection_params)

    worker1 = MultiprocessingWorker(random_list, redis_connector=redis_queue, is_creator=True)
    worker2 = MultiprocessingWorker(random_list, redis_connector=redis_queue)

    thread1 = threading.Thread(target=worker1)
    thread2 = threading.Thread(target=worker2)
    thread1.start()
    thread2.start()

    exit()
