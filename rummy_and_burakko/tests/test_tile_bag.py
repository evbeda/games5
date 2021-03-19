import unittest
from unittest.mock import patch
from ..player import Player
from ..tile_bag import TileBag


class TestTileBag(unittest.TestCase):
    def setUp(self):
        self.t_bag = TileBag()

    def test_create_tiles(self):
        with patch('rummy_and_burakko.tile_bag.Tile') as tile_patched:
            self.t_bag.create_tiles()

        self.assertEqual(len(self.t_bag.remaining_tiles), 106)

        tile_list = {
            'r': list(range(1, 14)),
            'y': list(range(1, 14)),
            'w': list(range(1, 14)),
            'b': list(range(1, 14)),
            '*': [0] * 2,
        }

        for color, number_list in tile_list.items():
            for number in number_list:
                tile_patched.assert_any_call(color, number)

    # teste de mock
    @patch.object(Player, "add_tiles")
    def test_call_add_tiles_by_assign_tiles(self, mock):
        players = [Player('juan'), Player('pedro')]
        self.t_bag.assign_tiles(players)
        mock.assert_called()
        self.assertEqual(mock.call_count, 2)
