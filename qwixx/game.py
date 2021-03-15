import player


class Game:
    def __init__(self, player_amount=1):
        if player_amount not in range(1, 5):
            raise Exception

        self.players = [player.Player() for _ in range(player_amount)]
        self.current_player = 0
        self.dice_set = {}

    def create_dice_set(self):
        raise NotImplementedError

    def remove_die(self, color):
        for index, die in enumerate(self.dice_set):
            if die.color == color:
                self.dice_set.pop(index)
                break
