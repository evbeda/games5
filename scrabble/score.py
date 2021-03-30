class Score:

    # def score_word(self):
    #     pass

    # def search_horiz_word(self):
    #     pass

    # def search_vert_word(self):
    #     pass

    @staticmethod
    def multiply_score(spots):
        score = 0
        word_mult = 1
        for spot in spots:
            if spot.mult_not_used:
                if spot.mult_type == 'w':
                    word_mult *= spot.mult_value
                if spot.mult_type == 'l':
                    score += spot.tile.score * spot.mult_value
                else:
                    score += spot.tile.score
            else:
                score += spot.tile.score
            spot.mult_not_used = False
        return score * word_mult
