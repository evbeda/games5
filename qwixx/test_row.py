import unittest
from row import Row


class TestRow(unittest.TestCase):
    def setUp(self):
        valuesRow = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        colorRow = "red"
        self.row = Row(valuesRow, colorRow)

    def test_Lock_Row(self):
        self.assertEqual(self.row.lock_Row(), True)

    def test_Contain_Values_Red(self):
        valuesRow = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        colorRow = "red"
        expected = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        row = Row(valuesRow, colorRow)
        self.assertEqual(row.row, expected)

    def test_Contain_Values_Yellow(self):
        valuesRow = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        colorRow = "yellow"
        expected = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        row = Row(valuesRow, colorRow)
        self.assertEqual(row.row, expected)

    def test_Contain_Values_Green(self):
        valuesRow = (12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
        colorRow = "green"
        expected = (12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
        row = Row(valuesRow, colorRow)
        self.assertEqual(row.row, expected)

    def test_Contain_Values_Blue(self):
        valuesRow = (12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
        colorRow = "blue"
        expected = (12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
        row = Row(valuesRow, colorRow)
        self.assertEqual(row.row, expected)

    def test_Upward(self):
        valuesRow = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        colorRow = "yellow"
        expected = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        row = Row(valuesRow, colorRow)
        self.assertEqual(sorted(row.row), expected)

    def test_Falling(self):
        valuesRow = (12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
        colorRow = "blue"
        expected = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        row = Row(valuesRow, colorRow)
        self.assertEqual(sorted(row.row, reverse=True), expected)
