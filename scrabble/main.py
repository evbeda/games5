from .game.game import Game


class Scrabble:

    @property
    def input_args(self):
        if self.play_word:
            return 4
        else:
            return 1

    def __init__(self):
        self.is_playing = True
        self.game = None
        self.create_game = True
        self.input_players = False
        self.play_word = False
        self.change_letters = False
        self.challenge = False
        self.in_challenge = False
 
    @property
    def board(self):
        return self.game.print_board()

    def next_turn(self):
        # if game_over -> self.is_playing = False
        query = self.game.get_current_player_hand() + '\n'

        if self.play_word:
            query += 'X, Y, V/H, word'
        else:
            query += 'Do you want to play a word?'

        return query

    def play(self, *args):
        if self.create_game:
            # 1 args, player count
            pass
        elif self.input_players:
            # x args, player names
            pass
        elif self.play_word:
            # 4 args
            pass
        elif self.change_letters:
            # 1 args, how many
            pass
        elif self.challenge:
            # 1 args, challenger player -> receives penalty if word is correct
            # challenge round
            pass
        elif self.in_challenge:
            # 1 args, challenge result and apply penalty
            pass
        else:
            # 1 args, play, change or pass
            # if play, set self.play_word = True
            # if change, set self.change_letters
            # if pass do challenge round
            pass
