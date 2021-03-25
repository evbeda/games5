import unittest
from unittest.mock import patch
from .set_dices import SetDices


class TestSetDices(unittest.TestCase):
    def setUp(self):
        self.t_set_dices = SetDices()

    @patch('random.randint', return_value=3)
    def test_roll_dices(self, random_mock):
        # data
        values_test = {
            'white_1': 3,
            'white_2': 3,
            'red': 3,
            'yellow': 3,
            'blue': 3,
            'green': 3
        }
        # process
        values = {}
        self.t_set_dices.roll_dices()
        for die in self.t_set_dices.dices:
            values[die.color] = die.value
        # assert
        self.assertEqual(random_mock.call_count, 6)
        self.assertEqual(len(values), 6)
        self.assertEqual(values, values_test)
