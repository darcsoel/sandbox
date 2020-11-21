import random
import string
import sys


if __name__ == '__main__':
    string_len = 30
    strings_count = 15

    for _ in range(strings_count):
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        rnd_str = ''.join(random.choice(chars) for _ in range(string_len))
        print(rnd_str)

    sys.exit()
