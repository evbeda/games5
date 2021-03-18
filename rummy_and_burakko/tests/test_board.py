import unittest
from unittest.mock import patch
from ..board import Board
from ..set_tiles import SetTiles
from parameterized import parameterized


class TestBoard(unittest.TestCase):
    @patch.object(Board, 'validate_sets', return_value=True)
    def test_add_new_play(self, mock_validate_sets):
        board = Board()
        set_one = SetTiles([('red', 5), ('red', 6), ('red', 7)], 1)
        set_two = SetTiles([('blue', 5), ('blue', 6), ('blue', 7)], 2)
        board.add_new_play([set_one, set_two])

        self.assertEqual(board.sets[0], set_one)
        self.assertEqual(board.sets[1], set_two)

    @parameterized.expand([
        (
            [SetTiles([('red', 5), ('red', 6), ('red', 8)], 1),
                SetTiles([('blue', 5), ('blue', 6), ('blue', 7)], 2)],
            False
        ),
        (
            [SetTiles([('red', 5), ('red', 6), ('blue', 7)], 1),
                SetTiles([('blue', 5), ('blue', 6), ('blue', 7)], 2)],
            True
        ),
    ])
    def test_validate_sets(self, sets, expected):
        board = Board()
        
        with patch.object(SetTiles, 'is_valid', return_value=expected)
            board.validate_sets(sets)
        
        self.assertEqual(board.add_new_play(sets), expected)
