import unittest
from unittest.mock import Mock
from unittest.mock import patch
from parameterized import parameterized
from ..qwixx import (
    Qwixx,
    QWIXX_STATE_START,
    QWIXX_STATE_OPTION,
    QWIXX_STATE_PLAY,
    QWIXX_TURN_WHITE,
    QWIXX_TURN_COLOR,
    OPTION_PLAY,
    OPTION_PASS,
)
from ..set_dices import SetDices
from ..score_pad import ScorePad
from ..row import Row


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
            dice_mock = Mock()
            dice_mock.color = color
            self.qwixx.dice_set.append(dice_mock)

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
        self.qwixx.mark_with_white(1)
        mock_mark_number.assert_called_once_with(4, 'red')

    @patch.object(Qwixx, "create_scored_pad")
    @patch.object(SetDices, "roll_dices")
    def test_play_players(self, mock_roll, mock_create):
        self.qwixx.play_start(5)
        mock_create.assert_called_once_with(5)
        mock_roll.assert_called_once_with()

    @parameterized.expand([
        (QWIXX_STATE_START, 'Enter number of players',),
        (QWIXX_STATE_OPTION, 'Game option :\n1) play \n2) pass',),
    ])
    def test_next_turn(self, state, expected):
        self.qwixx.game_state = state
        self.assertEqual(self.qwixx.next_turn(), expected)

    @parameterized.expand([
        (QWIXX_TURN_WHITE, 'Choose in which row you want to mark the common dice (1): red, 2): yellow, 3): blue, 4): green) or pass ?',),
        (QWIXX_TURN_COLOR, 'Choose in which row you want to mark acommon die with a colored die (0/3),common die (0/1) andcolor die(0/3) or Penalty (99/99)?',),
    ])
    def test_next_turn_play(self, turn_color, expected):
        self.qwixx.game_state = QWIXX_STATE_PLAY
        self.qwixx.turn_color = turn_color
        self.assertEqual(self.qwixx.next_turn(), expected)

    @parameterized.expand([
        (2, 0, 5, 451),
        (4, 3, 5, 451),
    ])
    def test_board(self, cant_score_pad, id_player, marks, cant_letter):
        qwixx = Qwixx()
        qwixx.create_scored_pad(cant_score_pad)
        qwixx.current_player = id_player
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
        (Row('rojo'), 54),
        (Row('blue'), 55),
    ])
    def test_output_row(self, row, expected):
        self.assertEqual(len(self.qwixx.output_row(row)), expected)

    @patch.object(Qwixx, 'play_start')
    def test_play_start(self, patched_play_start):
        self.qwixx.game_state = QWIXX_STATE_START
        self.qwixx.play(4)
        patched_play_start.assert_called_once_with(4)

    @patch.object(Qwixx, 'play_option')
    def test_play_option_(self, patched_play_option):
        self.qwixx.game_state = QWIXX_STATE_OPTION
        self.qwixx.play(OPTION_PLAY)
        patched_play_option.assert_called_once_with(OPTION_PLAY)

    @parameterized.expand([
        (OPTION_PLAY, 0, 0, QWIXX_STATE_PLAY,),
        (OPTION_PASS, 0, 1, QWIXX_STATE_OPTION,),
        (OPTION_PASS, 3, 0, QWIXX_STATE_OPTION,),
    ])
    def test_play_option_play(
        self,
        selected_option,
        current_player,
        expected_current_player,
        expected_game_state,
    ):
        self.qwixx.play_start(4)
        self.qwixx.current_player = current_player
        self.qwixx.play_option(selected_option)
        self.assertEqual(
            self.qwixx.game_state,
            expected_game_state,
        )
        self.assertEqual(
            self.qwixx.current_player,
            expected_current_player,
        )

    def test_play_option_pass_with_penalty(self):
        self.qwixx.play_start(4)
        self.qwixx.turn_color = QWIXX_TURN_COLOR
        self.qwixx.play_option(OPTION_PASS)
        self.assertEqual(
            self.qwixx.score_pad[0].penalty,
            1,
        )
        self.assertTrue(self.qwixx.is_playing)

    def test_play_option_pass_with_last_penalty(self):
        self.qwixx.play_start(4)
        self.qwixx.turn_color = QWIXX_TURN_COLOR
        self.qwixx.score_pad[0].penalty = 3
        self.qwixx.play_option(OPTION_PASS)
        self.assertEqual(
            self.qwixx.score_pad[0].penalty,
            4,
        )
        self.assertFalse(self.qwixx.is_playing)

    def test_play_option_pass_without_penalty(self):
        self.qwixx.play_start(4)
        self.qwixx.turn_color = QWIXX_TURN_WHITE
        self.qwixx.play_option(OPTION_PASS)
        self.assertEqual(
            self.qwixx.score_pad[0].penalty,
            0,
        )

    def test_play_option_exception(self):
        self.assertEqual(
            self.qwixx.play_option(3),
            'Invalid Option',
        )

    @parameterized.expand([
        (QWIXX_TURN_WHITE, 1, '',),
        (QWIXX_TURN_COLOR, 1, 1,),
    ])
    @patch.object(Qwixx, 'mark_with_color')
    @patch.object(Qwixx, 'mark_with_white')
    def test_play_play_turn(
        self,
        turn_color,
        dice1,
        dice2,
        patched_mark_with_white,
        patched_mark_with_color,
    ):
        self.qwixx.turn_color = turn_color
        self.qwixx.play_turn(dice1, dice2)
        if self.qwixx.turn_color == QWIXX_TURN_WHITE:
            patched_mark_with_white.assert_called_once_with(dice1)
        else:
            patched_mark_with_color.assert_called_once_with(dice1, dice2)


    @patch.object(Qwixx, 'mark_with_white')
    def test_play_play_color(self, patched_mark_with_white):
        self.qwixx.play_start(4)
        self.qwixx.turn_color = QWIXX_TURN_WHITE
        self.qwixx.play_turn('red')
        patched_mark_with_white.assert_called_once_with('red')

    @parameterized.expand([
        (0, 0, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE,),
        (1, 0, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE,),
        (2, 0, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE,),
        (3, 0, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE, QWIXX_TURN_COLOR,),
        (0, 0, QWIXX_TURN_COLOR, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE,),
        (1, 1, QWIXX_TURN_WHITE, QWIXX_TURN_COLOR, QWIXX_TURN_WHITE,),
        (2, 1, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE,),
        (3, 1, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE,),
        (0, 1, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE, QWIXX_TURN_COLOR,),
        (1, 1, QWIXX_TURN_COLOR, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE,),
    ])
    def test_set_next_player(self, current_player, current_color_player, turn_color, previous_turn_color, expected_next_turn_color):
        self.qwixx.play_start(4)
        self.qwixx.game_state = QWIXX_STATE_PLAY
        self.qwixx.current_player = current_player
        self.qwixx.previous_turn_color = previous_turn_color
        self.qwixx.current_color_player = current_color_player
        self.qwixx.turn_color = turn_color
        self.qwixx.set_next_player()
        self.assertEqual(
            self.qwixx.game_state,
            QWIXX_STATE_OPTION,
        )
        self.assertEqual(
            self.qwixx.current_player,
            (current_player + 1) % 4,
        )
        self.assertEqual(
            self.qwixx.turn_color,
            expected_next_turn_color,
        )

    @parameterized.expand([
        (['blue', 'red'], False),
        (['blue', 'red', 'yellow'], False),
        (['blue'], True),
        ([], True),
    ])
    def test_you_cant_play(self, blocked_row, expected):
        row = Row
        row.blocked_rows.clear()
        row.blocked_rows.extend(blocked_row)
        self.qwixx.you_can_play
        self.assertEqual(self.qwixx.is_playing, expected)

