from tkinter import Frame, Label


class CreateVaultView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.temp = Label(self, text="Luo uusi holvi")
        self.temp.pack()
