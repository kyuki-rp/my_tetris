import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title("マイテトリス")
        self.canvas = tk.Canvas(master, width=400, height=400, bg="skyblue")
        self.canvas.pack()
        self.block_size = 20
        self.draw_field()

    def draw_field(self):
        for y in range(0, 10):
            for x in range(0, 10):
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
    app.mainloop()
