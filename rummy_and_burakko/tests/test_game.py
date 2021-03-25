import unittest
from unittest.mock import patch
from parameterized import parameterized
from ..tile_bag import TileBag
from ..game import Game
from ..player import Player
from ..board import Board


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_names = ["Pedro", "Juana", "Mia"]
        self.game = Game(self.player_names)

    def test_game_attributes(self):
        self.assertEqual(type(self.game.tile_bag), type(TileBag()))
        self.assertEqual(len(self.game.players), 3)
        self.assertEqual(self.game.current_turn, 0)

    def test_create_players(self):
        with patch('rummy_and_burakko.game.Player') as player_patched:
            self.game.create_players(self.player_names)

        self.assertEqual(len(self.game.players), 3)
        player_patched.assert_called()

    @parameterized.expand([
        # Players, Current, Next
        (3, 0, 1),
        (4, 3, 0),
        (3, 2, 0),
    ])
    def test_next_turn(self, players, current_turn, next_turn):
        self.game.players = [Player("Pedro")] * players
        self.game.current_turn = current_turn

        self.game.next_turn()

        self.assertEqual(self.game.current_turn, next_turn)

    @patch.object(Player, "temporary_hand")
    @patch.object(Board, "temporary_sets")
    @patch.object(Player, "change_state")
    def test_next_turn_calls(
        self,
        m_change_state,
        m_temporary_sets,
        m_temporary_hand,
    ):
        # data
        self.game.players = [Player("Pedro")]
        # process
        self.game.next_turn()
        # assert
        m_change_state.assert_called_once_with()
        m_temporary_sets.assert_called_once_with()
        m_temporary_hand.assert_called_once_with()

    @patch.object(TileBag, "assign_tiles")
    def test_call_assign_tiles(self, mock):
        self.game.distribute_tiles()
        self.assertEqual(mock.call_count, 1)

    @patch('random.shuffle')
    def test_start_order(self, mock):
        # data
        first_order = self.game.players.copy()
        # process
        self.game.random_order()
        mock.assert_called_once_with(first_order)

    board = (
            "1: L[ 0:r5 1:b5 2:y5 ]\n" +
            "2: L[ 0:r3 1:b3 2:y3 3:w3 ]\n" +
            "3: S[ 0:r3 1:r4 2:r5 3:r6 ]"
    )
    hand = "player_1> 0:r11 1:y2 2:y13 3:b5"

    @patch.object(Player, "get_hand", return_value=hand)
    @patch.object(Board, "get_board", return_value=board)
    def test_show_game(self, mock_board, mock_player):
        # data
        expected = (
            "Mesa\n" +
            mock_board.return_value +
            "\nMano\n\n" +
            mock_player.return_value
        )
        # process
        self.game.create_players(["player_1", "player_2"])
        self.game.distribute_tiles()
        result = self.game.show_game()
        # assert
        self.assertEqual(result, expected)
        mock_board.assert_called_once()
        mock_player.assert_called_once()

    @patch.object(Player, "valid_hand", return_value=True)
    @patch.object(Board, "valid_sets", return_value=False)
    def test_valid_turn(self, mock_valid_hand, mock_valid_sets):
        # data
        expected = False
        # process
        self.game.create_players(["player_1", "player_2"])
        self.game.distribute_tiles()
        result = self.game.valid_turn()
        # assert
        self.assertEqual(mock_valid_hand.call_count, 1)
        self.assertEqual(mock_valid_sets.call_count, 1)
        self.assertEqual(result, expected)

    @parameterized.expand([
        # (option, call_count)
        # (0, (1, 0, 0, 0)),
        # (1, (0, 1, 0, 0)),
        (2, (0, 0, 1, 0)),
        (3, (0, 0, 0, 1)),
    ])
    @patch.object(Game, "end_turn")
    @patch.object(Board, "give_one_tile_from_board")
    # @patch.object(Board, "put_a_tile")
    # @patch.object(Board, "put_new_set")
    def test_make_play_calls(
        self,
        option,
        call_count,
        # mock_new_set,
        # mock_put_a_tile,
        mock_take_tile,
        mock_end,
    ):
        # data
        self.game.players = [Player("test_1")]
        arg_1 = 10
        arg_2 = 55
        # process
        self.game.make_play(option, [arg_1, arg_2])
        # assert
        # self.assertEqual(mock_new_set.call_count, call_count[0])
        # self.assertEqual(mock_put_a_tile.call_count, call_count[1])
        self.assertEqual(mock_take_tile.call_count, call_count[2])
        self.assertEqual(mock_end.call_count, call_count[3])

    @patch.object(Board, "give_one_tile_from_board")
    def test_make_play_arguments(self, mock):
        # data
        self.game.players = [Player("test_1")]
        player = self.game.players[self.game.current_turn]
        option = 2
        set_id = 1
        index = 3
        # process
        self.game.make_play(option, [set_id, index])
        # assert
        mock.assert_called_once_with(player, set_id, index)

    @parameterized.expand([
        # (return_value, validate.call_count, give_one_tile.call_count)
        (True, 1, 0),
        (False, 0, 1),
    ])
    @patch.object(TileBag, "give_one_tile")
    @patch.object(Player, "validate_turn")
    @patch.object(Board, "validate_turn")
    @patch.object(Player, "change_state")
    def test_end_turn(
        self,
        rv,
        call_count_1,
        call_count_2,
        mock_player_change_state,
        mock_board,
        mock_player_validate,
        mock_bag,
    ):
        # data
        self.game.create_players(["player_1", "player_2"])
        self.game.distribute_tiles()
        # process
        with patch.object(Game, "valid_turn", return_value=rv) as mock_v_t:
            self.game.end_turn()
            # assert
            self.assertEqual(mock_v_t.call_count, 1)
            self.assertEqual(mock_player_change_state.call_count, 1)
            self.assertEqual(mock_board.call_count, call_count_1)
            self.assertEqual(mock_player_validate.call_count, call_count_1)
            self.assertEqual(mock_bag.call_count, call_count_2)
