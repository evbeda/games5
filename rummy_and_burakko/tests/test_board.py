import unittest
from unittest.mock import patch
from ..board import Board
from ..set_tiles import SetTiles
from ..tile import Tile
from parameterized import parameterized


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    @parameterized.expand([
        (
            [
                SetTiles(
                    [Tile('red', 5), Tile('blue', 6), Tile('red', 10)]
                ),
                SetTiles(
                    [Tile('blue', 5), Tile('blue', 6), Tile('blue', 7)]
                ),
            ],
            False
        ),
        (
            [
                SetTiles(
                    [Tile('red', 5), Tile('red', 6), Tile('blue', 7)]
                ),
                SetTiles(
                    [Tile('blue', 5), Tile('blue', 6), Tile('blue', 7)]
                ),
            ],
            False
        ),
        (
            [
                SetTiles([
                    Tile('red', 5),
                    Tile('red', 6),
                    Tile('red', 7)]
                ),
                SetTiles([
                    Tile('blue', 10),
                    Tile('blue', 11),
                    Tile('blue', 12)]
                ),
                SetTiles([
                    Tile('green', 7),
                    Tile('blue', 7),
                    Tile('red', 7),
                    Tile('black', 7)]
                ),
            ],
            True
        ),
    ])
    def test_valid_sets(self, sets, expected):
        # data
        for id, set_tile in enumerate(sets):
            self.board.temp_sets.update({id: set_tile})
        # process
        result = self.board.valid_sets()
        # assert
        self.assertEqual(result, expected)

    def test_board_format(self):
        self.board.temp_sets = {
            1: SetTiles([Tile('r', 5), Tile('b', 5), Tile('y', 5)]),
            2: SetTiles(
                [
                    Tile('r', 3), Tile('b', 3),
                    Tile('y', 3), Tile('w', 3)
                ]
            ),
            3: SetTiles(
                [
                    Tile('r', 3), Tile('r', 4),
                    Tile('r', 5), Tile('r', 6)
                ]
            ),
        }

        board_str = (
            "1: L[ 0:r5 1:b5 2:y5 ]\n"
            "2: L[ 0:r3 1:b3 2:y3 3:w3 ]\n"
            "3: S[ 0:r3 1:r4 2:r5 3:r6 ]"
        )

        self.assertEqual(self.board.get_board(), board_str)

    @parameterized.expand([
        (
            SetTiles(
                [Tile('r', 3), Tile('r', 4), Tile('r', 5), Tile('r', 6)]
            ),
            3,
            Tile('r', 6)
        ),
    ])
    @patch.object(SetTiles, 'extract_one_tile', return_value=Tile('r', 6))
    def test_give_one_tile_from_board(
        self, set_tile, index, chosen_tile, mock
    ):
        self.board.temp_sets = {
            1: set_tile,
        }
        self.board.give_one_tile_from_board(1, index)

        self.assertEqual(self.board.reused_tiles, [chosen_tile])

    @parameterized.expand([
        (SetTiles([Tile('r', 3), Tile('r', 4)]), 3),
        (SetTiles([]), 3),
    ])
    def test_give_one_tile_from_board_fail(self, set_tile, index):
        self.board.sets = {
            1: set_tile,
        }
        with self.assertRaises(Exception):
            self.board.give_one_tile_from_board(1, index)

    def test_get_reused_tiles(self):
        # data
        self.board.reused_tiles = [Tile('r', 3), Tile('r', 4), Tile('r', 5)]
        start_index = 5
        expected = '5:r3   6:r4   7:r5'
        # process
        result = self.board.get_reused_tiles(start_index)
        # assert
        self.assertEqual(result, expected)

    def test_place_new_set(self):
        tiles_array = [Tile('r', 3), Tile('r', 4), Tile('r', 5)]
        expected_sets = {
            1: SetTiles(tiles_array)
        }
        self.board.place_new_set(tiles_array)
        for index in range(len(tiles_array)):
            self.assertEqual(
                self.board.temp_sets[1].tiles[index],
                expected_sets[1].tiles[index]
            )

    def test_get_a_reused_tile(self):
        # data
        self.board.reused_tiles = [Tile('r', 5), Tile('b', 5), Tile('y', 5)]
        index = 1
        expected = Tile('b', 5)
        # process
        result = self.board.get_a_reused_tile(index)
        # assert
        self.assertEqual(result, expected)

    @parameterized.expand([
        # (index, expected)
        (0, [2, 3, 4, 5]),
        (4, [1, 2, 3, 4]),
        (2, [1, 2, 4, 5]),
    ])
    def test_remove_reused_tile(self, index, expected):
        # data
        self.board.reused_tiles = list(range(1, 6))
        # process
        self.board.remove_reused_tile(index)
        # assert
        self.assertEqual(self.board.reused_tiles, expected)

    @parameterized.expand([
        ([1, 2, 3], False),
        ([], True),
        ([1], False),
    ])
    def test_all_reused_tiles(self, lenght, expected):
        self.board.reused_tiles = lenght
        result = self.board.all_reused_tiles()
        self.assertEqual(result, expected)
