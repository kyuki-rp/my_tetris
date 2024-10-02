import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title("マイテトリス")
        self.canvas = tk.Canvas(master, width=400, height=400, bg="skyblue")
        self.canvas.pack()
        self.draw_block()

    def draw_block(self):
        self.canvas.create_rectangle(0, 0, 20, 20, fill="grey")


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
