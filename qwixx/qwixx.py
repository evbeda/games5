from .score_pad import ScorePad
from .set_dices import SetDices


QWIXX_STATE_START = 'start_game'
QWIXX_STATE_OPTION = 'select_option'
QWIXX_STATE_WHITE = 'white'
QWIXX_STATE_COLOR = 'color'
game_state_next_turn = {
    QWIXX_STATE_START: 'Enter number of players',
    QWIXX_STATE_OPTION: 'Game option :\n1)play \n2)pass',
    QWIXX_STATE_WHITE: 'Choose in which row you want to mark the common dice (0/3) or not (99)?',
    QWIXX_STATE_COLOR: 'Choose in which row you want to mark acommon die with a colored die (0/3),common die (0/1) andcolor die(0/3) or Penalty (99/99)?',
}


class Qwixx:

    name = 'Qwixx'
    input_are_ints = True

    # @property
    # def input_args(self):
    #     game_state_args = {
    #         QWIXX_STATE_START: 1,
    #         QWIXX_STATE_PLAYERS: self.input_player_args,
    #     }
    #     return game_state_args[self.game_state]()

    def __init__(self):
        self.game_state = QWIXX_STATE_START
        self.input_are_ints = False
        self.score_pad = []
        self.current_player = 0
        self.dice_set = SetDices()
        self.is_playing = True

    def play_start(self, n_players):
        self.score_pad = self.create_scored_pad(n_players)
        self.dice_set.roll_dices()
        self.game_state = QWIXX_STATE_OPTION

    def create_scored_pad(self, player_amount):
        if player_amount not in range(1, 5):
            raise Exception
        for indice_Player in range(player_amount):
            self.score_pad.append(ScorePad())
            self.score_pad[indice_Player].id_player = indice_Player

    def next_turn(self):
        return game_state_next_turn[self.game_state]

    def remove_dice(self, color):
        for index, dice in enumerate(self.dice_set):
            if dice.color == color:
                self.dice_set.pop(index)
                break

    def mark_with_white(self, color):
        s_pad = self.score_pad[self.current_player]
        first_die = self.dice_set.get_value_of_die('white_1')
        second_die = self.dice_set.get_value_of_die('white_2')
        total = first_die + second_die
        s_pad.mark_number_in_row(total, color)

    def play(self, *args):
        if self.game_state == QWIXX_STATE_START:
            self.play_start(args[0])
    #     if self.state == WHITE:
    #         return self.mark_with_white([row])
    #     if self.state == COLOR:
    #         return self.mark_with_color([row, die_color, die_white])

    @property
    def board(self):
        output = " "
        output += "\n"
        output += "the player who plays :" + str(self.score_pad[self.current_player].id_player)
        output += "\n"
        output += "score pad "
        output += "\n"
        for row in self.score_pad[self.current_player].rows.values():
            output += self.output_row(row)
        output += "\n"
        output += "penalty"
        output += " " + str(self.score_pad[self.current_player].penalty)
        output += "\n"
        output += "score :"
        output += "" + str(tuple(range(1, 13)))
        output += "\n"
        output += "       (1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 70)"

        return output

    def is_locked(self, row):
        if row.color in row.blocked_rows:
            return "is loked"
        else:
            return "not loked"

    def output_row(self, row):
        output = ' '
        output += '' + row.color
        output += ' ' + str(tuple(range(2, 13)))
        # buscar la forma de representar las marcas en el output
        output += ' ' + self.is_locked(row)
        output += "\n"
        return output

    # def you_can_play(self):
    #     if len(Row.blocked_rows) < 2:
    #         self.is_playing = True
    #     else:
    #         self.is_playing = False
