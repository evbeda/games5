import unittest
# from unittest.mock import patch
from .player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.t_player = Player()
        # self.t_player = Player('Test_name')

    # def test_constructor(self):
        # self.assertEqual(self.t_player.name, 'Test_name')
