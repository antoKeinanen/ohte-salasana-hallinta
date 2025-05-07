from __future__ import annotations
from tkinter import Frame, Label, Entry, Button
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

        container = Frame(self)
        container.grid()

        heading = Label(container, text="Luo uusi tunnus", font=("Arial", 16))
        heading.grid(pady=16)

        name_label = Label(container, text="Tunnuksen nimi")
        name_label.grid(sticky="w")

        self._name_field = Entry(container, width=32)
        self._name_field.grid()

        name_label = Label(container, text="Käyttäjänimi")
        name_label.grid(sticky="w")

        self._username_field = Entry(container, width=32)
        self._username_field.grid()

        password_label = Label(container, text="Salasana")
        password_label.grid(sticky="w")

        self._password_field = Entry(container, width=32)
        self._password_field.grid()

        button_container = Frame(container)
        button_container.grid(pady=16)

        cancel_button = Button(
            button_container,
            text="Peruuta",
            command=self._swap_to_vault_view,
        )
        cancel_button.pack(side="left", padx=8)

        create_button = Button(
            button_container,
            text="Luo tunnus",
            command=self._create_credential,
        )
        create_button.pack(side="right", padx=8)

    def _swap_to_vault_view(self):
        self._view_controller.swap_view("vault")

    def _create_credential(self):
        name = self._name_field.get()
        username = self._username_field.get()
        password = self._password_field.get()

        credential = Credential(-1, name, username, password)

        self._credential_service.add_credential(credential)

        self._swap_to_vault_view()
