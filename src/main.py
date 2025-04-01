from tkinter import Tk, font
from controller.app_controller import AppController


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

        self.default_font = font.nametofont("TkDefaultFont")
        self.default_font.configure(family="Roboto", weight=font.NORMAL)

        self.text_font = font.nametofont("TkTextFont")
        self.text_font.configure(family="Roboto")


if __name__ == "__main__":
    app = PasswordManagerApp()
    app_controller = AppController(app)
    app_controller.run_main_loop()
