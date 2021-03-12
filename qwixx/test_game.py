import unittest
# from unittest.mock import patch

from game import Game


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

        dice_set = self.game.create_dice_set()

        for die in dice_set:
            die_color_amount = result_color_amount.setdefault(die.color, 0)
            die_color_amount += 1

        for expected_color, expected_amount in expected_color_amount.items:
            self.assertEqual(
                result_color_amount[expected_color],
                expected_amount
            )
