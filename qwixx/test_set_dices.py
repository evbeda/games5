import unittest
from unittest.mock import patch
from .set_dices import SetDices


class TestSetDices(unittest.TestCase):
    def setUp(self):
        self.t_set_dices = SetDices()

    @patch('random.randint')
    def test_roll_dices(self, random_mock):
        # process
        values = self.t_set_dices.roll_dices()

        # assert
        self.assertEqual(random_mock.call_count, 6)
