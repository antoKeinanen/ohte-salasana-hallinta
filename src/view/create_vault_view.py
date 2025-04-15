from __future__ import annotations
from tkinter import Frame, Label, Entry, Button, messagebox
from typing import TYPE_CHECKING
from service.vault_service import vault_service

if TYPE_CHECKING:
    from controller.view_controller import ViewController


class CreateVaultView(Frame):
    def __init__(self, view_controller: ViewController, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._view_controller = view_controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.container = Frame(self)
        self.container.grid()

        self.heading = Label(self.container, text="Luo uusi holvi", font=("Arial", 16))
        self.heading.grid(pady=16)

        self.name_label = Label(self.container, text="Holvin nimi")
        self.name_label.grid(sticky="w")

        self.name_field = Entry(self.container, width=32)
        self.name_field.grid()

        self.password_label = Label(self.container, text="Salasana")
        self.password_label.grid(sticky="w")

        self.password_field = Entry(self.container, show="*", width=32)
        self.password_field.grid()

        self.button_container = Frame(self.container)
        self.button_container.grid(pady=16)

        self.cancel_button = Button(
            self.button_container,
            text="Peruuta",
            command=self._swap_to_locked_view,
        )
        self.cancel_button.pack(side="left", padx=8)

        self.create_button = Button(
            self.button_container,
            text="Luo holvi",
            command=self._create_vault,
        )
        self.create_button.pack(side="right", padx=8)

    def _swap_to_locked_view(self):
        self._view_controller.swap_view("locked")

    def _create_vault(self):
        name = self.name_field.get()
        error = vault_service.create_vault(name)
        if error:
            messagebox.showerror("Holvin luonti epäonnistui", error)
            return
        self._swap_to_locked_view()
