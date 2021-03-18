import unittest
from unittest.mock import patch
from ..board import Board
from ..set_tiles import SetTiles
from ..tile import Tile
from parameterized import parameterized


class TestBoard(unittest.TestCase):
    @patch('rummy_and_burakko.tile.Tile', create=True)
    @patch('rummy_and_burakko.board.SetTiles', create=True)
    @patch.object(Board, 'validate_sets', return_value=True)
    def test_add_new_play(self, mock_validate_sets, set_tile_patched, tile_patched):
        board = Board()
        set_one = [Tile('r', 5), Tile('r', 6), Tile('r', 7)]
        board.add_new_play([set_one])
        set_tile_patched.assert_called_with(set_one)
        self.assertEqual(len(board.sets), 1)

    @parameterized.expand([
        (
            [
                SetTiles([Tile('red', 5), Tile('red', 6), Tile('red', 8)]),
                SetTiles([Tile('blue', 5), Tile('blue', 6), Tile('blue', 7)]),
            ],
            False
        ),
        (
            [
                SetTiles([Tile('red', 5), Tile('red', 6), Tile('blue', 7)]),
                SetTiles([Tile('blue', 5), Tile('blue', 6), Tile('blue', 7)]),
            ],
            False
        ),
    ])
    def test_validate_sets(self, sets, expected):
        board = Board()
        
        with patch.object(SetTiles, 'is_valid', return_value=expected):
            board.validate_sets(sets)

    @patch('rummy_and_burakko.tile.Tile', create=True)
    @patch.object(Board, 'validate_sets', return_value=True)
    def test_remove_reused_tiles(self, board_patched, tiles_patched):
        board = Board()

        (t1, t2, t3, t4, t5, t6) = [Tile('*', 0) for _ in range(6)]
        [t.assign_set_id(1) for t in (t1, t2, t3, t4)]
        
        with patch('rummy_and_burakko.tests.test_board.SetTiles', create=True):
            set_1 = SetTiles([t1, t2, t3, t4])

        board.sets = {1: set_1}
        set_2 = [t2, t5, t6]
        
        with patch.object(SetTiles, 'remove_tile') as remove_tile_patched:
            board.add_new_play([set_2])
            remove_tile_patched.assert_called()

    def test_board_format(self):
        board = Board()
        board.sets = {
            1: SetTiles([Tile('r', 5), Tile('b', 5), Tile('y', 5)]),
            2: SetTiles([Tile('r', 3), Tile('b', 3), Tile('y', 3), Tile('w', 3)]),
            3: SetTiles([Tile('r', 3), Tile('r', 4), Tile('r', 5), Tile('r', 6)]),
        }

        board_str = '1: L[ 0:r5 1:b5 2:y5 ]\n2: L[ 0:r3 1:b3 2:y3 3:w3 ]\n3: S[ 0:r3 1:r4 2:r5 3:r6 ]'

        self.assertEqual(board.get_board(), board_str)
