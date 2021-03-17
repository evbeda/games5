class Tile:

    set_tile = (('aeoisnlrut', 1),
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
        for t in Tile.set_tile:
            if letter in t[0]:
                self.score = t[1]
                break
       
    @property
    def order(self):
        return ord(self.letter) - ord('a')
