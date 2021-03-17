class Board():
    def __init__(self):
        self.sets = []

    def add_new_play(self, sets):
        if self.validate_sets(sets):
            for item in sets:
                self.sets.append(item)
            return True
        else:
            return False

    def validate_sets(self, sets):
        for item in sets:
            if not(item.is_valid()):
                return False
        return True
