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

    @patch.object(Game, "distribute_tiles")
    @patch.object(Game, "random_order")
    @patch.object(Game, "create_players")
    def test_play_players_input(self, m_init, m_order, m_distribute):
        # data
        players = ["test_1", "test_2", "test_3"]
        # process
        self.rummy.play_players_input(players)
        # assert
        m_init.assert_called_once_with(players)
        m_order.assert_called_once_with()
        m_distribute.assert_called_once_with()

    @parameterized.expand([
        # (game_state, expected)
        ('start_game', 'Enter number of players'),
        ('new_set_q', 'Enter quantity of tiles to play'),
        ('end_turn', 'Turn Ended'),
    ])
    def test_next_turn_query(self, game_state, expected):
        # process
        self.rummy.game_state = game_state
        result = self.rummy.next_turn_query()
        # assert
        self.assertEqual(result, expected)

    @parameterized.expand([
        # (option, game_state)
        (0, 'select_option'),
        (1, 'new_set_q'),
        (4, 'end_turn'),
        (5, 'select_option'),
    ])
    def test_play_select_option(self, option, game_state):
        # data
        self.rummy.game_state = 'select_option'
        # process
        self.rummy.play_select_option(option)
        # assert
        self.assertEqual(self.rummy.game_state, game_state)

    # def test_play_new_set_q(self):
    #     self.input_q_tiles = quantity
    #     self.game_state = GAME_STATE_NEW_SET_TILES

    # def test_play_make_move(self:
    #     self.game.make_play(self.option, moves)
    #     self.game_state = GAME_STATE_SELECT_OPTION

    @parameterized.expand([
        # (game_state)
        ('start_game', (1, 0)),
        ('players_input', (0, 1)),
    ])
    @patch.object(RummyAndBurakko, 'play_players_input')
    @patch.object(RummyAndBurakko, 'play_start_game')
    def test_play(self, game_state, call_count, mock_start, mock_players):
        # data
        args = [1, 2, 3, 4]
        self.rummy.game_state = game_state
        # process
        self.rummy.play(args)
        # assert
        self.assertEqual(mock_start.call_count, call_count[0])
        self.assertEqual(mock_players.call_count, call_count[1])
