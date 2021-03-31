import unittest
from unittest.mock import patch
from parameterized import parameterized
from ..game import Game
from ..player import Player
from ..tile import Tile
from ..board import Board


class TestGame(unittest.TestCase):
    def setUp(self):
        players = ["player_1", "player_2", "player_3"]
        self.t_game = Game(players)

    @parameterized.expand([
        (2, 86),
        (3, 79),
        (4, 72),
    ])
    def test_game_initiator(self, players, remaining_tiles):
        t_game = Game([f"player_{i}" for i in range(players)])
        self.assertEqual(len(t_game.tile_bag.tiles), remaining_tiles)

    def test_create_players(self):
        self.assertEqual(len(self.t_game.players), 3)
        self.assertEqual(self.t_game.players[2].name, "player_3")

    def test_players_max(self):
        with self.assertRaises(Exception):
            Game(5)

    @patch.object(Board, 'get_board')
    def test_print_board(self, get_board_patched):
        self.t_game.print_board()
        get_board_patched.assert_called()

    @patch.object(Player, 'get_hand')
    def test_get_current_player_hand(self, get_hand_patched):
        self.t_game.get_current_player_hand()
        get_hand_patched.assert_called()

    @patch.object(Game, 'change_turn')
    def test_skip_turn(self, change_turn_patched):
        self.t_game.skip_turn()
        self.assertEqual(self.t_game.skipped_turns, 1)
        change_turn_patched.assert_called()

    @patch.object(Game, 'game_over')
    def test_skip_turn_game_over(self, game_over_patched):
        self.t_game.skipped_turns = 5
        self.t_game.skip_turn()
        game_over_patched.assert_called()

    @parameterized.expand([
        (4, 2, 3),
        (2, 1, 0),
        (3, 2, 0),
        (4, 3, 0),
    ])
    def test_change_turn(self, player_count, current_player, next_player):
        players = ["Juan" for _ in range(player_count)]
        t_game = Game(players)
        t_game.current_player = current_player
        t_game.change_turn()
        self.assertEqual(t_game.current_player, next_player)

    def test_change_turn_refill_hand(self):
        player = self.t_game.players[self.t_game.current_player]
        player.tiles_in_hand.pop()
        self.t_game.change_turn()
        self.assertEqual(len(player.tiles_in_hand), 7)

    def test_change_turn_skip_lost(self):
        self.t_game.current_player = 0
        self.t_game.lost_turns = [1]
        self.t_game.change_turn()
        self.assertEqual(self.t_game.current_player, 2)

    @parameterized.expand([
        (
            [30, 40, 35],
            [
                ['a', 'b', 'c'],
                ['x', 'y', 'h'],
                ['f', 'e', 'q'],
            ],
            True,
            [23, 24, 25],
        ),
        (
            [30, 40, 35],
            [
                ['a', 'b', 'c'],
                ['x', 'y'],
                ['f', 'e', 'q'],
            ],
            False,
            [30, 40, 35],
        ),
    ])
    def test_count_points(
        self, scores, player_hands, minus_remaining_tiles, expected
    ):
        for player, score, tiles in zip(
            self.t_game.players,
            scores,
            player_hands
        ):
            player.score = score
            player.tiles_in_hand = [Tile(t) for t in tiles]
        score = self.t_game.count_points(minus_remaining_tiles)
        for player_score, expected_score in zip(score, expected):
            self.assertEqual(player_score[1], expected_score)

    def test_resolve_challenge_word_correct(self):
        self.t_game.resolve_challenge(True, 1)
        self.assertIn(1, self.t_game.lost_turns)

    def test_resolve_challenge_word_correct_no_player(self):
        with self.assertRaises(Exception):
            self.t_game.resolve_challenge(True)

    @patch.object(Player, 'revert_play')
    @patch.object(Board, 'revert_board')
    def test_resolve_challenge_word_incorrect(
        self, revert_board_patched, revert_play_patched
    ):
        self.t_game.resolve_challenge(False)
        revert_board_patched.assert_called()
        revert_play_patched.assert_called()

    @parameterized.expand([
        (
            [
                (0, 10),
                (1, 50),
                (2, 30),
            ],
            [
                (1, 50),
                (2, 30),
                (0, 10),
            ],
            True,
        ),
        (
            [
                (0, 10),
                (1, 30),
                (2, 30),
            ],
            [
                (1, 30),
                (2, 30),
                (0, 10),
            ],
            False,
        ),
    ])
    @patch.object(Game, 'count_points')
    def test_game_over(
        self, result, sorted_result, expected_param, count_points_patched
    ):
        count_points_patched.return_value = result
        self.t_game.game_over()
        self.assertFalse(self.t_game.is_playing)
        self.assertEqual(self.t_game.game_results, sorted_result)
        count_points_patched.assert_called_with(expected_param)

    @parameterized.expand([
        (
            [
                (1, 50),
                (2, 30),
                (0, 10),
            ],
            [60, 65, 20],
            'Final scores:\n'
            '1: player_2 - 50\n'
            '2: player_3 - 30\n'
            '3: player_1 - 10',
        ),
    ])
    def test_get_game_results(self, game_results, player_scores, expected):
        self.t_game.game_results = game_results
        for player, score in zip(self.t_game.players, player_scores):
            player.score = score

        self.assertEqual(self.t_game.get_game_results(), expected)

    @patch.object(Board, 'place_word')
    def test_place_word(self, place_word_patched):
        self.t_game.place_word(7, 6, False, 'word')
        player = self.t_game.players[self.t_game.current_player]
        place_word_patched.assert_called_with('word', 6, 7, False, player)
