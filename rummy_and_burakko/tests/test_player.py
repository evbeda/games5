import unittest
from ..player import Player
from ..tile import Tile
from parameterized import parameterized


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Pedro")

    def test_player_attributes(self):
        self.assertEqual(self.player.name, "Pedro")
        self.assertEqual(self.player.first_move, True)
        self.assertEqual(self.player.hand, [])

    def test_add_tiles_to_hand(self):
        # To hand
        self.player.add_tiles([1, 2, 5])
        [self.assertIn(tile, self.player.hand) for tile in [1, 2, 5]]

        # To temp_hand
        self.player.is_playing = True
        self.player.add_tiles([7, 8, 12, 13])
        [self.assertIn(tile, self.player.temp_hand) for tile in [7, 8, 12, 13]]

    @parameterized.expand([
        # (indexes, expected)
        (0, [2, 3, 4, 5]),
        (4, [1, 2, 3, 4]),
        (2, [1, 2, 4, 5]),
    ])
    def test_remove_tile(self, index, expected):
        # data
        self.player.temp_hand = list(range(1, 6))
        # process
        self.player.remove_tile(index)
        # assert
        self.assertEqual(self.player.temp_hand, expected)

    def test_hand_format(self):
        self.player.temp_hand = [Tile('r', 7), Tile('b', 4), Tile('y', 5)]

        self.assertEqual(self.player.get_hand(), 'Pedro> 0:r7 1:b4 2:y5')

    @parameterized.expand([
        # temp_hand, expected
        ([Tile('r', 7), Tile('b', 4), Tile('y', 5), Tile('*', 0)], False),
        ([Tile('r', 7), Tile('b', 4), Tile('y', 5), Tile('*', 0), Tile('r', 13)], False),
        ([Tile('r', 7), Tile('b', 4)], True),
        ([], True),
    ])
    def test_valid_hand(self, temp_hand, expected):
        # data
        self.player.hand = [
            Tile('r', 7),
            Tile('b', 4),
            Tile('y', 5),
            Tile('*', 0)
        ]
        self.player.temp_hand = temp_hand
        # process
        result = self.player.valid_hand()
        # assert
        self.assertEqual(result, expected)

    def test_validate_turn(self):
        p = Player('jugador 1')
        p.temp_hand = [1, 2, 3]

        p.validate_turn()

        self.assertTrue(p.hand == p.temp_hand)
        self.assertFalse(p. hand is p.temp_hand)

    def test_change_state(self):
        self.assertFalse(self.player.is_playing)
        self.player.change_state()
        self.assertTrue(self.player.is_playing)

    def test_get_lenght(self):
        # data
        self.player.temp_hand = [
            Tile('r', 7),
            Tile('b', 4),
            Tile('y', 5),
            Tile('*', 0),
        ]
        expected = 4
        # process
        result = self.player.get_lenght()
        # assert
        self.assertEqual(result, expected)

    def test_get_a_tile(self):
        # data
        self.player.temp_hand = [
            Tile('r', 7),
            Tile('b', 4),
            Tile('y', 5),
            Tile('*', 0),
        ]
        index = 3
        expected = Tile('*', 0)
        # process
        result = self.player.get_a_tile(index)
        # assert
        self.assertEqual(result, expected)
