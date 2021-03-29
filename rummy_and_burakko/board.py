from .set_tiles import SetTiles


class Board():
    def __init__(self):
        self.sets = {}
        self.temp_sets = {}
        self.last_id = 0
        self.reused_tiles = []

    def get_board(self):
        return '\n'.join([
            f'{index}: {tile_set.get_tiles()}'
            for index, tile_set in self.sets.items()
        ])

    def get_reused_tiles(self, start_index):
        return '   '.join([
            f'{index}:{tile.color}{tile.number}'
            for index, tile in enumerate(self.reused_tiles, start_index)
        ])

    def temporary_sets(self):
        self.temp_sets = self.sets.copy()

    def valid_sets(self):
        return all(
            [value_set.is_valid() for value_set in self.temp_sets.values()]
        )

    def validate_turn(self):
        self.sets = self.temp_sets.copy()

    def give_one_tile_from_board(self, set_id, index):
        if len(self.sets[set_id].tiles) > 0:
            self.reused_tiles.append(
                    self.sets[set_id].extract_one_tile(index)
                )
        else:
            raise Exception

    def place_new_set(self, tiles):
        self.last_id = self.last_id + 1
        for tile in tiles:
            tile.set_id = self.last_id
        self.sets[self.last_id] = SetTiles(tiles)

    def get_a_reused_tile(self, index):
        return self.reused_tiles[index]

    def remove_reused_tile(self, index):
        self.reused_tiles.pop(index)
