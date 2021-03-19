from .player import Player
from .tile_bag import TileBag
import random


class Game:

    def __init__(self):
        self.players = []
        self.current_turn = 0
        self.tile_bag = TileBag()

    def create_players(self, names):
        if 2 <= len(names) <= 4:
            self.players = [Player(name) for name in names]
        else:
            raise Exception

    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def distribute_tiles(self):
        self.tile_bag.assign_tiles(self.players)

    def random_order(self):
        random.shuffle(self.players)
