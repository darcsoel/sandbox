import logging
import multiprocessing
from sys import exit


def worker(conn):
    """Get data from parent process"""

    logging.warning(conn.recv())
    conn.send('send by child process')


if __name__ == '__main__':
    """Try python pipe feature"""

    conn1, conn2 = multiprocessing.Pipe()
    process = multiprocessing.Process(target=worker, args=(conn2,))

    process.start()
    conn1.send('send by main process')

    logging.warning(conn1.recv())

    exit()
