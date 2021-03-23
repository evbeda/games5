from .board import Board
from .tile_bag import TileBag
from .player import Player


class Game:

    def __init__(self, name_players):
        if len(name_players) not in range(1, 5):
            raise Exception
        self.players = self.create_player(name_players)
        self.board = Board()
        self.tile_bag = TileBag()
        self.first = 0
        self.skipped_turns = 0
        self.current_player = 0

    def create_player(self, name_players):
        return [Player(j, name) for j, name in enumerate(name_players)]

    # def first_player(self):
    #     ref = []
    #     for player in self.players:
    #         print("first call", len(self.tile_bag.tiles))
    #         player.one_draw(self.tile_bag)
    #         print("second call", len(self.tile_bag.tiles))
    #         value = player.tiles_in_hand[0].order
    #         ref.append((value))
    #     return ref.index(min(ref))

    def print_board(self):
        return self.board.get_board()

    def change_player_tiles(self, tile_amount):
        self.players.get(self.current_player).put_t_draw_t(tile_amount)

    def place_word(x, y, horizontal, word):
        self.board.place_word(word, y, x, horizontal)

    @property
    def player_count(self):
        return len(self.players)

    def resolve_challenge(self, result):
        pass

    def get_current_player_hand(self):
        curr_player = self.players[self.current_player]
        return f'{curr_player.name}:\n{curr_player.get_hand()}'

    def change_turn(self):
        self.current_player = (self.current_player + 1) % self.player_count

    def skip_turn(self):
        if self.skipped_turns < self.player_count * 2:
            self.skipped_turns += 1
        else:
            self.game_over()
        self.change_turn()

    def game_over(self):
        pass
