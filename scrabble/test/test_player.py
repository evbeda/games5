import unittest
from unittest.mock import patch
from parameterized import parameterized
from ..game.player import Player
from ..game.tile_bag import TileBag
from ..game.tile import Tile


class TestPlayer(unittest.TestCase):
    def setUp(self):
        # data
        self.id_test = 1
        self.name_test = 'Test_1'
        self.player_test = Player(self.id_test, self.name_test)
        self.t_bag = TileBag()

    def test_player_init(self):
        self.assertEqual(self.player_test.id, self.id_test)
        self.assertEqual(self.player_test.name, self.name_test)

    def test_one_draw(self):
        # process
        self.player_test.one_draw(self.t_bag)
        # assert
        self.assertEqual(len(self.t_bag.tiles), 99)
        self.assertEqual(len(self.player_test.tiles_in_hand), 1)

    def test_full_draw(self):
        # data
        self.player_test.tiles_in_hand = [9, 99]
        # process
        self.assertEqual(len(self.player_test.tiles_in_hand), 2)
        self.assertEqual(len(self.t_bag.tiles), 100)

        self.player_test.full_draw(self.t_bag)
        # assert
        self.assertEqual(len(self.player_test.tiles_in_hand), 7)
        self.assertEqual(len(self.t_bag.tiles), 95)

    @patch('random.randint')
    def test_put_t_draw_t(self, mock_random):
        # data
        tiles = [Tile('a') for _ in range(7)]
        self.player_test.tiles_in_hand = tiles.copy()
        t_index = [1, 5]
        # process
        self.player_test.put_t_draw_t(self.t_bag, t_index)
        # assert
        self.assertNotEqual(self.player_test.tiles_in_hand, tiles)
        self.assertEqual(mock_random.call_count, 2)
        self.assertEqual(len(self.player_test.tiles_in_hand), 7)

    @patch('random.randint')
    def test_one_draw_random(self, mock_random):
        # data
        start = 0
        end = len(self.t_bag.tiles) - 1
        # process
        self.player_test.one_draw(self.t_bag)
        # assert
        mock_random.assert_called_once_with(start, end)

    @patch.object(Player, 'one_draw')
    def test_full_draw_calls(self, mock_draw_one):
        # data
        self.player_test.tiles_in_hand = [3, 7, 17]
        # process
        self.player_test.full_draw(self.t_bag)
        # assert
        self.assertEqual(mock_draw_one.call_count, 4)

    @parameterized.expand([
        ('abcdefg', 'a | b | c | d | e | f | g'),
    ])
    def test_get_hand(self, letters, expected):
        self.player_test.tiles_in_hand = [
            Tile(letter) for letter in letters
        ]
        self.assertEqual(self.player_test.get_hand(), expected)
