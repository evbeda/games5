from .score_pad import (
    ScorePad,
    ReachPenaltyLimit,
    ItCannotBeMarked,
)
from .set_dices import SetDices
from .row import Row


QWIXX_STATE_START = 'start_game'
QWIXX_STATE_OPTION = 'select_option'
QWIXX_STATE_PLAY = 'play'

QWIXX_TURN_WHITE = 'white'
QWIXX_TURN_COLOR = 'color'

game_state_next_turn = {
    QWIXX_STATE_START: 'Enter number of players',
    QWIXX_STATE_OPTION: 'Game option :\n1) play \n2) pass',
}
game_state_color_next_turn = {
    QWIXX_TURN_WHITE:
        'Choose in which row you want to mark the common dice (1): red, 2): yellow, '
        '3): blue, 4): green) or pass ?',
    QWIXX_TURN_COLOR:
        'Choose in which row you want to mark acommon die with a colored die (0/3),'
        'common die (0/1) and color die(0/3) or Penalty (99/99)?',
}
OPTION_PLAY = 1
OPTION_PASS = 2

COLOR_ROW = {
    1: 'red',
    2: 'yellow',
    3: 'blue',
    4: 'green',
}

COLOR_DICE = {
    1: 'white1',
    2: 'white2'
}


class Qwixx:

    name = 'Qwixx'
    input_are_ints = True

    def __init__(self):
        self.game_state = QWIXX_STATE_START
        self.score_pad = []
        self.current_player = 0
        self.current_color_player = 0
        self.dice_set = SetDices()
        self.is_playing = True
        self.turn_color = QWIXX_TURN_WHITE
        self.previous_turn_color = QWIXX_TURN_WHITE

    def play_start(self, n_players):
        self.create_scored_pad(n_players)
        self.dice_set.roll_dices()
        self.game_state = QWIXX_STATE_OPTION

    def create_scored_pad(self, player_amount):
        if player_amount not in range(1, 5):
            raise Exception
        for indice_Player in range(player_amount):
            self.score_pad.append(ScorePad())
            self.score_pad[indice_Player].id_player = indice_Player

    def next_turn(self):
        if self.game_state == QWIXX_STATE_PLAY:
            return game_state_color_next_turn[self.turn_color]
        else:
            return game_state_next_turn[self.game_state]

    def remove_dice(self, color):
        for index, dice in enumerate(self.dice_set):
            if dice.color == color:
                self.dice_set.pop(index)
                break

    def mark_with_color(self, white_index, color_index):
        color = COLOR_ROW[color_index]
        s_pad = self.score_pad[self.current_player]
        first_die = self.dice_set.get_value_of_die(COLOR_DICE[white_index])
        second_die = self.dice_set.get_value_of_die(color)
        total = first_die + second_die
        try:
            s_pad.mark_number_in_row(total, color)
        except ItCannotBeMarked:
            return 'it cannot be marked'
        self.set_next_player()

    def mark_with_white(self, color_index):
        color = COLOR_ROW[color_index]
        s_pad = self.score_pad[self.current_player]
        first_die = self.dice_set.get_value_of_die('white_1')
        second_die = self.dice_set.get_value_of_die('white_2')
        total = first_die + second_die
        s_pad.mark_number_in_row(total, color)
        self.set_next_player()

    def set_next_player(self):
        self.game_state = QWIXX_STATE_OPTION
        next_player = (self.current_player + 1) % len(self.score_pad)
        if self.turn_color == QWIXX_TURN_COLOR and self.previous_turn_color == QWIXX_TURN_WHITE:
            self.current_color_player = (self.current_color_player + 1) % len(self.score_pad)
            self.turn_color = QWIXX_TURN_WHITE
            self.previous_turn_color = QWIXX_TURN_COLOR
            self.dice_set.roll_dices()
        elif next_player == self.current_color_player:
            self.turn_color = QWIXX_TURN_COLOR
            self.previous_turn_color = QWIXX_TURN_WHITE
        self.current_player = next_player

    def play_option(self, option):
        if option == OPTION_PLAY:
            self.game_state = QWIXX_STATE_PLAY
        elif option == OPTION_PASS:
            if self.turn_color == QWIXX_TURN_COLOR:
                try:
                    self.score_pad[self.current_player].add_penalty()
                except ReachPenaltyLimit:
                    self.is_playing = False
            self.set_next_player()
        else:
            return 'Invalid Option'

    def play_turn(self, *args):
        if self.turn_color == QWIXX_TURN_WHITE:
            self.mark_with_white(args[0])
        else:
            self.mark_with_color(args[0], args[1])

    @property
    def input_args(self):
        return (
            2
            if self.game_state == QWIXX_STATE_PLAY and self.turn_color == QWIXX_TURN_COLOR
            else 1
        )

    def play(self, *args):
        if self.game_state == QWIXX_STATE_START:
            self.play_start(args[0])
        elif self.game_state == QWIXX_STATE_OPTION:
            return self.play_option(args[0])
        elif self.game_state == QWIXX_STATE_PLAY:
            return self.play_turn(*args)
        return ''

    @property
    def board(self):
        output = " "
        if self.score_pad:
            output += "Dice: white->{}".format(self.dice_set.get_value_of_die('white_1'))
            output += "\n"
            output += "      white->{}".format(self.dice_set.get_value_of_die('white_2'))
            output += "\n"
            output += "      blue->{}".format(self.dice_set.get_value_of_die('blue'))
            output += "\n"
            output += "      green->{}".format(self.dice_set.get_value_of_die('green'))
            output += "\n"
            output += "      red->{}".format(self.dice_set.get_value_of_die('red'))
            output += "\n"
            output += "the player who plays :{} ".format(self.score_pad[self.current_player].id_player)
            output += "color :" + self.turn_color
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
        output += '{}'.format(row.color)
        output += '{}'.format(str(tuple(range(2, 13))))
        output += "\n"
        output += '{}'.format(row.marks)
        output += "\n"
        output += '{}'.format(self.is_locked(row))
        output += "\n"
        return output

    @property
    def you_can_play(self):
        if len(Row.blocked_rows) < 2:
            self.is_playing = True
        else:
            self.is_playing = False
