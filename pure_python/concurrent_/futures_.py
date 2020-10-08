import sys

from concurrent.futures import ThreadPoolExecutor


def worker(flag):
    print(f'You requested {flag} country flag\n')


if __name__ == '__main__':
    flags = ('UA', 'USA', 'GE', 'RU')
    with ThreadPoolExecutor() as executor:
        executor.map(worker, flags)
        sys.exit()
