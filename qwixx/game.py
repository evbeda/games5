import player


class Game:
    def __init__(self, player_amount=1):
        self.player_amount = player_amount
        self.current_player = player.Player()
        self.dice_set = []

    def create_dice_set(self):
        raise NotImplementedError

    def remove_die(self):
        raise NotImplementedError
