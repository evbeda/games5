import unittest
from ..game.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.id_test = 1
        self.name_test = 'Test_1'
        self.player_test = Player(self.id_test, self.name_test)

    def test_player_init(self):
        self.assertEqual(self.player_test.id, self.id_test)
        self.assertEqual(self.player_test.name, self.name_test)

    def test_draw(self):
        # data
        tiles_test = [1, 2, 3]

        # process
        self.assertEqual(len(self.player_test.tiles_in_hand), 0)
        self.assertEqual(len(tiles_test), 3)

        self.player_test.draw(tiles_test)
        self.assertEqual(len(self.player_test.tiles_in_hand), 1)
        self.assertEqual(len(tiles_test), 2)
