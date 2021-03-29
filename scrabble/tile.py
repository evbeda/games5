class Tile:

    set_tile = (
        ('aeoisnlrut', 1),
        ('dg', 2),
        ('cbmp', 3),
        ('hfvy', 4),
        ('ch-q'.split('-'), 5),
        ('j-ll-ñ-rr-x'.split('-'), 8),
        ('z', 10)
    )

    def __init__(self, letter):
        self.letter = letter
        self.score = 0
        for tile_set, score in Tile.set_tile:
            if letter in tile_set:
                self.score = score
                break

    def __eq__(self, other):
        return self.letter == other.letter
