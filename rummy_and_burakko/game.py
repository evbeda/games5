import itertools

from .player import Player
from .tile import Tile


class Game:

    def __init__(self):
        self.remaining_tiles = []
        self.players = []
        self.current_turn = 0

    def create_players(self, names):
        self.players = [Player(name) for name in names]

    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def create_tiles(self):
        self.remaining_tiles = list(itertools.chain(
            *[[Tile(color, number) for color in ['b', 'r', 'y', 'w']*2] for number in range(1,14)]
        ))
        self.remaining_tiles += [Tile('*', 0), Tile('*', 0)]
