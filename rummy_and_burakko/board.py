from .set_tiles import SetTiles


class Board():
    def __init__(self):
        self.sets = {}
        self.temp_sets = {}
        self.last_id = 0
        self.reused_tiles = []

    def add_new_play(self, sets):
        new_tile_set = {}
        new_id = self.last_id + 1
        for tile_set in sets:
            for tile in tile_set:
                if tile.set_id != 0:
                    new_set = new_tile_set.get(tile.set_id)
                    if not new_set:
                        mod_set = self.sets[tile.set_id]
                        new_set = SetTiles(mod_set.tiles)
                    new_set.remove_tile(tile)
                    new_tile_set.update({tile.set_id: new_set})
            new_tile_set.update({new_id: SetTiles(tile_set)})
            new_id += 1

        if self.valid_sets():
            self.sets = new_tile_set
            self.last_id = new_id
            for set_id, tile_set in new_tile_set.items():
                for tile in tile_set.tiles:
                    tile.assign_set_id(set_id)
            return True
        else:
            return False

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
