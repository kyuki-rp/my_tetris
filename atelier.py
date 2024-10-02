import tkinter as tk


class Atelier():
    def __init__(self, master):
        master.title("マイテトリス")
        self.canvas = tk.Canvas(master, width=400, height=400, bg="skyblue")
        self.canvas.pack()
        self.block_size = 20

    def delete_all(self):
        self.canvas.delete("all")

    def draw_tetromino(self, tetromino):
        blocks = tetromino.calc_blocks()
        for block in blocks:
            self.draw_block(block.x, block.y)

    def draw_field(self, field):
        for y in range(field.tiles_size["y"]):
            for x in range(field.tiles_size["x"]):
                block_type = field.tiles[y][x]
                if block_type != 0:
                    self.draw_block(x, y)

    def draw_block(self, x, y):
        self.canvas.create_rectangle(
            self.block_size * x,
            self.block_size * y,
            self.block_size * (x + 1),
            self.block_size * (y + 1),
            fill="grey"
        )
