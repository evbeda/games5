class ScorePad:
    def __init__(self):
        self.penalty = 0

    def add_penalty(self):
        self.penalty += 1
        if self.penalty < 4:
            return self.penalty
        else:
            return True

    def calculate_score(self):
        raise NotImplementedError
