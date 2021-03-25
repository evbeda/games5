import unittest
from unittest.mock import Mock
from .qwixx import Qwixx


class TestQwixx(unittest.TestCase):
    def setUp(self):
        self.qwixx = Qwixx()

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

    def test_new_game_player_count(self):
        qwixx = Qwixx()
        qwixx.create_scored_pad(2)
        self.assertEqual(len(qwixx.score_pad), 2)

    def test_new_game_player_limit(self):
        with self.assertRaises(Exception):
            Qwixx(5)
