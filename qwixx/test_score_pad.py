import unittest
from parameterized import parameterized
from unittest.mock import patch
from .score_pad import ScorePad
from .row import Row


class TestScorePad(unittest.TestCase):
    def setUp(self):
        self.score_pad = ScorePad()

    def test_add_penalty(self):
        self.assertEqual(self.score_pad.add_penalty(), 1)

    def test_max_penalty(self):
        for _ in range(3):
            self.score_pad.add_penalty()

        self.assertTrue(self.score_pad.add_penalty())

    def test_create_rows(self):
        scrpad = ScorePad()
        expected = (
            ('red', (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)),
            ('yellow', (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)),
            ('blue', (12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2)),
            ('green', (12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2)),
        )
        for i, row in enumerate(scrpad.create_rows()):
            self.assertEqual(row, expected[i][0])
            # self.assertEqual(row.numbers, expected[i][1])

    @parameterized.expand([
        ([2, 3, 5, 8, 10, 11], 3, 69),
    ])
    def test_calculate_score(self, marks, penalty, expected):
        for row in self.score_pad.rows.values():
            row.marks = marks
        self.score_pad.penalty = penalty
        result = self.score_pad.calculate_score()
        self.assertEqual(result, expected)

    @patch.object(Row, 'set_mark')
    def test_mark_number_in_row(self, mock_set_mark):
        # data
        self.score_pad.rows['red'].marks = [2, 3, 7]
        # process
        num = 10
        self.score_pad.mark_number_in_row(num, 'red')
        mock_set_mark.assert_called_once_with(num)

    def test_pass_turn(self):
        # data
        self.score_pad.penalty = 2
        # process
        x = self.score_pad.pass_turn()
        # assert
        self.assertEqual(self.score_pad.penalty, 3)
        self.assertEqual(x, 3)

        # process
        x = self.score_pad.pass_turn()
        # assert
        self.assertEqual(self.score_pad.penalty, 4)
        self.assertEqual(x, True)

    @patch.object(ScorePad, 'mark_number_in_row')
    def test_mark_number_mocked(self, mock_mark_number_in_row):
        # process
        num = 10
        self.score_pad.mark_number(num, 'red')
        mock_mark_number_in_row.assert_called_once_with(num, 'red')
