from sys import exit
from mod import Mod
from os import urandom


class ShamirSecretBasic:
    big_number_base_encrypt = 2**521 - 1
    keys_count = 5


class ShamirSecretEncoder(ShamirSecretBasic):
    def __init__(self, phrase, keys: list):
        if not isinstance(keys, (list, tuple)):
            raise ValueError("keys must be list or tuple")

        if len(keys) != self.keys_count:
            raise ValueError("keys must contains 5 keys")

        self._keys = keys
        self._phrase = phrase

    @staticmethod
    def int_from_string(s):
        bytes_ = s.encode('utf-8')

        acc = 0
        for b in bytes_:
            acc = acc * 256
            acc += b

        return acc

    def encode(self):
        pass


class ShamirSecretDecoder(ShamirSecretBasic):
    keys_count = 3

    def __init__(self, phrase, keys: list):
        if not isinstance(keys, (list, tuple)):
            raise ValueError("keys must be list or tuple")

        if len(keys) < self.keys_count:
            raise ValueError(f"keys must contains at least {self.keys_count} keys")

        self._keys = keys
        self._phrase = phrase

    def decode(self):
        pass


def main():
    phrase = 'some secret phrase to crypto'

    encoder = ShamirSecretEncoder()


if __name__ == '__main__':
    main()
    exit()
