import unittest
from parameterized import parameterized
from row import Row


class TestRow(unittest.TestCase):
    def test_lock_row(self):
        color_row = "red"
        self.row = Row(color_row)
        self.assertEqual(self.row.lock_Row(), True)

    @parameterized.expand([
        ('red', tuple(range(2,13))),
        ('yellow', tuple(range(2,13))),
        ('blue', tuple(reversed(range(2,13)))),
        ('green', tuple(reversed(range(2,13)))),
    ])
    def test_contain_values(self, color_row, expected):
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

    # def test_can_mark(self):
    #     r = Row('red')
    #     r.marks = [2, 3, 6]

    #     self.assertTrue(r.can_mark(7))

    @parameterized.expand([
        ('red', [2, 3, 6], 7, True),
        # ('', [2, 3, 6], True),
        # ('red', [2, 3, 6], True),
        # ('red', [2, 3, 6], True),
    ])
    def test_can_mark(self, color, marks, number, expected):
        r = Row(color)
        r.marks = marks

        self.assertEqual(r.can_mark(number), expected)