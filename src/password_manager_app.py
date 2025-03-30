from tkinter import Tk

class PasswordManagerApp(Tk):
    def __init__(self):
        super().__init__()

        start_width = 900
        start_height = 600
        min_width = 900
        min_height = 600

        self.geometry(f"{start_width}x{start_height}")
        self.minsize(width=min_width, height=min_height)
        self.title("Password manager")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
