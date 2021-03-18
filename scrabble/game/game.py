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
