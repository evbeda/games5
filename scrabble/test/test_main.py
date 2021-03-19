import unittest
from unittest.mock import patch
from ..main import Scrabble
from ..game.game import Game
from ..game.player import Player


class TestMain(unittest.TestCase):

    @patch.object(Game, 'print_board')
    def test_board(self, print_board_patched):
        scrabble = Scrabble()
        scrabble.game = Game(["Pedro"])
        board = scrabble.board
        print_board_patched.assert_called()
