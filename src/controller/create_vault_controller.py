from __future__ import annotations
from typing import TYPE_CHECKING
from tkinter import messagebox, Widget
from service.database_service import database_service
from view.create_vault_view import CreateVaultView

if TYPE_CHECKING:
    from controller.app_controller import AppController


class CreateVaultController:
    def __init__(self, _context: Widget, app_controller: AppController):
        self._app_controller = app_controller
        self.frame = CreateVaultView(self)

    def create_new_vault(self, name: str):
        error = database_service.create_database(name)
        if not error:
            self._app_controller.swap_view("locked")
            messagebox.showinfo(
                "Holvi luotu!", f"Holvi '{name}' luotu onnistuneesti")
            return

        messagebox.showerror("Holvin luonti epäonnistui!", error)

    def swap_to_locked_view(self):
        self._app_controller.swap_view("locked")
