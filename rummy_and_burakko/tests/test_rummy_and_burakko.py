import unittest
from unittest.mock import patch
from parameterized import parameterized
from ..rummy_and_burakko import RummyAndBurakko
from ..game import Game


class TestRummyAndBurakko(unittest.TestCase):
    def setUp(self):
        self.rummy = RummyAndBurakko()

    def test_constructor(self):
        pass

    @patch.object(Game, "show_game", return_value="test")
    def test_board(self, mock):
        # data
        players = ["test_1", "test_2", "test_3"]
        # process
        result = self.rummy.board
        self.assertEqual(result, "Starting...")

        self.rummy.game = Game(players)
        result = self.rummy.board
        mock.assert_called_once_with()
        self.assertEqual(mock.return_value, "test")

    @parameterized.expand([
        # (input_players)
        (0, 0, 'start_game'),
        (1, 1, 'players_input'),
    ])
    def test_play_start_game(self, input_players, res_1, res_2):
        self.rummy.play_start_game(input_players)
        self.assertEqual(self.rummy.input_player_args, res_1)
        self.assertEqual(self.rummy.game_state, res_2)

    # @patch.object(Game, "distribute_tiles")
    # @patch.object(Game, "random_order")
    # # @patch.object(Game, "__init__")
    # def test_play_players_input(self, m_order, m_distribute):
    #     # data
    #     players = ["test_1", "test_2", "test_3"]
    #     # process
    #     self.rummy.play_players_input(players)


    #     m_order.assert_called_once_with()
    #     m_distribute.assert_called_once_with()

