import unittest
from src.funny_string import funny_string


class FunnyStringTest(unittest.TestCase):

    def test_funny(self):
        s = "acxz"
        result = funny_string(s)
        self.assertEqual(result, "Funny")

    def test_not_funny(self):
        s = "bcxz"
        result = funny_string(s)
        self.assertEqual(result, "Not Funny")

    def test_single_char(self):
        s = "a"
        result = funny_string(s)
        self.assertEqual(result, "Funny")