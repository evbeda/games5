import unittest
from unittest.mock import patch
from ..game.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.id_test = 1
        self.name_test = 'Test_1'
        self.player_test = Player(self.id_test, self.name_test)

    def test_player_init(self):
        self.assertEqual(self.player_test.id, self.id_test)
        self.assertEqual(self.player_test.name, self.name_test)

    def test_one_draw(self):
        # data
        tiles_test = [1, 2, 3]
        # process
        self.assertEqual(len(self.player_test.tiles_in_hand), 0)
        self.assertEqual(len(tiles_test), 3)
        # assert
        self.player_test.one_draw(tiles_test)
        self.assertEqual(len(self.player_test.tiles_in_hand), 1)
        self.assertEqual(len(tiles_test), 2)

    def test_draw_full_hand(self):
        # data
        tiles_test = list(range(0, 20))
        self.player_test.tiles_in_hand = [9, 99]
        # process
        self.assertEqual(len(self.player_test.tiles_in_hand), 2)
        self.assertEqual(len(tiles_test), 20)
        # assert
        self.player_test.complete_hand_draw(tiles_test)
        self.assertEqual(len(self.player_test.tiles_in_hand), 7)
        self.assertEqual(len(tiles_test), 15)

    @patch('random.randint')
    def test_one_draw_random_module(self, mock_random):
        # data
        tiles_test = list(range(0, 10))
        start = 0
        end = len(tiles_test) - 1
        # process
        self.player_test.one_draw(tiles_test)
        # assert
        mock_random.assert_called_once_with(start, end)

    @patch.object(Player, 'one_draw')
    def test_complete_draw_calls(self, mock_draw_one):
        # data
        tiles_test = list(range(0, 10))
        self.player_test.tiles_in_hand = [3, 7, 17]
        # process
        self.player_test.complete_hand_draw(tiles_test)
        # assert
        self.assertEqual(mock_draw_one.call_count, 4)
