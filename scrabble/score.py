class Score:

    # mi palabra original es vertical
    @staticmethod
    def search_horiz_word(self, word, row, col, direccion, spots):
        len_word = len(word)
        end_word = row + len_word
        for i in range(row, end_word):
            if spots[i][col - 1].tile is not None:
                self.metodo_nuevo(direccion, i, col - 1)
            elif spots[i][col + 1].tile is not None:
                self.metodo_nuevo(direccion, i, col + 1)

    # mi palabra original es horizontal
    @staticmethod
    def search_vert_word(self, word, row, col, direccion, spots):
        len_word = len(word)
        end_word = col + len_word
        for i in range(row, end_word):
            if spots[row - 1][i].tile is not None:
                self.metodo_nuevo(direccion, row - 1, i, spots)
            elif spots[i][col + 1].tile is not None:
                self.metodo_nuevo(direccion, row + 1, i, spots)

    @staticmethod
    def nuevo_metodo(direccion, row, col, spots):
        pass

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
