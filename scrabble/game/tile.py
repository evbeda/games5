class Tile:

    letter_score = {
        1: 'aeoisnlrut'.split(),
        2: 'dg'.split(),
        3: 'cbmp'.split(),
        4: 'hfvy'.split(),
        5: 'ch-q'.split('-'),
        8: 'j-ll-ñ-rr-x'.split('-'),
        10: 'z'.split(),
    }

    def __init__(self, letter):
        self.letter = letter
        for score, letter_list in Tile.letter_score.items():
            if letter in letter_list:
                self.score = score
