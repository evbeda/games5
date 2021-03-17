import unittest

from ..game import Game


class TestGame(unittest.TestCase):

    def test_game_attributes(self):
        game = Game()

        self.assertEqual(game.remaining_tiles, 106)
        self.assertEqual(game.players, [])
        self.assertEqual(game.current_turn, 0)
