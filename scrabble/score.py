from .tile import Tile


class Score:

    # def score_word(self):
    #     pass

    # def search_horiz_word(self):
    #     pass

    # def search_vert_word(self):
    #     pass

    def multiply_score(self, spots, word):
        score = 0
        word_mult = 1
        for spot, letter in zip(spots, word):
            if spot.tile is None and spot.mult_type == 'w':
                word_mult *= spot.mult_value

            if spot.tile is None and spot.mult_type == 'l':
                score += Tile(letter).score * spot.mult_value
            else:
                score += Tile(letter).score

        return score * word_mult
