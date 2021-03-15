import unittest
from unittest.mock import patch
from set_tiles import SetTiles
from tile import Tile
from parameterized import parameterized


class TestSetTiles(unittest.TestCase):
    # Procedure test
    @patch.object(SetTiles, 'is_a_leg', return_value=True)   # 2 argument
    @patch.object(SetTiles, 'is_a_stair', return_value=False)  # 1 argument
    def test_valid_T_F(self, mock_stair, mock_leg):
        tiles_leg = SetTiles([])
        valid_leg = tiles_leg.is_valid()

        # assert
        self.assertTrue(valid_leg)
        mock_leg.assert_called_once_with()
        mock_stair.assert_not_called()

    # Procedure test
    @patch.object(SetTiles, 'is_a_leg', return_value=False)   # 2 argument
    @patch.object(SetTiles, 'is_a_stair', return_value=True)  # 1 argument
    def test_valid_F_T(self, mock_stair, mock_leg):
        tiles_leg = SetTiles([])
        valid_leg = tiles_leg.is_valid()

        # assert
        self.assertTrue(valid_leg)
        mock_leg.assert_called_once_with()
        mock_stair.assert_called_once_with()

    @patch.object(SetTiles, 'is_a_leg', return_value=False)
    @patch.object(SetTiles, 'is_a_stair', return_value=False)
    def test_valid_F_F(self, mock_stair, mock_leg):
        tiles_not_set = SetTiles([])
        valid_set = tiles_not_set.is_valid()

        # assert
        self.assertFalse(valid_set)
        mock_leg.assert_called_once_with()
        mock_stair.assert_called_once_with()

    @parameterized.expand([
        (True, (('red', 5), ('blue', 5), ('green', 5))),
        (False, (('red', 5), ('blue', 6), ('green', 5))),
        (False, (('red', 5), ('blue', 5), ('blue', 5))),
        (True, (('*', 0), ('blue', 5), ('green', 5))),
        (False, (('*', 0), ('blue', 5), ('green', 5), ('*', 0))),
    ])
    def test_is_a_leg(self, expected, tiles):
        # set variables
        tiles_leg = SetTiles([Tile(t[0], t[1]) for t in tiles])
        result = tiles_leg.is_a_leg()
        
        # assert
        self.assertEqual(result, expected)
