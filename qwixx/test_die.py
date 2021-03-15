import unittest
from unittest.mock import patch

from die import Die


class TestDie(unittest.TestCase):

    def test_random_die(self):
        die = Die('white')
        with patch('random.randint', return_value=3) as randint_patched:
            result = die.roll_die()
            self.assertEqual(result, 3)
            self.assertEqual(randint_patched.call_args[0][0], 1)
            self.assertEqual(randint_patched.call_args[0][1], 6)

    def test_has_color(self):
        die = Die('blue')
        self.assertEqual(die.color, 'blue')
