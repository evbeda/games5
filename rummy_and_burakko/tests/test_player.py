import unittest

from ..player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("")

    def test_player_attributes(self):
        player = Player("Pedro")

        self.assertEqual(player.name, "Pedro")
        self.assertEqual(player.first_move, True)
        self.assertEqual(player.hand, [])

    def test_add_tiles_to_hand(self):
        self.player.add_tiles([1, 2, 5])
        
        [self.assertIn(tile, self.player.hand) for tile in [1, 2, 5]]

    def test_take_tiles_from_hand(self):
        self.player.hand = [2, 6, 7, 8]
        
        self.player.remove_tiles([6, 8])

        [self.assertNotIn(tile, self.player.hand) for tile in [6, 8]]
        
    def test_take_tile_not_in_hand(self):
        self.player.hand = [1, 2, 3]

        with self.assertRaises(Exception):
            self.player.remove_tiles([4])
