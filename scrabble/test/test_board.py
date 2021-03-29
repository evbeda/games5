import unittest
from ..game.board import Board
from ..game.spot import Spot
from ..game.tile import Tile
from parameterized import parameterized
from unittest.mock import patch


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.b = Board()
    
    def test_board(self):
        self.assertEqual(len(self.b.spots), 15)
        self.assertEqual(len(self.b.spots[0]), 15)

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
        self.assertEqual(self.b.multiplier(row, col), expected)

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

        self.assertEqual(self.b.get_board(), expected_board)

    @parameterized.expand([
        ('hola', 7, 5, True, True),
        ('hola', 5, 7, False, True),
        ('hola', 5, 2, False, False),
        ('hola', 11, 4, True, False),
    ])
    def test_can_place_first_word(
        self, word, row, col, direction, expected
    ):
        result = self.b.can_place_first_word(word, row, col, direction)

        self.assertEqual(result, expected)

    @parameterized.expand([
        ('sol', 0, 0, True, True),
        ('pala', 4, 7, False, True),
        ('sol', 6, 5, False, True),
        ('sol', 7, 5, False, False),
        ('martillo', 7, 2, True, False),
    ])
    def test_can_place_word(self, word, row, col, direction, expected):
        word_tile = self.b.word_to_tile('hola')
        self.b.place_letters(word_tile, 7, 4, True, [0, 1, 2, 3])

        self.assertEqual(self.b.can_place_word(word, row, col, direction), expected)

    def test_place_letters(self):  # , word, row, col, direction):
        word = self.b.word_to_tile('hola')
        row = 4
        col = 8
        direction = True
        self.b.place_letters(word, row, col, direction, range(len(word)))

        for i in range(len(word)):
            if direction:
                self.assertEqual(self.b.spots[row][col+i].tile, word[i])
            else:
                self.assertEqual(self.b.spots[row+i][col].tile, word[i])

    def test_word_to_tile(self):
        word = 'hola'
        word_tile = self.b.word_to_tile(word)
        for i, wt in enumerate(word_tile):
            self.assertEqual(wt.letter, word[i])

    @parameterized.expand([
        (4, 7, 4, True, ['b', 'a', 'r', 'c']),
        (4, 7, 3, True, [None, 'b', 'a', 'r']),
        (4, 7, 8, True, ['o', None, None, None]),
        (4, 0, 0, False, [None, None, None, None]),
    ])
    def test_get_spots_to_place_word(self, len_word, row, col, dire, expected):
        word_tile = self.b.word_to_tile('barco')
        self.b.place_letters(word_tile, 7, 4, True, range(len(word_tile)))
            
        spots_word = self.b.get_spots_to_place_word(len_word, row, col, dire)

        for sfw, exp in zip(spots_word, expected):
            if sfw.tile:
                self.assertEqual(sfw.tile.letter, exp)
            else:
                self.assertEqual(sfw.tile, exp)

    @parameterized.expand([
        ([None, Tile('p'), None], [(1, 'p')],),
        # ([None, Tile('p'), None], ['p'],),
        # ([None, Tile('a'), Tile('c')], ['a', 'c'],),
        # ([None, None, None, None], [],),
    ])
    def test_tiles_in_board(self, tiles, expected):
        spots = []
        for t in tiles:
            spot = Spot(0, 'c')
            if t:
                spot.set_tile(t)
            spots.append(spot)

        spots_with_tile = self.b.tiles_in_board(spots)
        for swt, exp in zip(spots_with_tile, expected):
            self.assertEqual(swt, exp)

    @parameterized.expand([
        ('casa', [(1, 'a'), (2, 's')], [(0, 'c'), (3, 'a')]),
        ('casa', [], [(0, 'c'), (1, 'a'), (2, 's'), (3, 'a')]),
        ('casa', [(0, 'c'), (1, 'a'), (2, 's'), (3, 'a')], []),
    ])
    def test_tiles_diff(self, word, letters_in_board, expected):
        self.assertEqual(self.b.tiles_diff(word, letters_in_board), expected)
