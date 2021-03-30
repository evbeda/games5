class Score:

    # mi palabra original es vertical
    @staticmethod
    def define_direction(word, row, col, direction, spots):
        if direction is True:
            return Score.search_vert_letter(word, row, col, spots)
        else:
            return Score.search_horiz_letter(word, row, col, spots)

    @staticmethod
    def search_horiz_letter(word, row, col, spots):
        len_word = len(word)
        end_word = row + len_word
        list_words = []
        for i in range(row, end_word):
            if spots[i][col - 1].tile is not None:
                list_words.append(Score.search_horiz_word(i, col - 1, spots))
            elif spots[i][col + 1].tile is not None:
                list_words.append(Score.search_horiz_word(i, col + 1, spots))
        return list_words

    # mi palabra original es horizontal
    @staticmethod
    def search_vert_letter(word, row, col, spots):
        len_word = len(word)
        end_word = col + len_word
        list_words = []
        for i in range(row, end_word):
            if spots[row - 1][i].tile is not None:
                list_words.append(Score.search_vert_word(row - 1, i, spots))
            elif spots[i][col + 1].tile is not None:
                list_words.append(Score.search_vert_word(row + 1, i, spots))
        return list_words

    # metodo para obtener nuevas palabras formadas
    @staticmethod
    def search_horiz_word(row, col, spots):
        sublist1 = []
        sublist2 = []
        sublist3 = []
        for i in range(col, -1, -1):
            if spots[row][i].tile is not None:
                sublist1.append(spots[row][col])
            else:
                break
        for i in range(col, 15, 1):
            if spots[row][i].tile is not None:
                sublist2.append(spots[row][col])
            else:
                break
        sublist3 = sublist1[::-1] + sublist2
        return sublist3

    @staticmethod
    def search_vert_word(row, col, spots):
        sublist1 = []
        sublist2 = []
        sublist3 = []
        for i in range(row, -1, -1):
            if spots[i][col].tile is not None:
                sublist1.append(spots[row][col])
            else:
                break
        for i in range(row, 15, 1):
            if spots[i][col].tile is not None:
                sublist2.append(spots[row][col])
            else:
                break
        sublist3 = sublist1[::-1] + sublist2
        return sublist3

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
