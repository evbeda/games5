import unittest
from ..player import Player
from ..tile import Tile


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Pedro")

    def test_player_attributes(self):
        self.assertEqual(self.player.name, "Pedro")
        self.assertEqual(self.player.first_move, True)
        self.assertEqual(self.player.hand, [])

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

    def test_hand_format(self):
        self.player.hand = [Tile('r', 7), Tile('b', 4), Tile('y', 5)]

        self.assertEqual(self.player.get_hand(), 'Pedro> 0:r7 1:b4 2:y5')

    # def test_validate_hand(self):
    #     player.hand = [Tile('r', 7), Tile('b', 4), Tile('y', 5)]