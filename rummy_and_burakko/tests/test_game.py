import unittest
from unittest.mock import patch
from parameterized import parameterized

from ..game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_game_attributes(self):
        game = Game()

        self.assertEqual(game.remaining_tiles, [])
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
        
    def test_create_tiles(self):
        with patch('rummy_and_burakko.game.Tile') as tile_patched:
            self.game.create_tiles()

        self.assertEqual(len(self.game.remaining_tiles), 106)

        tile_list = {
            'r': list(range(1,14)),
            'y': list(range(1,14)),
            'w': list(range(1,14)),
            'b': list(range(1,14)),
            '*': [0] * 2,
        }

        for color, number_list in tile_list.items():
            for number in number_list:
                tile_patched.assert_any_call(color, number)
