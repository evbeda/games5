from ..score import Score
from ..spot import Spot
from ..tile import Tile
import unittest
from parameterized import parameterized


class TestScore(unittest.TestCase):

    # def test_score_word(self):
    #     pass

    # def test_search_horiz_word(self):
    #     pass

    # def test_search_vert_word(self):
    #     pass

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
