from row import Row


class ScorePad:
    def __init__(self):
        self.rows = self.create_rows()
        self.penalty = 0

    def create_rows(self):
        all_rows = []
        for color in ['red', 'yellow', 'blue', 'green']:
            all_rows.append(Row(color))

        return all_rows

    def add_penalty(self):
        self.penalty += 1
        if self.penalty < 4:
            return self.penalty
        else:
            return True

    def calculate_score(self):
        raise NotImplementedError
