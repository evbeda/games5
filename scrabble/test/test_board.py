import unittest
from ..game.board import Board
from parameterized import parameterized


class TestBoard(unittest.TestCase):
    def test_board(self):
        board = Board()
        self.assertEqual(len(board.spots), 15)
        self.assertEqual(len(board.spots[0]), 15)

    @parameterized.expand([
        (0, 1, (0,'c')),    # common spot
        (0, 11, (2,'l')),   # spot with mult x2 letter
        (9, 5, (3,'l')),    # spot with mult x3 letter
        (7, 7, (2,'w')),    # spot with mult x2 word
        (14, 0, (3,'w')),    # spot with mult x3 word
    ])
    def test_multiplier(self, x, y, expected):
        s = Board()
        self.assertEqual(s.multiplier(x,y), expected)
