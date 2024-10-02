import tkinter as tk
from game import Field, Tetromino


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title("マイテトリス")
        self.canvas = tk.Canvas(master, width=400, height=400, bg="skyblue")
        self.canvas.pack()
        self.block_size = 20
        self.field = Field()
        self.tetromino = Tetromino(7, 1)

    def update(self):
        self.drop_proc()
        self.delete_all()
        self.draw_field(self.field)
        self.draw_tetromino(self.tetromino)
        self.after(50, self.update)

    def drop_proc(self):
        future_tetromino = self.tetromino.copy()
        future_tetromino.y += 1
        if self.field.is_allowed(future_tetromino):
            self.tetromino.y += 1
        else:
            self.tetromino = Tetromino(7, 1)

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


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.update()
    app.mainloop()
