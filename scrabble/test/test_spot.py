import unittest
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
