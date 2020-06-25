import unittest

from cryptography.shamir_secret_share import ShamirSecretEncoder, ShamirSecretDecoder


class ShamirSecretTest(unittest.TestCase):
    def setUp(self) -> None:
        self.phrase = 'some secret phrase to crypto'

        encoder = ShamirSecretEncoder(self.phrase)
        self.keys = encoder.encode()

    def test_decoder(self):
        decoder = ShamirSecretDecoder(self.keys)
        decoded = decoder.decode()
        self.assertEquals(self.phrase, decoded)
