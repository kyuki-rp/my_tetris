import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title("マイテトリス")
        self.canvas = tk.Canvas(master, width=400, height=400, bg="skyblue")
        self.canvas.pack()
        self.block_size = 20
        for y in range(0, 200, 20):
            for x in range(0, 200, 20):
                self.draw_block(x, y)

    def draw_block(self, x, y):
        self.canvas.create_rectangle(
            x, y, x + self.block_size, y + self.block_size, fill="grey"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
