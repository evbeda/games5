import unittest
from ..game.game import Game


class TestGame(unittest.TestCase):

    def test_game_initiator(self):
        g = Game(3)
        self.assertEqual(g.turn, 0)

    def test_new_player(self):
        g = Game(3)
        self.assertEqual(g.players, 3)

    def test_new_player_max(self):
        with self.assertRaises(Exception):
            Game(5)

