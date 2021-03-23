from .player import Player
from .tile_bag import TileBag
from .board import Board
import random


class Game:

    def __init__(self):
        self.players = []
        self.current_turn = 0
        self.tile_bag = TileBag()
        self.board = Board()

    def create_players(self, names):
        if 2 <= len(names) <= 4:
            self.players = [Player(name) for name in names]
        else:
            raise Exception

    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)
        self.board.temporary_sets()
        self.players[self.current_turn].temporary_hand()

    def distribute_tiles(self):
        self.tile_bag.assign_tiles(self.players)

    def random_order(self):
        random.shuffle(self.players)

    def show_game(self):
        return "\n".join([
            "Mesa",
            self.board.get_board(),
            "Mano\n",
            self.players[self.current_turn].get_hand(),
        ])

    def hand_to_board(self, indexes):
        pass

    def board_to_hand(self):
        pass

    def end_turn(self):
        if self.board.validate_sets() and self.players[self.current_turn].validate_hand():
            self.board.valid_turn()
            self.players[self.current_turn].valid_turn()
        else:
            self.tile_bag.give_one_tile(self.players[self.current_turn])
