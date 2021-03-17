import unittest
from .score_pad import ScorePad


class TestScorePad(unittest.TestCase):
    def setUp(self):
        self.scorepad = ScorePad()

    def test_add_penalty(self):
        self.assertEqual(self.scorepad.add_penalty(), 1)

    # def test_calculate_score(self):
    #     self.assertEqual(ScorePad.calculate_score(), 38)

    # def test_calculate_row(self):
    #     raise NotImplementedError

    def test_max_penalty(self):
        for _ in range(3):
            self.scorepad.add_penalty()

        self.assertTrue(self.scorepad.add_penalty())

    def test_create_rows(self):
        scrpad = ScorePad()
        expected = (
            ('red', (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)),
            ('yellow', (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)),
            ('blue', (12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2)),
            ('green', (12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2)),
            )
        for i, row in enumerate(scrpad.create_rows()):
            self.assertEqual(row.color, expected[i][0])
            self.assertEqual(row.numbers, expected[i][1])
