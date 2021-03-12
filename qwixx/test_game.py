import unittest
from unittest.mock import patch

from game import Game
from player import Player


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_dice_set(self):
        expected_color_amount = {
            'white': 2,
            'red': 1,
            'yellow': 1,
            'green': 1,
            'blue': 1,
        }
        result_color_amount = {}

        self.game.create_dice_set()

        for die in self.game.dice_set:
            die_color_amount = result_color_amount.setdefault(die.color, 0)
            die_color_amount += 1

        for expected_color, expected_amount in expected_color_amount.items:
            self.assertEqual(
                result_color_amount[expected_color],
                expected_amount
            )

    def test_remove_die_from_set(self):
        self.game.create_dice_set()
        self.game.remove_dice('blue')
        self.assertNotIn('blue', [die.color for die in self.game.dice_set])

    @patch.object(Player, 'mark_number', return_value=True)
    @patch.object(Game, 'remove_die')
    def test_check_row_locked(self, mark_number_patched, remove_die_patched):
        color_locked = self.game.current_player.mark_number(12, 'red')

        if color_locked:
            self.game.remove_die('red')

        assert remove_die_patched.called_with_args('red')