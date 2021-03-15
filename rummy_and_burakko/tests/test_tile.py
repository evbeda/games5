import unittest
from tile import Tile
from parameterized import parameterized


class TestTiles(unittest.TestCase):
    @parameterized.expand([
        # color, number, is_jocker, expected
        ('red', 5, False,),  # Color case
        ('yellow', 3, False,),  # Number case
        ('*', 0, True,),  # Jocker case
    ])
    #  Test de resultado o de procedimiento?
    def test_create_tile(self, color, number, is_jocker):
        # seteo
        example_tile = Tile(color, number, is_jocker)
        # assert
        self.assertEqual(example_tile.color, color)
        self.assertEqual(example_tile.number, number)
        self.assertEqual(example_tile.is_jocker, is_jocker)


if __name__ == '__main__':
    unittest.main()
