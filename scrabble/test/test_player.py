import unittest
from game.player import Player


class TestBoard(unittest.TestCase):
    def test_player_init(self):
        id_test = 1
        name_test = 'Test_1'
        player_test = Player(id_test, name_test)

        self.assertEqual(player_test.id, id_test)
        self.assertEqual(player_test.name, name_test)
