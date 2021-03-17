import unittest
# from unittest.mock import patch
from .player import Player
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

    def test_mark_number(self):
        # data
        # rows[0] es la row roja, seria mas facil si rows fuera un diccionario
        self.t_player.score_pad.rows[0].marks = [2, 3, 7]
        # process
        self.t_player.mark_number(10, 'red')
        # aseert
        self.assertEqual(self.t_player.score_pad.rows[0].marks, [2, 3, 7, 10])
        self.assertEqual(self.t_player.score_pad.rows[0].color, 'red')
