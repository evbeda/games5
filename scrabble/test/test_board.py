import unittest
from game.board import Board


class TestBoard(unittest.TestCase):
    def test_board(self):
        board = Board()
        self.assertEqual(len(board.spots), 15,)
