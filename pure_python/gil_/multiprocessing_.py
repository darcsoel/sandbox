import multiprocessing
import os
import random
from sys import exit


class Process:
    def __init__(self, number):
        self._number = number

    def __call__(self, *args, **kwargs):
        proc = os.getpid()
        n = self._number

        print(f"ID {proc} -> number {n}")


def main():
    random_list = random.sample(range(10, 30), 5)
    processes = []

    for number in random_list:
        process = multiprocessing.Process(target=Process(number))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    for process in processes:
        process.kill()


if __name__ == '__main__':
    main()
    exit()
