import unittest
from unittest.mock import patch
from ..game.game import Game
from ..game.player import Player
from ..game.tile import Tile


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
