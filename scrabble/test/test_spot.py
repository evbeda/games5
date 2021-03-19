import unittest
from parameterized import parameterized
from ..game.spot import Spot
from ..game.tile import Tile


class TestSpot(unittest.TestCase):

    def test_spot_constructor(self):
        s = Spot(0,'c')
        self.assertEqual(s.mult_value, 0)
        self.assertEqual(s.mult_type, 'c')

    def test_set_tile(self):
        t = Tile('a')
        s = Spot(0,'c')
        s.set_tile(t)
        self.assertEqual(s.tile.letter, t.letter)

    @parameterized.expand([
        (Spot(0, 'c'), Tile('a'), ' a '),
        (Spot(2, 'l'), None, 'x2l'),
        (Spot(2, 'l'), Tile('a'), ' a '),
        (Spot(2, 'w'), None, 'x2w'),
        (Spot(2, 'l'), Tile('a'), ' a '),
        (Spot(3, 'w'), None, 'x3w'),
        (Spot(2, 'l'), Tile('a'), ' a '),
        (Spot(3, 'l'), None, 'x3l'),
        (Spot(2, 'l'), Tile('a'), ' a '),
        (Spot(0, 'c'), None, '   '),
    ])
    def test_spot_format(self, spot, tile, expected):
        s = spot
        if tile:
            s.set_tile(tile)
        self.assertEqual(s.get_spot(), expected)
