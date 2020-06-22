from sys import exit
from mod import Mod
from os import urandom
import random
import string
from functools import reduce
from operator import mul


class ShamirSecretBasic:
    """Constant library"""

    big_number_base_encrypt = 2 ** 521 - 1
    keys_count = 3


class ShamirSecretEncoder(ShamirSecretBasic):
    """
    Encode string
    """

    keys_count = 5

    def __init__(self, phrase):
        if not isinstance(phrase, str) or not phrase:
            raise ValueError("Wrong phrase")

        self._keys = []
        self._phrase = phrase

    def _int_from_string(self, s):
        bytes_ = s.encode('utf-8')
        return self._int_from_bytes(bytes_)

    @staticmethod
    def _int_from_bytes(bytes_):
        acc = 0
        for b in bytes_:
            acc *= 256
            acc += b

        return acc

    def _build_first_keys(self, phrase):
        polynomial = [phrase]

        for i in range(2):
            key = Mod(self._int_from_bytes(urandom(16)), self.big_number_base_encrypt)
            polynomial.append(key)

        return polynomial

    def _build_polynomial_keys(self, polynomial):
        shards = {}
        for i in range(self.keys_count):
            x = Mod(self._int_from_bytes(urandom(16)), self.big_number_base_encrypt)
            y = self._evaluate_polynomial(polynomial, x)
            shards[i] = (x, y)
        return shards

    @staticmethod
    def _evaluate_polynomial(coefficients, x):
        acc = 0
        power = 1
        for c in coefficients:
            acc += c * power
            power *= x
        return acc

    def encode(self):
        """
        Encode inner string, return decoded string
        :return: str
        """

        numeric_phrase = self._int_from_string(self._phrase)

        if numeric_phrase >= self.big_number_base_encrypt:
            raise ValueError('Can not encrypt. String value too big')

        numeric_phrase = Mod(numeric_phrase, self.big_number_base_encrypt)

        polynomial = self._build_first_keys(numeric_phrase)
        keys = self._build_polynomial_keys(polynomial)

        return keys


class ShamirSecretDecoder(ShamirSecretBasic):
    """
    Decode string from at least 3 keys
    """

    def __init__(self, keys: (list, tuple, dict)):
        if not isinstance(keys, (list, tuple, dict)):
            raise ValueError("keys must be iterable")

        if len(keys) < self.keys_count:
            raise ValueError(f"keys must contains at least {self.keys_count} keys")

        if isinstance(keys, dict):
            keys = list(keys.values())

        self._keys = keys
        self._phrase = ''

    def decode(self):
        """Decode bytes keys to string"""

        x_s = [s[0] for s in self._keys]
        acc = Mod(0, self.big_number_base_encrypt)

        for i in range(len(self._keys)):
            others = list(x_s)
            cur = others.pop(i)
            factor = Mod(1, self.big_number_base_encrypt)
            for el in others:
                factor *= el * (el - cur).inverse()
            acc += factor * self._keys[i][1]

        return bytes(str(acc)).decode('utf-8')


def main():
    phrase = 'some secret phrase to crypto'

    encoder = ShamirSecretEncoder(phrase)
    keys = encoder.encode()

    decoder = ShamirSecretDecoder(keys)
    decoded = decoder.decode()

    print(decoded)


if __name__ == '__main__':
    main()
    exit()
