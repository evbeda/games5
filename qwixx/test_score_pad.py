import unittest
from score_pad import ScorePad


class TestScorePad(unittest.TestCase):
    def setUp(self):
        self.scorepad = ScorePad()

    def test_add_penalty(self):
        self.assertEqual(self.scorepad.add_penalty(), 1)

    def test_calculate_score(self):
        self.assertEqual(ScorePad.calculate_score(), 38)

    def test_calculate_row(self):
        raise NotImplementedError
