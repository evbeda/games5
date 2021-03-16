import random


class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.tiles_in_hand = []

    def one_draw(self, tiles_sack):
        index = random.randint(0, len(tiles_sack)-1)
        tile_to_draw = tiles_sack.pop(index)
        self.tiles_in_hand.append(tile_to_draw)

    def full_draw(self, tiles_sack):
        diff = 7 - len(self.tiles_in_hand)
        while diff != 0:
            self.one_draw(tiles_sack)
            diff -= 1
