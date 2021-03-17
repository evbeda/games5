import unittest
from unittest.mock import patch

from ..game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_game_attributes(self):
        game = Game()

        self.assertEqual(game.remaining_tiles, 106)
        self.assertEqual(game.players, [])
        self.assertEqual(game.current_turn, 0)

    def test_create_players(self):
        player_names = ["Pedro", "Juana", "Mia"]
        
        with patch('rummy_and_burakko.game.Player') as player_patched:
            self.game.create_players(player_names)

        self.assertEqual(len(self.game.players), 3)
        player_patched.assert_called()
