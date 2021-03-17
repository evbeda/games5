import unittest
from unittest.mock import patch
from .dice import Dice


class TestDice(unittest.TestCase):
    def test_random_dice(self):
        dice = Dice('white')
        with patch('random.randint', return_value=3) as randint_patched:
            result = dice.roll_dice()
            self.assertEqual(result, 3)
            self.assertEqual(randint_patched.call_args[0][0], 1)
            self.assertEqual(randint_patched.call_args[0][1], 6)
            # randint_patched.assert_called_once_with(1, 6)

    def test_has_color(self):
        dice = Dice('blue')
        self.assertEqual(dice.color, 'blue')
