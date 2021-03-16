import unittest
from unittest.mock import patch
from ..game.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        # data
        self.id_test = 1
        self.name_test = 'Test_1'
        self.player_test = Player(self.id_test, self.name_test)
        self.tiles_test = list(range(0, 20))

    def test_player_init(self):
        self.assertEqual(self.player_test.id, self.id_test)
        self.assertEqual(self.player_test.name, self.name_test)

    def test_one_draw(self):
        # process
        self.player_test.one_draw(self.tiles_test)
        # assert
        self.assertEqual(len(self.tiles_test), 19)
        self.assertEqual(len(self.player_test.tiles_in_hand), 1)

    def test_full_draw(self):
        # data
        self.player_test.tiles_in_hand = [9, 99]
        # process
        self.assertEqual(len(self.player_test.tiles_in_hand), 2)
        self.assertEqual(len(self.tiles_test), 20)

        self.player_test.full_draw(self.tiles_test)
        # assert
        self.assertEqual(len(self.player_test.tiles_in_hand), 7)
        self.assertEqual(len(self.tiles_test), 15)

    @patch('random.randint')
    def test_one_draw_random(self, mock_random):
        # data
        start = 0
        end = len(self.tiles_test) - 1
        # process
        self.player_test.one_draw(self.tiles_test)
        # assert
        mock_random.assert_called_once_with(start, end)

    @patch.object(Player, 'one_draw')
    def test_full_draw_calls(self, mock_draw_one):
        # data
        self.player_test.tiles_in_hand = [3, 7, 17]
        # process
        self.player_test.full_draw(self.tiles_test)
        # assert
        self.assertEqual(mock_draw_one.call_count, 4)
