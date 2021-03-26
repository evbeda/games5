import unittest
from unittest.mock import Mock
from unittest.mock import patch
from parameterized import parameterized
from .qwixx import Qwixx
from .set_dices import SetDices
from .score_pad import ScorePad
from .row import Row


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

    @patch.object(Qwixx, "create_scored_pad")
    @patch.object(SetDices, "roll_dices")
    def test_play_players(self, mock_roll, mock_create):
        self.qwixx.play_players(5)
        mock_create.assert_called_once_with(5)
        mock_roll.assert_called_once_with()

    @parameterized.expand([
        ('white',  'Choose in which row you want to mark the common dice (0/3) or not (99)?'),
        ('color', 'Choose in which row you want to mark acommon die with a colored die (0/3),common die (0/1) andcolor die(0/3) or Penalty (99/99)?',),
        ])
    def test_next_turn_query(self, state, expected):
        self.qwixx.game_state = state
        self.assertEqual(self.qwixx.next_turn_query(), expected)

    @parameterized.expand([
       (2, 0, 361),
       (4, 3, 361),
        ])
    def test_board(self, cant_score_pad, id_player, cant_letter):
        qwixx = Qwixx()
        qwixx.create_scored_pad(cant_score_pad)
        qwixx.current_player = id_player
        print(qwixx.board)
        self.assertEqual(len(qwixx.board), cant_letter)
 
    @parameterized.expand([
       (Row('rojo'), 'green', 'not loked'),
       (Row('rojo'), 'rojo', 'is loked'),
    ])
    def test_is_locked(self, row, color_row, expected):
        row.blocked_rows.append(color_row)
        self.qwixx.is_locked(row)
        self.assertEqual(self.qwixx.is_locked(row), expected)

    @parameterized.expand([
       (Row('rojo'), 52),
       (Row('blue'), 53),
    ])
    def test_output_row(self, row, expected):
        self.assertEqual(len(self.qwixx.output_row(row)), expected)