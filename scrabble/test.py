import unittest


class Tile:
    def _init_(self, letter, score):
        self.letter = letter
        self.score = score


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
