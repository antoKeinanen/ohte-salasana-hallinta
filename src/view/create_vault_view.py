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

        container = Frame(self)
        container.grid()

        heading = Label(container, text="Luo uusi holvi", font=("Arial", 16))
        heading.grid(pady=16)

        name_label = Label(container, text="Holvin nimi")
        name_label.grid(sticky="w")

        self._name_field = Entry(container, width=32)
        self._name_field.grid()

        password_label = Label(container, text="Salasana")
        password_label.grid(sticky="w")

        self._password_field = Entry(container, show="*", width=32)
        self._password_field.grid()

        button_container = Frame(container)
        button_container.grid(pady=16)

        cancel_button = Button(
            button_container,
            text="Peruuta",
            command=self._swap_to_locked_view,
        )
        cancel_button.pack(side="left", padx=8)

        create_button = Button(
            button_container,
            text="Luo holvi",
            command=self._create_vault,
        )
        create_button.pack(side="right", padx=8)

    def _swap_to_locked_view(self):
        self._view_controller.swap_view("locked")

    def _create_vault(self):
        name = self._name_field.get()
        password = self._password_field.get()

        error = vault_service.create_vault(name, password)
        if error:
            messagebox.showerror("Holvin luonti epäonnistui", error)
            return

        self._swap_to_locked_view()
