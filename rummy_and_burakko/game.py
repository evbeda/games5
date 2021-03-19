# import random
from .player import Player
# from .tile import Tile
from .tile_bag import TileBag


class Game:

    def __init__(self):
        # self.remaining_tiles = []
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
            

    # def create_tiles(self):
    #     self.remaining_tiles = list(itertools.chain(
    #         *[[Tile(color, number) for color in ['b', 'r', 'y', 'w']*2] for
    #             number in range(1, 14)]
    #     ))
    #     self.remaining_tiles += [Tile('*', 0), Tile('*', 0)]

    # def asign_tiles(self):
    #     random.shuffle(self.remaining_tiles)
    #     for i in self.players:
    #         i.add_tiles(self.remaining_tiles[:14])
    #         self.remaining_tiles = self.remaining_tiles[15:]
