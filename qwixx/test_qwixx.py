import unittest
from unittest.mock import Mock
from unittest.mock import patch
from .qwixx import Qwixx
from .set_dices import SetDices
from .score_pad import ScorePad


class TestQwixx(unittest.TestCase):
    def setUp(self):
        self.qwixx = Qwixx()

    def test_remove_dice_from_set(self):
        self.qwixx.dice_set = []

        colors = [
            'white',
            'white',
            'red',
            'yellow',
            'green',
            'blue',
        ]

        for color in colors:
            dice = Mock()
            dice.color = color
            self.qwixx.dice_set.append(dice)

        self.qwixx.remove_dice('blue')
        self.assertNotIn('blue', [dice.color for dice in self.qwixx.dice_set])

    def test_new_game_player_count(self):
        qwixx = Qwixx()
        qwixx.create_scored_pad(2)
        self.assertEqual(len(qwixx.score_pad), 2)

    def test_new_game_player_limit(self):
        with self.assertRaises(Exception):
            Qwixx(5)

    @patch.object(ScorePad, 'mark_number_in_row')
    @patch.object(SetDices, 'get_value_of_die', return_value=2)
    def test_mark_with_white(self, mock_value_of_die, mock_mark_number):
        self.qwixx.score_pad = [ScorePad()]
        self.qwixx.mark_with_white('red')
        mock_mark_number.assert_called_once_with(4, 'red')
