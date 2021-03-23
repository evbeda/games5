import unittest
from ..game.board import Board
from ..game.tile import Tile
from parameterized import parameterized
from unittest.mock import patch


class TestBoard(unittest.TestCase):
    def test_board(self):
        b = Board()
        self.assertEqual(len(b.spots), 15)
        self.assertEqual(len(b.spots[0]), 15)

    @patch.object(Board, 'multiplier', return_value=(0, 'c'))
    def test_set_spots(self, multiplier_mock):
        b = Board()
        self.assertEqual(multiplier_mock.call_count, 225)

    @parameterized.expand([
        (0, 1, (0, 'c')),    # common spot
        (0, 11, (2, 'l')),   # spot with mult x2 letter
        (9, 5, (3, 'l')),    # spot with mult x3 letter
        (7, 7, (2, 'w')),    # spot with mult x2 word
        (14, 0, (3, 'w')),    # spot with mult x3 word
    ])
    def test_multiplier(self, row, col, expected):
        s = Board()
        self.assertEqual(s.multiplier(row, col), expected)

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
|3xW|   |   |2xL|   |   |   |2xW|   |   |   |2xL|   |   |3xW|
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

        board = Board()
        self.assertEqual(board.get_board(), expected_board)

    @parameterized.expand([
        ('hola', 7, 5, True, True),
        ('hola', 5, 7, False, True),
        ('hola', 5, 2, False, False),
        ('hola', 11, 4, True, False),
    ])
    def test_can_place_first_word(
        self, word, row, col, direction, expected
    ):
        b = Board()
        result = b.can_place_first_word(word, row, col, direction)

        self.assertEqual(result, expected)

    @parameterized.expand([
        ('sol', 0, 0, True, True),
        ('pala', 4, 7, False, True),
        ('sol', 6, 5, False, True),
        ('sol', 7, 5, False, False),
        ('martillo', 7, 2, True, False),
    ])
    def test_can_place_word(self, word, row, col, direction, expected):
        b = Board()
        t1 = Tile('h')
        t2 = Tile('o')
        t3 = Tile('l')
        t4 = Tile('a')
        b.place_letters([t1, t2, t3, t4], 7, 4, True, [0, 1, 2, 3])

        self.assertEqual(b.can_place_word(word, row, col, direction), expected)

    def test_place_letters(self):  # , word, row, col, direction):
        b = Board()
        t1 = Tile('h')
        t2 = Tile('o')
        t3 = Tile('l')
        t4 = Tile('a')
        word = [t1, t2, t3, t4]
        row = 4
        col = 8
        direction = True
        b.place_letters(word, row, col, direction, range(len(word)))

        for i in range(len(word)):
            if direction:
                self.assertEqual(b.spots[row][col+i].tile, word[i])
            else:
                self.assertEqual(b.spots[row+i][col].tile, word[i])
