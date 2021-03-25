import unittest
from parameterized import parameterized
from .row import Row
from unittest.mock import patch


class TestRow(unittest.TestCase):
    def test_lock_row(self):
        # color_row = "red"
        r = Row('yellow')
        r.blocked_rows = []
        self.assertEqual(r.blocked_rows, [])
        r.lock_Row()
        self.assertEqual(r.blocked_rows, [r.color])

    @parameterized.expand([
        ('red', tuple(range(2, 13))),
        ('yellow', tuple(range(2, 13))),
        ('blue', tuple(reversed(range(2, 13)))),
        ('green', tuple(reversed(range(2, 13)))),
    ])
    def test_correct_row_generation(self, color_row, expected):
        row_example = Row(color_row)
        self.assertEqual(row_example.numbers, expected)

    def test_can_mark_last_more_5(self):
        row_example = Row('red')
        row_example.marks = [2, 3, 4, 5, 6]
        result = row_example.can_mark_last()
        self.assertTrue(result)

    def test_cant_mark_last_less_5(self):
        row_example = Row('red')
        row_example.marks = [3]
        result = row_example.can_mark_last()
        self.assertFalse(result)

    @parameterized.expand([
        ('red', 0, True),
        ('red', 0, False),
    ])
    @patch.object(Row, 'can_mark')
    def test_check_row_lock(self, color, call_count_mock, expected,
                            mock_can_mark):
        r = Row(color)
        r.blocked_rows.append('red')
        r.check_row_lock(5)
        # Como testear el return de la funcion check_row_lock
        self.assertEqual(mock_can_mark.call_count, call_count_mock, expected)

    @parameterized.expand([
        ('red', [2, 3, 6], 7, True),
        ('red', [2, 4, 6], 3, False),
        ('yellow', [3, 4, 6], 2, False),
        ('blue', [6, 5, 4], 3, True),
        ('blue', [6, 5, 4], 7, False),
        ('green', [7, 5, 4], 6, False),
        ('green', [], 6, True),
        ('red', [], 7, True),
    ])
    def test_can_mark(self, color, marks, number, expected):
        r = Row(color)
        r.marks = marks

        self.assertEqual(r.can_mark(number), expected)

    @parameterized.expand([
        ('red', [2, 3, 6], 6),
    ])
    def test_calculate_marks(self, color, marks, expected):
        r = Row(color)
        r.marks = marks
        self.assertEqual(r.calculate_marks(), expected)

    @parameterized.expand([
        ('green', [4], 7, [4]),
        ('yellow', [2], 7, [2, 7]),
    ])
    def test_set_mark(self, color, marks, number, expected):
        r = Row(color)
        r.marks = marks
        r.set_mark(number)
        self.assertEqual((r.marks), expected)
