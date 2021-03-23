import unittest
from unittest.mock import patch
from parameterized import parameterized
from ..scrabble import Scrabble
from ..game.game import Game
from ..game.player import Player
from ..game.tile import Tile


class TestScrabble(unittest.TestCase):

    def setUp(self):
        self.scrabble = Scrabble()

    @patch.object(Game, 'print_board')
    def test_board(self, print_board_patched):
        self.scrabble.game = Game(["Pedro"])
        board = self.scrabble.board
        print_board_patched.assert_called()

    @parameterized.expand([
        ('create_game', 1),
        ('play_word', 4),
        ('ask_challenge', 1),
        ('in_challenge', 1),
        ('select_action', 1),
    ])
    def test_input_arg_count(self, state, args):
        # Create game: Number of players
        self.scrabble.game_state = state
        self.assertEqual(self.scrabble.input_args, args)

    def test_input_arg_count_for_input_players(self):
        # Players names: one for each player
        self.scrabble.game_state = 'input_players'
        self.scrabble.input_player_args = 3
        self.assertEqual(self.scrabble.input_args, 3)

    def test_play_create_game(self):
        self.scrabble.play(3)
        self.assertEqual(self.scrabble.input_player_args, 3)
        self.assertEqual(self.scrabble.game_state, 'input_players')
    
    def test_play_create_game_invalid(self):
        player_count = 5
        self.scrabble.play(player_count)
        self.assertEqual(self.scrabble.input_player_args, 0)
        self.assertEqual(self.scrabble.game_state, 'create_game')

    def test_play_setup_players(self):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game_state = 'input_players'
        self.scrabble.input_player_args = len(player_names)
        self.scrabble.play(player_names)
        self.assertIsNotNone(self.scrabble.game)
        self.assertEqual(self.scrabble.game_state, 'select_action')

    @patch.object(Game, 'change_player_tiles')
    def test_play_change_tiles(self, change_tiles_patched):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game_state = 'change_letters'
        tiles = ('a', 'b', 'c')
        self.scrabble.change_letters = len(tiles)
        self.scrabble.play(*tiles)
        self.assertEqual(self.scrabble.game_state, 'change_turn')
        change_tiles_patched.assert_called_with(tiles)

    @patch.object(Game, 'place_word')
    def test_play_add_word(self, play_word_patched):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game_state = 'play_word'
        self.scrabble.play('5', '7', 'h', 'word')
        self.assertEqual(self.scrabble.game_state, 'ask_challenge')
        play_word_patched.assert_called_with(5, 7, True, 'word')

    def test_play_action_pass(self):
        self.scrabble.game_state = 'select_action'
        self.scrabble.play('pass')
        self.assertEqual(self.scrabble.game_state, 'change_turn')

    def test_play_action_play_word(self):
        self.scrabble.game_state = 'select_action'
        self.scrabble.play('play')
        self.assertEqual(self.scrabble.game_state, 'play_word')

    def test_play_action_change_letters(self):
        self.scrabble.game_state = 'select_action'
        self.scrabble.play('4')
        self.assertEqual(self.scrabble.change_letters, 4)
        self.assertEqual(self.scrabble.game_state, 'change_letters')

    def test_play_challenge(self):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game_state = 'ask_challenge'
        self.scrabble.play(1)
        self.assertEqual(self.scrabble.challenger_player, 1)
        self.assertEqual(self.scrabble.game_state, 'in_challenge')

    def test_play_challenge_skip(self):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game_state = 'ask_challenge'
        self.scrabble.play(99)
        self.assertEqual(self.scrabble.game_state, 'change_turn')

    @parameterized.expand([
        ('yes', True),
        ('no', False),
    ])
    @patch.object(Game, 'resolve_challenge')
    def test_play_challenge_result(self, user_input, expected_param, resolve_challenge_patched):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game_state = 'in_challenge'
        self.scrabble.challenger_player = 1
        self.scrabble.play(user_input)
        self.assertEqual(self.scrabble.game_state, 'change_turn')
        resolve_challenge_patched.assert_called_with(expected_param)

    @parameterized.expand([
        ('create_game', True),
        ('input_players', False),
        ('play_word', False),
        ('change_letters', False),
        ('ask_challenge', True),
        ('in_challenge', False),
        ('select_action', False),
    ])
    def test_input_are_ints(self, state, expected):
        self.scrabble.game_state = state
        self.assertEqual(self.scrabble.input_are_ints, expected)

    @parameterized.expand([
        ('create_game', 'Enter number of players'),
        ('input_players', 'Enter player names'),
        ('change_letters', 'Which letters do you want to change?'),
        ('play_word', 'Enter start coordinates, orientation and word\nx  y  h/v  word'),
        ('ask_challenge', 'Any player wants to challenge'),
        ('in_challenge', 'Look up new words in a dictionary. Are they correct?'),
        ('select_action', 'Enter "play" to play a new word, "pass" to end your turn or any number to change that amount of tiles'),
    ])
    def test_next_turn_state_query(self, state, expected):
        self.scrabble.game_state = state
        text = self.scrabble.next_turn_state_query()
        self.assertEqual(text, expected)

    @parameterized.expand([
        ('abcdefg', 'a | b | c | d | e | f | g'),
    ])
    def test_next_turn_show_hand(self, letters, expected):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game.current_player = 0
        self.scrabble.game.players[0].tiles_in_hand = [
            Tile(letter) for letter in letters
        ]
        hand_str = self.scrabble.next_turn_show_hand()
        self.assertEqual(hand_str, expected)
