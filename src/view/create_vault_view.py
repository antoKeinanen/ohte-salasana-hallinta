from __future__ import annotations
from tkinter import Frame, Label, Entry, Button
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.create_vault_controller import CreateVaultController


class CreateVaultView(Frame):
    def __init__(self, controller: CreateVaultController, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.container = Frame(self)
        self.container.grid()

        self.heading = Label(self.container, text="Luo uusi holvi", font=("", 16))
        self.heading.grid(pady=16)

        self.name_label = Label(self.container, text="Holvin nimi")
        self.name_label.grid(sticky="w")

        self.name_field = Entry(self.container, width=32)
        self.name_field.grid()

        self.password_label = Label(self.container, text="Salasana")
        self.password_label.grid(sticky="w")

        self.password_field = Entry(self.container, show="⏺", width=32)
        self.password_field.grid()

        self.button_container = Frame(self.container)
        self.button_container.grid(pady=16)

        self.cancel_button = Button(
            self.button_container,
            text="Peruuta",
            command=self._controller.swap_to_locked_view,
        )
        self.cancel_button.pack(side="left", padx=8)

        self.create_button = Button(
            self.button_container,
            text="Luo holvi",
            command=self._create_vault,
        )
        self.create_button.pack(side="right", padx=8)

    def _create_vault(self):
        name = self.name_field.get()
        self._controller.create_new_vault(name)
