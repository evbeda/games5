from game.spot import Spot


class Board:
    def __init__(self):
        self.spots = [[Spot(None) for _ in range(15)] for _ in range(15)]
