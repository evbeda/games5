import unittest
from unittest.mock import patch

from die import Die


class TestDie(unittest.TestCase):

    def setUp(self):
        self.die = Die()

    def test_random_die(self):
        with patch('random.randint', return_value=3) as randint_patched:
            result = self.die.roll_die()
            self.assertEqual(result, 3)
            self.assertEqual(randint_patched.call_args[0][0], 1)
            self.assertEqual(randint_patched.call_args[0][1], 6)
