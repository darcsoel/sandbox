import itertools
import sys
import threading
import time


class Spinner:
    alive = True

    def __call__(self, *args, **kwargs):
        write, flush = sys.stdout.write, sys.stdout.flush

        for char in itertools.cycle('|/-\\'):
            write(char)
            time.sleep(.1)
            flush()
            write('\x08')

            if not self.alive:
                break


if __name__ == '__main__':
    spinner = Spinner()

    spinner_thread = threading.Thread(target=spinner)
    spinner_thread.start()

    time.sleep(5)
    spinner.alive = False

    spinner_thread.join()

    sys.exit()
