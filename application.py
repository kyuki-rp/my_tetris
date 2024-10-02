import tkinter as tk
from game import Field, Tetromino
from atelier import Atelier


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.atelier = Atelier(master)
        self.field = Field()
        self.tetromino = Tetromino(7, 1)
        self.controller = {"x": 0, "y": 0, "rot": 0}
        master.bind("<KeyPress>", self.key_event)

    def update(self):
        self.control_proc()
        self.drop_proc()
        self.atelier.delete_all()
        self.atelier.draw_field(self.field)
        self.atelier.draw_tetromino(self.tetromino)
        self.after(50, self.update)

    def drop_proc(self):
        future_tetromino = self.tetromino.copy()
        future_tetromino.y += 1
        if self.field.is_allowed(future_tetromino):
            self.tetromino.y += 1
        else:
            for block in self.tetromino.calc_blocks():
                self.field.put_block(block.x, block.y, self.tetromino.shape)
            self.tetromino = Tetromino(7, 1)

    def control_proc(self):
        future_tetromino = self.tetromino.copy()
        future_tetromino.x += self.controller["x"]
        future_tetromino.y += self.controller["y"]
        future_tetromino.rot += self.controller["rot"]
        if self.field.is_allowed(future_tetromino):
            self.tetromino.x += self.controller["x"]
            self.tetromino.y += self.controller["y"]
            self.tetromino.rot += self.controller["rot"]
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
