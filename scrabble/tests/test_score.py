from ..score import Score
from ..spot import Spot
from ..tile import Tile
from ..board import Board
import unittest
from parameterized import parameterized
from unittest.mock import patch


class TestScore(unittest.TestCase):

    def setUp(self):
        self.b = Board()

    @parameterized.expand([
        (
            [
                (1, 'c', False),
            ],
            'a',
            1,
        ),
        (
            [
                (1, 'c', False),
                (1, 'c', False),
                (1, 'c', False),
                (2, 'l', True),
            ],
            'hola',
            8,
        ),
        (
            [
                (1, 'c', False),
                (1, 'c', False),
                (1, 'c', False),
                (2, 'w', True),
            ],
            'hola',
            14,
        ),
        (
            [
                (1, 'c', False),
                (1, 'c', False),
                (1, 'c', False),
                (2, 'w', False),
            ],
            'hola',
            7,
        ),
        (
            [
                (1, 'c', True),
                (1, 'c', False),
                (1, 'c', False),
                (2, 'w', False),
            ],
            'hola',
            7,
        ),
    ])
    def test_multiply_score(self, spot_values, word, expected):
        spots = []
        for m_value, m_type, m_not_used in spot_values:
            spot = Spot(m_value, m_type)
            spot.mult_not_used = m_not_used
            spots.append(spot)

        for spot, letter in zip(spots, word):
            spot.set_tile(Tile(letter))

        score = Score.multiply_score(spots)
        self.assertEqual(score, expected)

        for spot in spots:
            self.assertEqual(spot.mult_not_used, False)

    @parameterized.expand([
        ('hola', 6, 7),
    ])
    @patch.object(Score, 'search_horiz_word')
    def test_search_horiz_letter(self, word, row, col, mock_search_horiz_word):
        self.b.spots[6][7].set_tile(Tile('h'))
        self.b.spots[7][7].set_tile(Tile('o'))
        self.b.spots[8][7].set_tile(Tile('l'))
        self.b.spots[9][7].set_tile(Tile('a'))
        self.b.spots[7][6].set_tile(Tile('r'))
        Score.search_horiz_letter(word, row, col, self.b.spots)
        mock_search_horiz_word.assert_called()

    @parameterized.expand([
        ('hola', 6, 7),
    ])
    @patch.object(Score, 'search_vert_word')
    def test_search_vert_letter(self, word, row, col, mock_search_vert_word):
        self.b.spots[6][7].set_tile(Tile('h'))
        self.b.spots[6][8].set_tile(Tile('o'))
        self.b.spots[6][9].set_tile(Tile('l'))
        self.b.spots[6][10].set_tile(Tile('a'))
        self.b.spots[5][7].set_tile(Tile('r'))
        Score.search_vert_letter(word, row, col, self.b.spots)
        mock_search_vert_word.assert_called()

    @parameterized.expand([
        (7, 6, 'roca'),
    ])
    def test_search_horiz_word(self, row, col, expected_word):
        self.b.spots[7][6].set_tile(None)
        self.b.spots[7][6].set_tile(Tile('r'))
        self.b.spots[7][7].set_tile(Tile('o'))
        self.b.spots[7][8].set_tile(Tile('c'))
        self.b.spots[7][9].set_tile(Tile('a'))
        self.b.spots[7][6].set_tile(None)
        expected = []
        for letter in expected_word:
            spot = Spot(1, 'c')
            spot.set_tile(Tile(letter))
            expected.append(spot)
        self.assertEqual(Score.search_horiz_word(row, col, self.b.spots), expected)

    @parameterized.expand([
        (7, 6, 'roca'),
    ])
    def test_search_vert_word(self, row, col, expected_word):
        self.b.spots[5][7].set_tile(Tile('r'))
        self.b.spots[6][7].set_tile(Tile('r'))
        self.b.spots[7][7].set_tile(Tile('c'))
        self.b.spots[8][7].set_tile(Tile('a'))
        expected = []
        for letter in expected_word:
            spot = Spot(1, 'c')
            spot.set_tile(Tile(letter))
            expected.append(spot)
        self.assertEqual(Score.search_vert_word(row, col, self.b.spots), expected)
