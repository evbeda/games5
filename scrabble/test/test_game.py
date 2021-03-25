import unittest
from unittest.mock import patch
from parameterized import parameterized
from ..game.game import Game
from ..game.player import Player
from ..game.tile import Tile
from ..game.board import Board


class TestGame(unittest.TestCase):
    def setUp(self):
        players = ["player_1", "player_2", "player_3"]
        self.t_game = Game(players)

    # actualizar cuando se tenga el manejo de turnos
    def test_game_initiator(self):
        self.assertEqual(len(self.t_game.tile_bag.tiles), 100)

    def test_create_players(self):
        self.assertEqual(len(self.t_game.players), 3)
        self.assertEqual(self.t_game.players[2].name, "player_3")

    def test_players_max(self):
        with self.assertRaises(Exception):
            Game(5)

    # class DrawGenerator:
    #     letters = 'cas'

    #     def __init__(self):
    #         self.last_index = -1

    #     def __call__(self, *args, **kwargs):
    #         self.last_index += 1
    #         return self.letters[self.last_index]

    # draw_generator = DrawGenerator()
    # def test_first_player(self):
    #     with patch.object(Player, 'one_draw', side_effect='draw_generator') as mock_one_draw:
    #         players = ["player_1"]
    #         t_game = Game(players)
    #         x = t_game.first_player()
    #         self.assertEqual(mock_one_draw.call_count, 3)
    #         self.assertEqual(x, 0)

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
    def test_count_points(self, scores, player_hands, minus_remaining_tiles, expected):
        for player, score, tiles in zip(self.t_game.players, scores, player_hands):
            player.score = score
            player.tiles_in_hand = [Tile(t) for t in tiles]
        score = self.t_game.count_points(minus_remaining_tiles)
        for player_score, expected_score in zip(score, expected):
            self.assertEqual(player_score, expected_score)

    def test_resolve_challenge_word_correct(self):
        self.t_game.resolve_challenge(True, 1)
        self.assertIn(1, self.t_game.lost_turns)

    def test_game_over(self):
        pass
