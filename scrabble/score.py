class Score:

    # def score_word(self):
    #     pass
class Score:
    #     def score_word(self):
    #         pass
    # para palabras horizontales, hacer verificacion horizontal para q no toque letra despues
    # para palabras verticales, hacer verificacion vertical para q no toque otra letra despues

    # mi palabra original es vertical
    @staticmethod
    def search_horiz_word(self, word, row, col):
        len_word = len(word)
        end_word = row + len_word
        for i in range(row, end_word):
            if [i][col - 1] == 'algo' or [i][col + 1] == 'algo':
                # recorrer para izquierda
                # luego recorrer para derecha
                pass

    # mi palabra original es horizontal
    @staticmethod
    def search_vert_word(self, word, row, col):
        len_word = len(word)
        end_word = row + len_word
        for i in range(row, end_word):
            if [i][col - 1] == 'algo' or [i][col + 1] == 'algo':
                # recorrer para izquierda
                # luego recorrer para derecha
                pass

    # def search_horiz_word(self):
    #     pass

    # def search_vert_word(self):
    #     pass

    @staticmethod
    def multiply_score(spots):
        score = 0
        word_mult = 1
        for spot in spots:
            if spot.mult_not_used and spot.mult_type == 'w':
                word_mult *= spot.mult_value
            if spot.mult_not_used and spot.mult_type == 'l':
                score += spot.tile.score * spot.mult_value
            else:
                score += spot.tile.score
            spot.mult_not_used = False
        return score * word_mult
