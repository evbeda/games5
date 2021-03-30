from ..score import Score
from ..spot import Spot
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
                (0, 'c'),
            ],
            'a',
            1,
        ),
    ])
    def test_multiply_score(self, spot_values, word, expected):
        spots = [Spot(m_value, m_type) for m_value, m_type in spot_values]
        score = Score.multiply_score(spots, word)
        self.assertEqual(score, expected)
