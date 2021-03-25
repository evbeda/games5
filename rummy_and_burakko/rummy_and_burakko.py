from .game import Game

GAME_STATE_CREATE_GAME = 'create_game'
GAME_STATE_INPUT_PLAYERS = 'input_players'
GAME_STATE_SELECT_OPTION = 'select_option'
GAME_STATE_NEW_SET_Q = 'new_set_q'
GAME_STATE_NEW_SET_TILES = 'new_set_tiles'
GAME_STATE_PUT_A_TILE = 'put_a_tile'
GAME_STATE_GET_A_TILE = 'get_a_tile'
GAME_STATE_PASS = 'pass'


class RummyAndBurakko():
    name = 'Rummy and Burakko'
    input_are_ints = True

    @property
    def input_args(self):
        game_state_args = {
            GAME_STATE_CREATE_GAME: 1,
            GAME_STATE_INPUT_PLAYERS: self.input_player_args,
            GAME_STATE_SELECT_OPTION: 1,
            GAME_STATE_NEW_SET_Q: 1,
            GAME_STATE_NEW_SET_TILES: self.input_q_tiles,
            GAME_STATE_PUT_A_TILE: 3,
            GAME_STATE_GET_A_TILE: 3,
            GAME_STATE_PASS: 0,
        }
        return game_state_args[self.game_state]()

    @property
    def board(self):
        if self.game is not None:
            return self.game.show_game()
        return "Starting..."

    def __init__(self):
        self.game = None
        self.game_state = GAME_STATE_CREATE_GAME
        self.is_playing = True
        self.input_player_args = 0
        self.input_q_tiles = 0

    # game creation
    def create_game(self, player_count):
        if 2 <= player_count <= 4:
            self.input_player_args = player_count
            self.game_state = GAME_STATE_INPUT_PLAYERS

    def input_players(self, *player_names):
        self.game = Game(player_names)
        self.game_state = GAME_STATE_SELECT_OPTION

    # turn event
    def next_turn(self):
        if self.is_playing:
            return 'Give me a number from 0 to 100'
        else:
            return 'Game Over'

    # plays
    def play(self, number):
        self.played_numbers.append(number)
        if number < self._guess_number:
            return 'too low'
        elif number > self._guess_number:
            return 'too high'
        self.is_playing = False
        return 'you win'
