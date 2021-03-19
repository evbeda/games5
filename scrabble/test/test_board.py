import unittest
from ..game.board import Board
from parameterized import parameterized
from unittest.mock import patch


class TestBoard(unittest.TestCase):
    def test_board(self):
        b = Board()
        self.assertEqual(len(b.spots), 15)
        self.assertEqual(len(b.spots[0]), 15)

    @patch.object(Board,'multiplier',return_value = (0,'c'))
    def test_set_spots(self, multiplier_mock):
        b = Board()
        self.assertEqual(multiplier_mock.call_count, 225)

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

    def test_board_format(self):
        expected_board = '''- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|3xW|   |   |2xL|   |   |   |3xW|   |   |   |2xL|   |   |3xW|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|   |2xW|   |   |   |3xL|   |   |   |3xL|   |   |   |2xW|   |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|   |   |2xW|   |   |   |2xL|   |2xL|   |   |   |2xW|   |   |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|2xL|   |   |2xW|   |   |   |2xL|   |   |   |2xW|   |   |2xL|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|   |   |   |   |2xW|   |   |   |   |   |2xW|   |   |   |   |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|   |3xL|   |   |   |3xL|   |   |   |3xL|   |   |   |3xL|   |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|   |   |2xL|   |   |   |2xL|   |2xL|   |   |   |2xL|   |   |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|3xW|   |   |2xL|   |   |   | + |   |   |   |2xL|   |   |3xW|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|   |   |2xL|   |   |   |2xL|   |2xL|   |   |   |2xL|   |   |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|   |3xL|   |   |   |3xL|   |   |   |3xL|   |   |   |3xL|   |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|   |   |   |   |2xW|   |   |   |   |   |2xW|   |   |   |   |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|2xL|   |   |2xW|   |   |   |2xL|   |   |   |2xW|   |   |2xL|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|   |   |2xW|   |   |   |2xL|   |2xL|   |   |   |2xW|   |   |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|   |2xW|   |   |   |3xL|   |   |   |3xL|   |   |   |2xW|   |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|3xW|   |   |2xL|   |   |   |3xW|   |   |   |2xL|   |   |3xW|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'''