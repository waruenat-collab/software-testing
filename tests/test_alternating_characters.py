import unittest
from src.alternating_characters import alternating_characters


class AlternatingCharactersTest(unittest.TestCase):

    def test_no_deletion(self):
        self.assertEqual(alternating_characters("ABAB"), 0)

    def test_with_deletion(self):
        self.assertEqual(alternating_characters("AAAB"), 2)

    def test_single_char(self):
        self.assertEqual(alternating_characters("A"), 0)