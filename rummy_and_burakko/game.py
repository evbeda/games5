from .player import Player
from .tile_bag import TileBag
from .board import Board
import random
from copy import deepcopy


class Game:

    def __init__(self, players):
        self.players = self.create_players(players)
        self.current_turn = 0
        self.tile_bag = TileBag()
        self.board = Board()

    def create_players(self, names):
        return [Player(name) for name in names]

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

    def make_play(self, option, args):
        player = self.players[self.current_turn]
        options = {
            # 1: self.put_new_set(*args)
            # 2: self.board.put_a_tile(player, *args)
            3: self.board.give_one_tile_from_board(*args)
        }
        options[option]

    def put_new_set(self, indexes):
        # intercambiar indices por tiles (copiando)
        tiles = self.make_tile_array(indexes)
        # eliminar tiles respecto a los indices
        # crear el set con las tiles
        # guardar el set

    def make_tile_array(self, indexes):
        tiles = []
        player = self.players[self.current_turn]
        for index in indexes:
            try:
                tile = deepcopy(player.get_a_tile(index))
            except:
                tile = deepcopy(self.board.get_a_reused_tile(index))

            tiles.append(tile)

        return tiles

    def quantity_of_tiles(self):
        return self.players[self.current_turn].get_lenght()

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
