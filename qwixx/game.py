import player


class Game:
    def __init__(self, player_amount=1):
        self.player_amount = player_amount
        self.current_player = player.Player()

    def create_dice_set(self):
        raise NotImplementedError

    def remove_die(self):
        raise NotImplementedError
