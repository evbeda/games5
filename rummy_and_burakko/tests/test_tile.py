import unittest
from ..tile import Tile
from parameterized import parameterized


class TestTiles(unittest.TestCase):
    @parameterized.expand([
        # color, number, is_joker, expected
        ('red', 5, False,),  # Color case
        ('yellow', 3, False,),  # Number case
        ('*', 0, True,),  # Joker case
    ])
    def test_create_tile(self, color, number, is_joker):
        # seteo
        example_tile = Tile(color, number)
        # assert
        self.assertEqual(example_tile.color, color)
        self.assertEqual(example_tile.number, number)
        self.assertEqual(example_tile.is_joker, is_joker)

    def test_assign_set_id(self):
        tile = Tile('blue', 2)
        tile.assign_set_id(30)
        self.assertEqual(tile.set_id, 30)
