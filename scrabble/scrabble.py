from .game.game import Game


class Scrabble:

    @property
    def input_args(self):
        if self.input_players:
            args = self.input_player_args
        elif self.play_word:
            args = 4
        else:
            args = 1

        return args

    def __init__(self):
        self.is_playing = True
        self.game = None
        self.create_game = True
        self.input_players = False
        self.input_player_args = 0
        self.play_word = False
        self.change_letters = False
        self.challenge = False
        self.in_challenge = False
 
    @property
    def board(self):
        return self.game.print_board()

    def next_turn(self):
        # if game_over -> self.is_playing = False
        query = self.game.get_current_player_hand() + '\n\n'

        if self.play_word:
            query += 'X, Y, V/H, word'
        else:
            query += 'Do you want to play a word?'

        return query

    def play(self, *args):
        if self.create_game:
            # 1 args, player count
            player_count = int(args[0])
            if 2 <= player_count <= 4:
                self.create_game = False
                self.input_players = True
                self.input_player_args = player_count
        elif self.input_players:
            # x args, player names
            self.input_players = False
            self.game = Game(args)
        elif self.play_word:
            # 4 args: X, Y, V/H, word
            x = int(args[0])
            y = int(args[1])
            horizontal = args[2] == 'h'
            word = args[3]
            self.game.place_word(x, y, horizontal, word)
            self.play_word = False
        elif self.change_letters:
            # 1 args, how many
            letter_amount = int(args[0])
            self.game.change_player_tiles(letter_amount)
            self.change_letters = False
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
