import unittest
from unittest.mock import patch
from parameterized import parameterized
from ..scrabble import Scrabble
from ..game.game import Game
from ..game.player import Player


class TestMain(unittest.TestCase):

    def setUp(self):
        self.scrabble = Scrabble()

    @patch.object(Game, 'print_board')
    def test_board(self, print_board_patched):
        self.scrabble.game = Game(["Pedro"])
        board = self.scrabble.board
        print_board_patched.assert_called()

    def test_input_arg_count(self):
        # Create game: Number of players
        self.assertEqual(self.scrabble.input_args, 1)
        self.scrabble.create_game = False

        # Players names: one for each player
        self.scrabble.input_players = True
        self.scrabble.input_player_args = 3
        self.assertEqual(self.scrabble.input_args, 3)
        self.scrabble.input_players = False

        # Pick action: one of play, change, pass
        self.assertEqual(self.scrabble.input_args, 1)

        # Play word: x, y, v/h, word
        self.scrabble.play_word = True
        self.assertEqual(self.scrabble.input_args, 4)
        self.scrabble.play_word = False
        
        # Change letters: amount to change, up to 7
        self.scrabble.change_letters = True
        self.assertEqual(self.scrabble.input_args, 1)
        self.scrabble.change_letters = False
        
        # Challenge words: id of player who challenges (may be penalized)
        self.scrabble.challenge = True
        self.assertEqual(self.scrabble.input_args, 1)
        self.scrabble.challenge = False
        
        # Challenge result: Word is correct/incorrect
        self.scrabble.in_challenge = True
        self.assertEqual(self.scrabble.input_args, 1)
        self.scrabble.in_challenge = False

    def test_play_create_game(self):
        player_count = 3
        self.scrabble.play(player_count)

        self.assertFalse(self.scrabble.create_game)
        self.assertTrue(self.scrabble.input_players)
        self.assertEqual(self.scrabble.input_player_args, player_count)
    
    def test_play_create_game(self):
        player_count = 5

        self.scrabble.play(player_count)

        self.assertTrue(self.scrabble.create_game)
        self.assertFalse(self.scrabble.input_players)
        self.assertEqual(self.scrabble.input_player_args, 0)

    def test_play_setup_players(self):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.create_game = False
        self.scrabble.input_players = True
        self.scrabble.input_player_args = len(player_names)

        self.scrabble.play(player_names)

        self.assertFalse(self.scrabble.input_players)
        self.assertIsNotNone(self.scrabble.game)

    @patch.object(Game, 'change_player_tiles')
    def test_play_change_tiles(self, change_tiles_patched):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.create_game = False
        self.scrabble.change_letters = True
        tile_number = 4

        self.scrabble.play(tile_number)

        self.assertFalse(self.scrabble.change_letters)
        change_tiles_patched.assert_called_with(4)