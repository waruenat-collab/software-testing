import unittest
from src.two_characters import two_characters


class TwoCharactersTest(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(two_characters("beabeefeab"), 5)

    def test_no_valid(self):
        self.assertEqual(two_characters("aaaa"), 0)

    def test_two_chars_only(self):
        self.assertEqual(two_characters("abab"), 4)