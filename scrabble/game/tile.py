class Tile:

    letter_score = {
        1: list('aeoisnlrut'),
        2: list('dg'),
        3: list('cbmp'),
        4: list('hfvy'),
        5: 'ch-q'.split('-'),
        8: 'j-ll-ñ-rr-x'.split('-'),
        10: list('z'),
    }

    def __init__(self, letter):
        self.letter = letter
        self.score = 0
        for score, letter_list in Tile.letter_score.items():
            if letter in letter_list:
                self.score = score
                break
