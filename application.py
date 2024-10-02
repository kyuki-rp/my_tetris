import tkinter as tk
from game import Field, Tetromino
from atelier import Atelier


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.atelier = Atelier(master)
        self.field = Field()
        self.tetromino = Tetromino(7, 1)

    def update(self):
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
            self.tetromino = Tetromino(7, 1)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.update()
    app.mainloop()
