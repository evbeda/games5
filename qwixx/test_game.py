import unittest
from unittest.mock import patch
from unittest.mock import Mock

from .game import Game
from .player import Player


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

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
        self.game.dice_set = []

        colors = [
            'white',
            'white',
            'red',
            'yellow',
            'green',
            'blue',
        ]

        for color in colors:
            die = Mock()
            die.color = color
            self.game.dice_set.append(die)

        self.game.remove_die('blue')
        self.assertNotIn('blue', [die.color for die in self.game.dice_set])

    # El orden de los mocks no es al reves?
    # Por que no utilizan el mock de remove die patched?
    @patch.object(Player, 'mark_number', return_value=True)
    @patch.object(Game, 'remove_die')
    def test_remove_die_when_row_locked(
        self,
        mark_number_patched,
        remove_die_patched,
    ):
        color_locked = self.game.players[self.game.current_player].mark_number(12, 'red')

        if color_locked:
            self.game.remove_die('red')

        assert remove_die_patched.called_with_args('red')

    def test_new_game_player_count(self):
        new_game = Game(2)
        self.assertEqual(len(new_game.players), 2)

    def test_new_game_player_limit(self):
        with self.assertRaises(Exception):
            Game(5)

    def test_end_game(self):
        mock = add_penalty() --> True
        play() # deberia terminar
    
