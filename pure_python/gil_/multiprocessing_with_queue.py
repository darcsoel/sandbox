import multiprocessing
import random
from sys import exit


class SomeProcess:
    stopping_element = None

    def __init__(self, numbers: list, queue):
        self._numbers = numbers
        self._queue = queue

    def __call__(self, *args, **kwargs):
        raise NotImplementedError


class CreatorProcess(SomeProcess):
    def __call__(self, *args, **kwargs):
        for number in self._numbers:
            self._queue.put(number)
            print(f'Putting number = {number}')


class ConsumerProcess(SomeProcess):
    def __call__(self, *args, **kwargs):
        while True:
            number = self._queue.get()

            if number is self.stopping_element:
                break

            print(f'Retrieved number = {number}')


def main():
    random_list = random.sample(range(10, 30), 10)
    random_list.append(SomeProcess.stopping_element)
    queue = multiprocessing.Queue()

    random_list_len = len(random_list)
    print(f'Numbers list length = {random_list_len}')

    creator_process = multiprocessing.Process(
        target=CreatorProcess(random_list, queue))
    consumer_process = multiprocessing.Process(
        target=ConsumerProcess(random_list, queue))

    print('Start processes')
    creator_process.start()
    consumer_process.start()

    print('Close queue and join thread')
    queue.close()
    queue.join_thread()

    print('Join processes')
    creator_process.join()
    consumer_process.join()

    print('Kill processes')
    creator_process.kill()
    consumer_process.kill()


if __name__ == '__main__':
    main()
    exit()
