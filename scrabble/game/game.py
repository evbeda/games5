from .board import Board


class Game:
    def __init__(self, n_players):
        if n_players not in range(1, 4):
            raise Exception
        self.players = n_players
        self.board = Board()
        self.turn = 0
