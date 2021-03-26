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
        # (input_players, assign_input, game_state, input_are_ints)
        (0, 0, 'start_game', True),
        (1, 1, 'players_input', False),
        (4, 4, 'players_input', False),
        (5, 0, 'start_game', True),
    ])
    def test_play_start_game(self, input_players, res_1, res_2, are_ints):
        self.rummy.play_start_game(input_players)
        self.assertEqual(self.rummy.input_player_args, res_1)
        self.assertEqual(self.rummy.game_state, res_2)
        self.assertEqual(self.rummy.input_are_ints, are_ints)

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
        self.assertTrue(self.rummy.input_are_ints)

    @parameterized.expand([
        # (game_state, expected)
        ('start_game', '\nEnter number of players'),
        ('new_set_q', '\nEnter quantity of tiles to play'),
        ('end_turn', '\nTurn Ended'),
    ])
    def test_next_turn_message(self, game_state, expected):
        # process
        self.rummy.game_state = game_state
        result = self.rummy.next_turn()
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

    @parameterized.expand([
        # (quantity, call_count, input_q_tiles)
        (2, 'new_set_q', 5),
        (3, 'new_set_tiles', 3),
        (4, 'new_set_tiles', 4),
        (6, 'new_set_q', 5),
        (14, 'new_set_q', 5),
    ])
    @patch.object(Game, 'quantity_of_tiles', return_value=5)
    def test_play_new_set_q(
        self,
        quantity,
        state,
        q,
        mock,
    ):
        # data
        players = ["player_1", "player_2", 'player_3']
        self.rummy.game = Game(players)

        old_q_tiles = 5
        self.rummy.input_q_tiles = old_q_tiles
        self.rummy.game_state = 'new_set_q'
        # process
        self.rummy.game.distribute_tiles()
        self.rummy.play_new_set_q(quantity)
        # assert
        mock.assert_called_once_with()
        self.assertEqual(self.rummy.game_state, state)
        self.assertEqual(self.rummy.input_q_tiles, q)

    @parameterized.expand([
        # (game_state, )
        ('start_game', 'start_game'),
        ('new_set_tiles', 'make_move'),
        ('put_a_tile', 'make_move'),
        ('select_option', 'select_option'),
    ])
    def test_play_next_turn(self, pre_state, post_state):
        # process
        self.rummy.game_state = pre_state
        self.rummy.next_turn()
        # assert
        self.assertEqual(self.rummy.game_state, post_state)

    @parameterized.expand([
        # (game_state, call_count)
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

    @patch.object(Game, 'make_play')
    def test_play_make_move(self, mock):
        # data
        players = ["player_1", "player_2", 'player_3']
        self.rummy.game = Game(players)

        self.rummy.option = 1
        data = [0, 1, 3, 5]
        # process
        self.rummy.play_make_move(data)
        # assert
        mock.assert_called_once_with(self.rummy.option, data)
        self.assertEqual(self.rummy.game_state, 'select_option')
