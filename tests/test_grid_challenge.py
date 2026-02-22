import unittest
from src.grid_challenge import grid_challenge


class GridChallengeTest(unittest.TestCase):

    def test_yes_case(self):
        grid = ["abc", "ade", "efg"]
        self.assertEqual(grid_challenge(grid), "YES")

    def test_no_case(self):
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        self.assertEqual(grid_challenge(grid), "NO")