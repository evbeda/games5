import unittest
from unittest.mock import patch
from parameterized import parameterized
from ..tile_bag import TileBag
from ..game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_game_attributes(self):
        game = Game()

        self.assertEqual(type(game.tile_bag), type(TileBag()))
        self.assertEqual(game.players, [])
        self.assertEqual(game.current_turn, 0)

    def test_create_players(self):
        player_names = ["Pedro", "Juana", "Mia"]

        with patch('rummy_and_burakko.game.Player') as player_patched:
            self.game.create_players(player_names)

        self.assertEqual(len(self.game.players), 3)
        player_patched.assert_called()

    @parameterized.expand([
        # Players, Current, Next
        (3, 0, 1),
        (4, 3, 0),
        (3, 2, 0),
    ])
    def test_change_turn(self, players, current_turn, next_turn):
        self.game.players = [""] * players
        self.game.current_turn = current_turn

        self.game.next_turn()

        self.assertEqual(self.game.current_turn, next_turn)

    @parameterized.expand([
        (["1"],),
        (["1", "2", "3", "4", "5"],),
    ])
    def test_player_limit(self, players):
        with self.assertRaises(Exception):
            self.game.create_players(players)
