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
        self.option = 0

    # game creation
    def play_create_game(self, player_count):
        if 2 <= player_count <= 4:
            self.input_player_args = player_count
            self.game_state = GAME_STATE_INPUT_PLAYERS

    def play_input_players(self, *player_names):
        self.game = Game(player_names)
        self.game_state = GAME_STATE_SELECT_OPTION

    # turn event
    def next_turn_query(self):
        game_state_next_turn = {
            GAME_STATE_CREATE_GAME: 'Enter number of players',
            GAME_STATE_INPUT_PLAYERS: 'Enter player names',
            GAME_STATE_SELECT_OPTION: 'Game Options:\n1)Enter a complete new set\n2)Put a tile from hand in a existing set\n3)Take a tile from a set\n4)End turn',
            GAME_STATE_NEW_SET_Q: 'Enter quantity of tiles to play',
            GAME_STATE_NEW_SET_TILES: 'Put the index of tiles to play in the correct order',
            GAME_STATE_PUT_A_TILE: 'Puting a tile: Select a tile, select the set, select the index in the chosen set',
            GAME_STATE_GET_A_TILE: 'Taking a tile: Select the set, select the index in the chosen set',
            GAME_STATE_PASS: 'Passing',
        }
        return game_state_next_turn[self.game_state]

    def next_turn(self):
        query = '\n'


        query += self.board + '\n\n'
        query += self.next_turn_state_query()

        return query

    # plays
    def play_select_option(self, option):
        options = {
            1: GAME_STATE_NEW_SET_Q,
            2: GAME_STATE_PUT_A_TILE,
            3: GAME_STATE_GET_A_TILE,
            4: GAME_STATE_PASS,
        }
        self.option = option
        self.game_state = options[option]


    def play(self, *args):
        method_name = 'play_' + self.game_state
        method = getattr(self, method_name)
        method(*args)
