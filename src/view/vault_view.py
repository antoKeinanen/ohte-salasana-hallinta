from __future__ import annotations
from tkinter import Frame, Listbox, Button, Label, Entry, StringVar
from typing import TYPE_CHECKING
from service.credential_service import CredentialService

if TYPE_CHECKING:
    from controller.view_controller import ViewController


class VaultView(Frame):
    def __init__(self, view_controller: ViewController, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._view_controller = view_controller
        self._vault = self._view_controller.app_controller.active_vault
        self._credential_service = CredentialService(self._vault)
        self._credential_service.get_all_credentials()
        self._credentials = self._vault.credentials

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.listbox = Listbox(self)
        for credential in self._credentials:
            self.listbox.insert("end", credential.name)
        self.listbox.grid(row=0, column=0, sticky="ns")
        self.listbox.bind("<<ListboxSelect>>", self._on_listbox_selection_change)

        self.create_vault_button = Button(
            self,
            text="+ Luo uusi tunnus",
            command=self._on_create_vault_button_click,
        )
        self.create_vault_button.grid(row=1, column=0, sticky="nsew")

        self.right_container = Frame(self)
        self.right_container.grid(row=0, column=1, rowspan=2)

        if not self._credentials:
            self.header = Label(
                self.right_container,
                text="Luo uusi tunnus painamalla 'Luo uusi tunnus' nappia",
            )
            self.header.grid(row=0, column=0, sticky="ew", pady=16)
            return

        self._selected_vault_index = 0
        self.listbox.activate(self._selected_vault_index)

        self._header_text = StringVar(
            self, f"Avaa {self._credentials[self._selected_vault_index].name}"
        )

        self.header = Label(
            self.right_container,
            textvariable=self._header_text,
            font=("Arial", 16),
        )
        self.header.grid(row=0, column=0, sticky="ew", pady=16)

        self.password_label = Label(self.right_container, text="Salasana:")
        self.password_label.grid(row=1, column=0, sticky="w")

        self.password_field = Entry(self.right_container, show="*", width=32)
        self.password_field.grid(row=2, column=0)

        self.submit_button = Button(self.right_container, text="Avaa holvi")
        self.submit_button.grid(row=3, column=0, pady=16, sticky="w")

    def _on_listbox_selection_change(self, _):
        index = self.listbox.curselection()
        if index:
            (self._selected_vault_index,) = index

    def _on_create_vault_button_click(self):
        self._view_controller.swap_view("create-credential")
