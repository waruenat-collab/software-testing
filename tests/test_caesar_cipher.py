import unittest
from src.caesar_cipher import caesar_cipher


class CaesarCipherTest(unittest.TestCase):

    def test_lowercase(self):
        self.assertEqual(caesar_cipher("abc", 2), "cde")

    def test_uppercase(self):
        self.assertEqual(caesar_cipher("XYZ", 3), "ABC")

    def test_non_alpha(self):
        self.assertEqual(caesar_cipher("a-b!", 1), "b-c!")

    def test_large_k(self):
        self.assertEqual(caesar_cipher("abc", 28), "cde")