import unittest
from unittest.mock import patch, Mock
from .player import Player
from .qwixx import Qwixx


class TestQwixx(unittest.TestCase):
    def setUp(self):
        self.qwixx = Qwixx()

    @unittest.skip('raise NotImplementedError in create_dice_set')
    def test_dice_set(self):
        expected_color_amount = {
            'white': 2,
            'red': 1,
            'yellow': 1,
            'green': 1,
            'blue': 1,
        }
        result_color_amount = {}
        self.qwixx.create_dice_set()

        for dice in self.qwixx.dice_set:
            dice_color_amount = result_color_amount.setdefault(dice.color, 0)
            dice_color_amount += 1

        for expected_color, expected_amount in expected_color_amount.items():
            self.assertEqual(
                result_color_amount[expected_color],
                expected_amount
            )

    def test_remove_dice_from_set(self):
        self.qwixx.dice_set = []

        colors = [
            'white',
            'white',
            'red',
            'yellow',
            'green',
            'blue',
        ]

        for color in colors:
            dice = Mock()
            dice.color = color
            self.qwixx.dice_set.append(dice)

        self.qwixx.remove_dice('blue')
        self.assertNotIn('blue', [dice.color for dice in self.qwixx.dice_set])

    # El orden de los mocks no es al reves?
    # Por que no utilizan el mock de remove dice patched?
    @patch.object(Player, 'mark_number', return_value=True)
    @patch.object(Qwixx, 'remove_dice')
    def test_remove_dice_when_row_locked(
        self,
        mark_number_patched,
        remove_dice_patched,
    ):
        self.qwixx.create_player(4)
        color_locked = self.qwixx.players[self.qwixx.current_player].mark_number(12, 'red')

        if color_locked:
            self.qwixx.remove_dice('red')

        assert remove_dice_patched.called_with_args('red')

    def test_new_game_player_count(self):
        qwixx = Qwixx()
        qwixx.create_player(2)
        self.assertEqual(len(qwixx.players), 2)

    def test_new_game_player_limit(self):
        with self.assertRaises(Exception):
            Qwixx(5)
