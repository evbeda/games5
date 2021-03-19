from .tile import Tile
import itertools
import random


class TileBag():
    def __init__(self):
        self.remaining_tiles = self.create_tiles()

    def create_tiles(self):
        temp_tiles = list(itertools.chain(
            *[[Tile(color, number) for color in ['b', 'r', 'y', 'w']*2] for
                number in range(1, 14)]
        ))
        temp_tiles += [Tile('*', 0), Tile('*', 0)]
        return temp_tiles

    def assign_tiles(self, players):
        random.shuffle(self.remaining_tiles)
        for i in players:
            i.add_tiles(self.remaining_tiles[:14])
            self.remaining_tiles = self.remaining_tiles[14:]
