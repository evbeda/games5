class Board():
    def __init__(self):
        self.sets = []

    def add_new_play(self, sets):
        for item in sets:
            self.sets.append(item)
