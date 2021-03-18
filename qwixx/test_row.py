import unittest
from parameterized import parameterized
from .row import Row


class TestRow(unittest.TestCase):
    def test_lock_row(self):
        color_row = "red"
        self.row = Row(color_row)
        self.assertEqual(self.row.lock_Row(), True)

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
        ('red', [2, 3, 6], 7, False, True),
        ('red', [2, 4, 6], 3, False, False),
        ('yellow', [3, 4, 6], 2, False, False),
        ('blue', [6, 5, 4], 3, False, True),
        ('blue', [6, 5, 4], 7, False, False),
        ('green', [7, 5, 4], 6, False, False),
        ('blue', [6, 5, 4], 3, True, False),
        ('red', [2, 3, 6], 7, True, False),
    ])
    def test_can_mark(self, color, marks, number, is_locked, expected):
        r = Row(color)
        r.is_locked = is_locked
        r.marks = marks

        self.assertEqual(r.can_mark(number), expected)


'''
class TestMockCantMarkLockRow(TestCase):
@mock.patch(row.lock_row)
    @parameterized.expand([
            (True, alguien intenta marcar, False),
            (False, alguien intenta, marcar, True),
        ])
    def test_lockrow_notmark(self, mock_response, expected):
        mock_response.return_value = True
        # self.assertEqual(r.can_mark(number), expected)
'''
