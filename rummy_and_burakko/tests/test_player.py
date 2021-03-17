import unittest

from ..player import Player


class TestPlayer(unittest.TestCase):
    def test_player_attributes(self):
        player = Player("Pedro")

        self.assertEqual(player.name, "Pedro")
        self.assertEqual(player.first_move, True)
        self.assertEqual(player.hand, [])
