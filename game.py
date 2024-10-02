import numpy as np


class Field():
    def __init__(self):
        self.tiles = np.array([
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ])
        self.tiles_size = {
            "x": self.tiles.shape[1],
            "y": self.tiles.shape[0],
        }

    def is_allowed(self, tetromino):
        blocks = tetromino.calc_blocks()
        return all(
            self.tiles[block.y][block.x] == 0
            for block in blocks
            if 0 <= block.x and block.x < self.tiles_size["x"]
            and 0 <= block.y and block.y < self.tiles_size["y"]
        )


class Block():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Tetromino():
    def __init__(self, x, y, rot=0, shape=2):
        self.x = x
        self.y = y
        self.rot = rot
        self.shape = shape

    def calc_blocks(self):
        blocks = [Block(-1, 0), Block(0, 0), Block(0, -1), Block(1, 0)]
        return [Block(self.x + block.x, self.y + block.y) for block in blocks]

    def copy(self):
        return Tetromino(self.x, self.y, self.rot, self.shape)