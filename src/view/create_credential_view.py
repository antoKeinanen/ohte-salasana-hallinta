from __future__ import annotations
from tkinter import Frame, Label, Entry, Button, messagebox
from typing import TYPE_CHECKING
from service.credential_service import CredentialService
from model.credential import Credential

if TYPE_CHECKING:
    from controller.view_controller import ViewController


class CreateCredentialView(Frame):
    def __init__(self, view_controller: ViewController, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._view_controller = view_controller
        self._vault = self._view_controller.app_controller.active_vault

        password = self._view_controller.app_controller.password
        self._credential_service = CredentialService(self._vault, password)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.container = Frame(self)
        self.container.grid()

        self.heading = Label(
            self.container, text="Luo uusi tunnus", font=("Arial", 16))
        self.heading.grid(pady=16)

        self.name_label = Label(self.container, text="Tunnuksen nimi")
        self.name_label.grid(sticky="w")

        self.name_field = Entry(self.container, width=32)
        self.name_field.grid()

        self.name_label = Label(self.container, text="Käyttäjänimi")
        self.name_label.grid(sticky="w")

        self.username_field = Entry(self.container, width=32)
        self.username_field.grid()

        self.password_label = Label(self.container, text="Salasana")
        self.password_label.grid(sticky="w")

        self.password_field = Entry(self.container, width=32)
        self.password_field.grid()

        self.button_container = Frame(self.container)
        self.button_container.grid(pady=16)

        self.cancel_button = Button(
            self.button_container,
            text="Peruuta",
            command=self._swap_to_vault_view,
        )
        self.cancel_button.pack(side="left", padx=8)

        self.create_button = Button(
            self.button_container,
            text="Luo tunnus",
            command=self._create_credential,
        )
        self.create_button.pack(side="right", padx=8)

    def _swap_to_vault_view(self):
        self._view_controller.swap_view("vault")

    def _create_credential(self):
        name = self.name_field.get()
        username = self.username_field.get()
        password = self.password_field.get()

        credential = Credential(-1, name, username, password)

        self._credential_service.add_credential(credential)

        self._swap_to_vault_view()
