from ..score import Score
from ..spot import Spot
import unittest


class TestScore(unittest.TestCase):

    # def test_score_word(self):
    #     pass

    # def test_search_horiz_word(self):
    #     pass

    # def test_search_vert_word(self):
    #     pass

    def test_multiply_score(self):
        spots = [Spot(0, 'c')]
        word = 'a'
        score = Score.multiply_score(spots, word)
        self.assertEqual(score, 1)
