from .player import Player
from .tile_bag import TileBag
from .board import Board
import random


class Game:

    # def __init__(self, players):
    def __init__(self):
        self.players = []
        # self.players = self.create_players(players)
        self.current_turn = 0
        self.tile_bag = TileBag()
        self.board = Board()

    def create_players(self, names):
        if 2 <= len(names) <= 4:
            self.players = [Player(name) for name in names]
        else:
            raise Exception

    def distribute_tiles(self):
        self.tile_bag.assign_tiles(self.players)

    def random_order(self):
        random.shuffle(self.players)

    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)
        self.players[self.current_turn].change_state()
        self.board.temporary_sets()
        self.players[self.current_turn].temporary_hand()

    def show_game(self):
        return "\n".join([
            "Mesa",
            self.board.get_board(),
            "Mano\n",
            self.players[self.current_turn].get_hand(),
        ])

    def make_play(self, option, *args):
        if option == 3:
            self.end_turn()
        else:
            player = self.players[self.current_turn]
            options = {
                0: self.board.put_new_set
                1: self.board.put_a_tile
                2: self.board.give_one_tile_from_board
            }
            options[option](player, *args)

    def end_turn(self):
        self.players[self.current_turn].change_state()
        if self.valid_turn():
            self.players[self.current_turn].validate_turn()
            self.board.validate_turn()
        else:
            self.tile_bag.give_one_tile(self.players[self.current_turn])

    def valid_turn(self):
        return (
            self.players[self.current_turn].valid_hand() and
            self.board.valid_sets()
        )
