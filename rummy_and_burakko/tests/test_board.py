import unittest
from unittest.mock import patch
from ..board import Board
from ..set_tiles import SetTiles
from ..tile import Tile
from parameterized import parameterized


class TestBoard(unittest.TestCase):
    @patch('rummy_and_burakko.game.Tile', create=True)
    @patch.object(Board, 'validate_sets', return_value=True)
    def test_add_new_play(self, mock_validate_sets, tile_patched):
        board = Board()
        set_one = SetTiles([Tile('r', 5), Tile('r', 6), Tile('r', 7)], 1)
        set_two = SetTiles([Tile('b', 5), Tile('b', 6), Tile('b', 7)], 2)
        board.add_new_play([set_one, set_two])

        self.assertIn(set_one, board.sets)
        self.assertIn(set_two, board.sets)

    @parameterized.expand([
        (
            [SetTiles([Tile('red', 5), Tile('red', 6), Tile('red', 8)], 1),
                SetTiles([Tile('blue', 5), Tile('blue', 6), Tile('blue', 7)], 2)],
            False
        ),
        (
            [SetTiles([Tile('red', 5), Tile('red', 6), Tile('blue', 7)], 1),
                SetTiles([Tile('blue', 5), Tile('blue', 6), Tile('blue', 7)], 2)],
            False
        ),
    ])
    def test_validate_sets(self, sets, expected):
        board = Board()
        
        with patch.object(SetTiles, 'is_valid', return_value=expected)
            board.validate_sets(sets)
        
        self.assertEqual(board.add_new_play(sets), expected)

    @patch.object(Board, 'validate_sets', return_value=True)
    def test_use_tiles_in_board(self, board_patched):
        board = Board()

        with patch('rummy_and_burakko.game.Tile', create=True):
            (t1, t2, t3, t4, t5, t6) = [Tile('*', 0) for _ in range(6)]
            [t.assign_set_id(1) for t in (t1, t2, t3, t4)]
            set_1 = SetTiles([t1, t2, t3, t4], 1),
            board.sets = [set_1]
            set_2 = SetTiles([t2, t5, t6], 2)
            board.add_new_play([set_2])
        
        self.assertIn(set_2, board.sets)
        self.assertNotIn(set_1, board.sets)
