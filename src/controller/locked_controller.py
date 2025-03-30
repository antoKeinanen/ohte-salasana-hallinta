from __future__ import annotations
from model.locked_state import LockedState
from util.discover_databases import discover_vaults
from tkinter import StringVar, Widget
from view.locked_view import LockedView
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.app_controller import AppController


class LockedController:
    def __init__(self, context: Widget, app_controller: AppController):
        self._app_controller = app_controller

        vaults = discover_vaults()
        vault_heading_content = StringVar(context, "")
        if len(vaults):
            vault_heading_content.set(f"Avaa {vaults[0][1]}")

        self.state = LockedState(vaults, vault_heading_content)

        self.frame = LockedView(self)

    def set_active_vault(self, index: int):
        self.state.selected_database = index
        self.state.vault_heading_content.set(f"Avaa {self.state.vaults[index][1]}")

    def swap_to_create_vault_view(self):
        self._app_controller.swap_view("create-vault")
