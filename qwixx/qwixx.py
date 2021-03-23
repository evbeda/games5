
WHITE = 'white'
COLOR = 'color'


class Qwixx:

    name = 'Qwixx'

    def __init__(self):
        self.state = WHITE
        self.input_args = 2
        self.input_are_ints = False
        self.players = None
        self.current_player = 0
        self.dice_set = {}

    def create_player(self, player_amount):
        if player_amount not in range(1, 5):
            raise Exception
        self.players = [Player() for _ in range(player_amount)]

    def remove_dice(self, color):
        for index, dice in enumerate(self.dice_set):
            if dice.color == color:
                self.dice_set.pop(index)
                break

    def create_dice_set(self):
        raise NotImplementedError

    def mark_with_white(self, row):
        pass

    def mark_with_color(row, die_color, die_white):
        pass

    def next_turn(self):
        if self.you_can_play:
            if self.state == WHITE:
                self.input_args = 1
                self.input_are_ints = True
                # return messages('Choose in which row you want to mark the common dice (0/3) or not (99)?')
            if self.state == COLOR:
                self.input_args = 3
                self.input_are_ints = True
                # return messages("Choose in which row you want to mark a common die with a colored die (0/3),common die (0/1) and color die(0/3) or Penalty (99/99)?")

    def play(self, row, die_color, die_white):
        if self.state == WHITE:
            return self.mark_with_white([row])
        if self.state == COLOR:
            return self.mark_with_color([row, die_color, die_white])

    @property
    def board(self):
        output = " "
        output += "\n"
        output += "the player who plays(player)"
        output += "\n"
        output += "score pad "
        for row in self.rows.values():
            if row.color == 'red':
                output += 'red'
                output += ' ' + tuple(range(2, 13))
                # buscar la forma de representar las marcas en el output
                output += ' ' + self.is_locked(row)
            if row.color == 'yellow':
                output += 'yellow'
                output += ' ' + tuple(range(2, 13))
                output += ' ' + self.is_locked(row)
            if row.color == 'green':
                output += 'green'
                output += ' ' + tuple(reversed(range(2, 13)))
                output += ' ' + self.is_locked(row)
            if row.color == 'blue':
                output += 'blue'
                output += ' ' + tuple(reversed(range(2, 13)))
                output += ' ' + self.is_locked(row)
        output += "\n"
        output += "penalty"
        output += " " + self.scoredpad.penalty
        output += "\n"
        output += "score"
        output += "" + tuple(range(1, 12))
        output += "(1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 70)"

    def is_locked(self, row):
        if self.row.color in self.row.blocked_rows:
            return "is loked"

    @property
    def you_can_play(self):
        if len(self.row.blocked_rows) < 2:
            return True
        else:
            return False  # lo que retorna en realidad end_game()
