import unittest
from unittest.mock import patch
from .player import Player
from .score_pad import ScorePad
# from .score_pad import ScorePad


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.t_player = Player()

    # def test_constructor(self):
        # self.assertEqual(self.t_player.name, 'Test_name')

    def test_pass_turn(self):
        # data
        self.t_player.score_pad.penalty = 2
        # process
        x = self.t_player.pass_turn()
        # assert
        self.assertEqual(self.t_player.score_pad.penalty, 3)
        self.assertEqual(x, 3)

        # process
        x = self.t_player.pass_turn()
        # assert
        self.assertEqual(self.t_player.score_pad.penalty, 4)
        self.assertEqual(x, True)

    @patch.object(ScorePad, 'mark_number_in_row')
    def test_mark_number_mocked(self, mock_mark_number_in_row):
        # process
        num = 10
        self.t_player.mark_number(num, 'red')
        mock_mark_number_in_row.assert_called_once_with(num, 'red')
