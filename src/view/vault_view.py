from __future__ import annotations
from tkinter import Frame, Listbox, Button, Label, StringVar
from typing import TYPE_CHECKING
from service.credential_service import CredentialService

if TYPE_CHECKING:
    from controller.view_controller import ViewController


class VaultView(Frame):
    def __init__(self, view_controller: ViewController, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._view_controller = view_controller
        self._vault = self._view_controller.app_controller.active_vault

        password = self._view_controller.app_controller.password
        self._credential_service = CredentialService(self._vault, password)

        self._credential_service.get_all_credentials()
        self._credentials = self._vault.credentials

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        close_vault_button = Button(
            self, text="Sulje holvi", command=self._on_close_vault_button_click
        )
        close_vault_button.grid(row=0, column=0, sticky="nsew")

        self._listbox = Listbox(self)
        self._listbox.grid(row=1, column=0, sticky="ns")
        self._listbox.bind("<<ListboxSelect>>",
                           self._on_listbox_selection_change)

        create_vault_button = Button(
            self,
            text="+ Luo uusi tunnus",
            command=self._on_create_credential_button_click,
        )
        create_vault_button.grid(row=2, column=0, sticky="nsew")

        self._right_container = Frame(self)
        self._right_container.grid(row=0, column=1, rowspan=2)

        if not self._credentials:
            header = Label(
                self._right_container,
                text="Luo uusi tunnus painamalla 'Luo uusi tunnus' nappia",
            )
            header.grid(row=0, column=0, sticky="ew", pady=16)
            return

        self._selected_vault_index = 0
        self._selected_credential = self._credentials[self._selected_vault_index]

        self._username_text = StringVar(
            self, f"Käyttäjätunnus: {self._selected_credential.username}"
        )
        self._password_text = StringVar(
            self, f"Salasana: {self._selected_credential.password}"
        )

        username_label = Label(
            self._right_container, textvariable=self._username_text
        )
        username_label.grid(row=0, column=0, sticky="ew")

        password_label = Label(
            self._right_container, textvariable=self._password_text
        )
        password_label.grid(row=1, column=0, sticky="ew")

        button_row = Frame(self._right_container)
        button_row.grid(pady=16)

        delete_button = Button(
            button_row, text="Poista", command=self._on_delete_button_click
        )
        delete_button.grid()

        update_button = Button(
            button_row,
            text="Muokkaa",
            command=self._on_update_credential_button_click,
        )
        update_button.grid()

        self._refresh_view()

    def _refresh_view(self):
        self._listbox.delete(0, "end")
        if not self._credentials:
            for child in [*self.self.right_container.children.values()]:
                child.destroy()

            self.header = Label(
                self.self.right_container,
                text="Luo uusi tunnus painamalla 'Luo uusi tunnus' nappia",
            )
            self.header.grid(row=0, column=0, sticky="ew", pady=16)
            return

        for credential in self._credentials:
            self._listbox.insert("end", credential.name)

        self._selected_credential = self._credentials[self._selected_vault_index]
        self._listbox.activate(self._selected_vault_index)
        self._update_credential_text()

    def _update_credential_text(self):
        self._username_text.set(
            f"Käyttäjätunnus: {self._selected_credential.username}")
        self._password_text.set(
            f"Salasana: {self._selected_credential.password}")

    def _on_listbox_selection_change(self, _):
        selection = self._listbox.curselection()
        if selection:
            self._selected_vault_index = selection[0]
            self._selected_credential = self._credentials[self._selected_vault_index]
            self._update_credential_text()

    def _on_delete_button_click(self):
        self._credential_service.delete_credential(self._selected_credential)
        self._credentials = self._vault.credentials
        self._selected_vault_index = 0
        self._refresh_view()

    def _on_create_credential_button_click(self):
        self._view_controller.swap_view("create-credential")

    def _on_update_credential_button_click(self):
        self._view_controller.swap_view(
            "update-credential", credential=self._selected_credential
        )

    def _on_close_vault_button_click(self):
        self._view_controller.app_controller.active_vault = None
        self._view_controller.swap_view("locked")
