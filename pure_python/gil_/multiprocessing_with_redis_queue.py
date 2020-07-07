import multiprocessing
import random
from sys import exit
import redis


class AbstractProcess:
    """
    Basic 'abstract' class
    """

    stopping_element = -1
    redis_connection_params = {'host': 'localhost', 'port': 6379, 'db': 0}
    redis_list_name = 'list_queue'

    def __init__(self, numbers: list, queue):
        self._numbers = numbers
        self._queue = queue

    def __call__(self, *args, **kwargs):
        raise NotImplementedError


class CreatorProcess(AbstractProcess):
    """This one create data for queue"""

    def __call__(self, *args, **kwargs):
        for number in self._numbers:
            self._queue.rpush(self.redis_list_name, number)


class ConsumerProcess(AbstractProcess):
    """This one pull data and making some actions"""

    def __call__(self, *args, **kwargs):
        while True:
            number = self._queue.lpop(self.redis_list_name)
            number = int(number)

            if number == self.stopping_element:
                break

            print(f'Retrieved number = {number}')


def main():
    random_list = random.sample(range(10, 30), 10)
    random_list.append(AbstractProcess.stopping_element)
    redis_queue = redis.Redis(**AbstractProcess.redis_connection_params)

    random_list_len = len(random_list)
    print(f'Numbers list length = {random_list_len}')

    creator_process = multiprocessing.Process(target=CreatorProcess(random_list, redis_queue))
    consumer_process = multiprocessing.Process(target=ConsumerProcess(random_list, redis_queue))

    print('Start processes')
    creator_process.start()
    consumer_process.start()

    print('Join processes')
    creator_process.join()
    consumer_process.join()

    print('Kill processes')
    creator_process.kill()
    consumer_process.kill()


if __name__ == '__main__':
    main()
    exit()
