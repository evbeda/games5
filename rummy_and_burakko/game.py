from .player import Player


class Game:

    def __init__(self):
        self.remaining_tiles = 106
        self.players = []
        self.current_turn = 0

    def create_players(self, names):
        self.players = [Player(name) for name in names]
