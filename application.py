import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title("マイテトリス")
        self.canvas = tk.Canvas(master, width=400, height=400, bg="skyblue")
        self.canvas.pack()
        self.block_size = 20
        self.draw_block(0, 0)
        self.draw_block(20, 0)

    def draw_block(self, x, y):
        self.canvas.create_rectangle(
            x, y, x + self.block_size, y + self.block_size, fill="grey"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
