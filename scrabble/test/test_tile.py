import unittest
from game.tile import Tile


class TestTile(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 2)
        self.assertEqual(
            tile.letter,
            'A',
        )
        self.assertEqual(
            tile.score,
            2,
        )
