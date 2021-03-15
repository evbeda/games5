import unittest
from unittest.mock import patch
from set_tiles import SetTiles


class TestSetTiles(unittest.TestCase):
    # Procedure test
    @patch('set_tiles.SetTiles.is_a_leg')   # 2 argument
    @patch('set_tiles.SetTiles.is_a_stair')  # 1 argument
    def test_valid_T_F(self, mock_stair, mock_leg):
        assert SetTiles.is_a_stair is mock_stair
        assert SetTiles.is_a_leg is mock_leg
        # seteo
        mock_leg.return_value = True
        mock_stair.return_value = False

        tiles_leg = SetTiles()
        valid_leg = tiles_leg.is_valid()

        # assert
        self.assertTrue(valid_leg)
        mock_leg.assert_called_once_with()
        mock_stair.assert_not_called()

    # Procedure test
    @patch('set_tiles.SetTiles.is_a_leg')   # 2 argument
    @patch('set_tiles.SetTiles.is_a_stair')  # 1 argument
    def test_valid_F_T(self, mock_stair, mock_leg):
        # seteo
        mock_leg.return_value = False
        mock_stair.return_value = True

        tiles_leg = SetTiles()
        valid_leg = tiles_leg.is_valid()

        # assert
        self.assertTrue(valid_leg)
        mock_leg.assert_called_once_with()
        mock_stair.assert_called_once_with()


