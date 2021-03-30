from .game import Game

GAME_STATE_START_GAME = 'start_game'
GAME_STATE_PLAYERS_INPUT = 'players_input'
GAME_STATE_SELECT_OPTION = 'select_option'
GAME_STATE_NEW_SET_Q = 'new_set_q'
GAME_STATE_NEW_SET_TILES = 'new_set_tiles'
GAME_STATE_PUT_A_TILE = 'put_a_tile'
GAME_STATE_GET_A_TILE = 'get_a_tile'
GAME_STATE_END_TURN = 'end_turn'

GAME_STATE_MAKE_MOVE = 'make_move'

game_state_next_turn = {
    GAME_STATE_START_GAME: 'Enter number of players',
    GAME_STATE_PLAYERS_INPUT: 'Enter player names',
    GAME_STATE_SELECT_OPTION: (
        'Game Options:\n1)Enter a complete new set\n2)Put a tile from hand in a existing set\n'
        '3)Take a tile from a set\n4)End turn'
    ),
    GAME_STATE_NEW_SET_Q: 'Enter quantity of tiles to play',
    GAME_STATE_NEW_SET_TILES: 'Put the index of tiles to play in the correct order',
    GAME_STATE_PUT_A_TILE: 'Puting a tile: Select a tile, select the set, select the index in the chosen set',
    GAME_STATE_GET_A_TILE: 'Taking a tile: Select the set, select the index in the chosen set',
    GAME_STATE_END_TURN: 'Turn Ended',
    GAME_STATE_MAKE_MOVE: 'Making move',
}


class RummyAndBurakko():
    name = 'Rummy and Burakko'

    @property
    def input_args(self):
        game_state_args = {
            GAME_STATE_START_GAME: 1,
            GAME_STATE_PLAYERS_INPUT: self.input_player_args,
            GAME_STATE_SELECT_OPTION: 1,
            GAME_STATE_NEW_SET_Q: 1,
            GAME_STATE_NEW_SET_TILES: self.input_q_tiles,
            GAME_STATE_PUT_A_TILE: 3,
            GAME_STATE_GET_A_TILE: 2,
        }
        return game_state_args[self.game_state]

    @property
    def board(self):
        if self.game is None:
            return "Starting..."
        return self.game.show_game()

    def __init__(self):
        self.game = None
        self.game_state = GAME_STATE_START_GAME
        self.is_playing = True
        self.input_player_args = 0
        self.input_q_tiles = 0
        self.option = 0
        self.input_are_ints = True

    # game creation
    def play_start_game(self, players_q):
        if 1 <= players_q <= 4:
            self.input_player_args, self.game_state = players_q, GAME_STATE_PLAYERS_INPUT
            self.input_are_ints = False

    def play_players_input(self, *player_names):
        self.game = Game(player_names)
        self.game.distribute_tiles()
        self.game.random_order()
        self.game_state = GAME_STATE_SELECT_OPTION
        self.input_are_ints = True
        self.game.next_turn()

    def next_turn(self):
        message = '\n'
        if self.game_state == GAME_STATE_END_TURN:
            self.game.end_turn()
            self.game.next_turn()
            message += self.game.show_game()
            self.game_state = GAME_STATE_SELECT_OPTION

        message += game_state_next_turn[self.game_state]
        return message

    # play
    def play_select_option(self, option):
        if 1 <= option <= 4:
            options = {
                1: GAME_STATE_NEW_SET_Q,
                2: GAME_STATE_PUT_A_TILE,
                3: GAME_STATE_GET_A_TILE,
                4: GAME_STATE_END_TURN,
            }
            self.option = option
            self.game_state = options[option]

    def play_new_set_q(self, quantity):
        limit = self.game.quantity_of_tiles()
        if 3 <= quantity <= limit:
            self.input_q_tiles = quantity
            self.game_state = GAME_STATE_NEW_SET_TILES

    def play_make_move(self, *moves):
        self.game.make_play(self.option, moves)
        self.game_state = GAME_STATE_SELECT_OPTION

    def play(self, *args):
        if self.game_state in [
            GAME_STATE_NEW_SET_TILES,
            GAME_STATE_PUT_A_TILE,
            GAME_STATE_GET_A_TILE,
        ]:
            self.game_state = GAME_STATE_MAKE_MOVE

        method = getattr(self, 'play_' + self.game_state)
        method(*args)
