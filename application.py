import random
import tkinter as tk
from game import Field, Tetromino
from atelier import Atelier


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.atelier = Atelier(master)
        self.field = Field()
        self.tetromino = self.make_tetromino()
        self.controller = {"x": 0, "y": 0, "rot": 0}
        master.bind("<KeyPress>", self.key_event)
        self.count = 0

    def make_tetromino(self):
        return Tetromino(7, 1, 0, random.choice([2, 3, 4, 5, 6, 7, 8]))

    def update(self):
        if max(self.field.tiles.flatten()) == 9:
            self.atelier.draw_game_over()
        else:
            self.count += 1
            self.control_proc()
            self.fill_proc()
            if self.count % 10 == 0:
                self.drop_proc()
            self.atelier.delete_all()
            self.atelier.draw_field(self.field)
            self.atelier.draw_tetromino(self.tetromino)
            self.after(50, self.update)

    def fill_proc(self):
        self.field.check()

    def drop_proc(self):
        future_tetromino = self.tetromino.next({"x": 0, "y": 1, "rot": 0})
        if self.field.is_allowed(future_tetromino):
            self.tetromino = future_tetromino
        else:
            for block in self.tetromino.calc_blocks():
                self.field.put_block(block.x, block.y, self.tetromino.shape)
            self.tetromino = self.make_tetromino()

    def control_proc(self):
        future_tetromino = self.tetromino.next(self.controller)
        if self.field.is_allowed(future_tetromino):
            self.tetromino = future_tetromino
        self.controller = {"x": 0, "y": 0, "rot": 0}

    def key_event(self, event):
        key = event.keysym
        if key == "1":
            self.controller = {"x": -1, "y": 0, "rot": 0}
        if key == "2":
            self.controller = {"x": 0, "y": 1, "rot": 0}
        if key == "3":
            self.controller = {"x": 1, "y": 0, "rot": 0}
        if key == "4":
            self.controller = {"x": 0, "y": 0, "rot": 1}


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.update()
    app.mainloop()
