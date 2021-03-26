import unittest
from ..game.tile_bag import TileBag
from ..game.tile import Tile


class TesttileBag(unittest.TestCase):

    def setUp(self):
        self.bag = TileBag()

    def test_tile_bag_attributes(self):
        t_b = TileBag()
        expected = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a',
                    'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e',
                    'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
                    'i', 'i', 'i', 'i', 'i', 'i',
                    's', 's', 's', 's', 's', 's',
                    'n', 'n', 'n', 'n', 'n'
                    'l', 'l', 'l', 'l', 'l'
                    'r', 'r', 'r', 'r', 'r', 'r',
                    'u', 'u', 'u', 'u', 'u', 'u',
                    't', 't', 't', 't', 't',
                    'd', 'd', 'd', 'd', 'd', 'd',
                    'g', 'g'
                    'c', 'c', 'c', 'c',
                    'b', 'b',
                    'm', 'm',
                    'p', 'p',
                    'h', 'h',
                    'f',
                    'v',
                    'y',
                    'ch',
                    'q',
                    'j',
                    'll',
                    'ñ',
                    'rr',
                    'x',
                    'z']
        self.assertEqual([tile.letter for tile in t_b.tiles], expected)

    def test_add_tile(self):
        new_tile = Tile('z')
        self.bag.add_tile(new_tile)
        self.assertIn(new_tile, self.bag.tiles)

    def test_draw_tile(self):
        drawn_tile = self.bag.draw_tile(7)
        self.assertNotIn(drawn_tile, self.bag.tiles)
