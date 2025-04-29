from __future__ import annotations
from tkinter import Frame, Label, Entry, Button, StringVar
from typing import TYPE_CHECKING
from service.credential_service import CredentialService
from model.credential import Credential

if TYPE_CHECKING:
    from controller.view_controller import ViewController


class UpdateCredentialView(Frame):
    def __init__(
        self, view_controller: ViewController, *args, credential: Credential, **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.credential = credential

        self._view_controller = view_controller
        self._vault = self._view_controller.app_controller.active_vault
        self._credential_service = CredentialService(self._vault)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.container = Frame(self)
        self.container.grid()

        self.heading = Label(
            self.container, text="Muokkaa tunnusta", font=("Arial", 16)
        )
        self.heading.grid(pady=16)

        self.name_label = Label(self.container, text="Tunnuksen nimi")
        self.name_label.grid(sticky="w")

        name_value = StringVar(self, self.credential.name)
        self.name_field = Entry(self.container, width=32,
                                textvariable=name_value)
        self.name_field.grid()

        self.username_label = Label(self.container, text="Käyttäjänimi")
        self.username_label.grid(sticky="w")

        username_value = StringVar(self, self.credential.username)
        self.username_field = Entry(
            self.container, width=32, textvariable=username_value
        )
        self.username_field.grid()

        self.password_label = Label(self.container, text="Salasana")
        self.password_label.grid(sticky="w")

        password_value = StringVar(self, self.credential.password)
        self.password_field = Entry(
            self.container, width=32, textvariable=password_value
        )
        self.password_field.grid()

        self.button_container = Frame(self.container)
        self.button_container.grid(pady=16)

        self.cancel_button = Button(
            self.button_container,
            text="Peruuta",
            command=self._swap_to_vault_view,
        )
        self.cancel_button.pack(side="left", padx=8)

        self.update_button = Button(
            self.button_container,
            text="Muokkaa tunnusta",
            command=self._update_credential,
        )
        self.update_button.pack(side="right", padx=8)

    def _swap_to_vault_view(self):
        self._view_controller.swap_view("vault")

    def _update_credential(self):
        name = self.name_field.get()
        username = self.username_field.get()
        password = self.password_field.get()

        credential = Credential(self.credential.id, name, username, password)

        self._credential_service.update_credential(credential)

        self._swap_to_vault_view()
