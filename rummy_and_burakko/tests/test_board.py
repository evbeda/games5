import unittest
from ..board import Board
from ..set_tiles import SetTiles


class TestBoard(unittest.TestCase):
    def test_add_new_play(self):
        board = Board()
        set_one = SetTiles([('red', 5), ('red', 6), ('red', 7)], 1)
        set_two = SetTiles([('blue', 5), ('blue', 6), ('blue', 7)], 2)
        sets = []
        sets.append(set_one)
        sets.append(set_two)
        board.add_new_play(sets)

        self.assertEqual(board.sets[0], set_one)
        self.assertEqual(board.sets[1], set_two)
