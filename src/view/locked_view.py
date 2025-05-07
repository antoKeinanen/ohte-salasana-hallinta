from __future__ import annotations
from tkinter import Frame, Listbox, Button, Label, Entry, StringVar, messagebox
from typing import TYPE_CHECKING
from service.vault_service import vault_service

if TYPE_CHECKING:
    from controller.view_controller import ViewController


class LockedView(Frame):
    def __init__(self, view_controller: ViewController, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._view_controller = view_controller
        self._vaults = vault_service.discover_vaults()

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._listbox = Listbox(self)
        for database in self._vaults:
            self._listbox.insert("end", database.name)
        self._listbox.grid(row=0, column=0, sticky="ns")
        self._listbox.bind("<<ListboxSelect>>",
                           self._on_listbox_selection_change)

        create_vault_button = Button(
            self,
            text="+ Luo uusi holvi",
            command=self._on_create_vault_button_click,
        )
        create_vault_button.grid(row=1, column=0, sticky="nsew")

        right_container = Frame(self)
        right_container.grid(row=0, column=1, rowspan=2)

        if not self._vaults:
            header = Label(
                right_container,
                text="Luo uusi hovi painamalla luo uusi holvi nappia",
            )
            header.grid(row=0, column=0, sticky="ew", pady=16)
            return

        self._selected_vault_index = 0
        self._listbox.activate(self._selected_vault_index)

        self._header_text = StringVar(
            self, f"Avaa {self._vaults[self._selected_vault_index].name}"
        )

        header = Label(
            right_container,
            textvariable=self._header_text,
            font=("Arial", 16),
        )
        header.grid(row=0, column=0, sticky="ew", pady=16)

        password_label = Label(right_container, text="Salasana:")
        password_label.grid(row=1, column=0, sticky="w")

        self._password_field = Entry(right_container, show="*", width=32)
        self._password_field.grid(row=2, column=0)

        submit_button = Button(
            right_container,
            text="Avaa holvi",
            command=self._on_open_vault_button_click,
        )
        submit_button.grid(row=3, column=0, pady=16, sticky="w")

    def _on_listbox_selection_change(self, _):
        index = self._listbox.curselection()
        if index:
            (self._selected_vault_index,) = index
            self._header_text.set(
                f"Avaa {self._vaults[self._selected_vault_index].name}"
            )

    def _on_create_vault_button_click(self):
        self._view_controller.swap_view("create-vault")

    def _on_open_vault_button_click(self):
        vault = self._vaults[self._selected_vault_index]
        password = self._password_field.get()

        is_authenticated = vault_service.validate_authentication(
            vault.path, password)

        if not is_authenticated:
            messagebox.showerror(
                "Virheellinen salasana", "Syöttämäsi salasana on väärä."
            )
            return

        self._view_controller.app_controller.active_vault = vault
        self._view_controller.app_controller.password = password
        self._view_controller.swap_view("vault")
