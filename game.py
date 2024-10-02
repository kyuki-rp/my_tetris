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

    def put_block(self, x, y, shape):
        if self.tiles[y][x] == 0:
            self.tiles[y][x] = shape
        else:
            self.tiles[y][x] = 9

    def check(self):
        for y in range(self.tiles_size["y"]-1):
            if all(tile != 0 for tile in self.tiles[y]):
                new_line = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
                new_tiles = np.delete(self.tiles, y, 0)
                new_tiles = np.vstack((new_line, new_tiles))
                self.tiles = new_tiles


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
        blocks = self.get_blocks(self.shape)
        blocks = self.rotate(blocks, self.rot)
        return [Block(self.x + block.x, self.y + block.y) for block in blocks]

    @staticmethod
    def get_blocks(shape):
        # T型
        if shape == 2:
            return [Block(-1, 0), Block(0, 0), Block(0, -1), Block(1, 0)]
        # Z型
        elif shape == 3:
            return [Block(-1, -1), Block(0, -1), Block(0, 0), Block(1, 0)]
        # S型
        elif shape == 4:
            return [Block(-1, 0), Block(0, 0), Block(0, -1), Block(1, -1)]
        # L型
        elif shape == 5:
            return [Block(0, -1), Block(0, 0), Block(0, 1), Block(1, 1)]
        # J型
        elif shape == 6:
            return [Block(0, -1), Block(0, 0), Block(0, 1), Block(-1, 1)]
        # O型
        elif shape == 7:
            return [Block(-1, -1), Block(-1, 0), Block(0, 0), Block(0, -1)]
        # I型
        elif shape == 8:
            return [Block(-2, 0), Block(-1, 0), Block(0, 0), Block(1, 0)]

    @staticmethod
    def rotate(blocks, rot):
        rot = rot % 4
        for _ in range(rot):
            blocks = [Block(block.y, -block.x) for block in blocks]
        return blocks

    def next(self, controller):
        copy_tetromino = Tetromino(self.x, self.y, self.rot, self.shape)
        copy_tetromino.x += controller["x"]
        copy_tetromino.y += controller["y"]
        copy_tetromino.rot += controller["rot"]
        return copy_tetromino
