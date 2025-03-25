from model.locked_state import LockedState
from util.discover_databases import discover_vaults
from tkinter import StringVar, Widget


class LockedController:
    def __init__(self, context: Widget, app_controller):
        self._app_controller = app_controller

        vaults = discover_vaults()
        vault_heading_content = StringVar(context, "")
        if len(vaults):
            vault_heading_content.set(f"Avaa {vaults[0][1]}")

        self.state = LockedState(vaults, vault_heading_content)

    def set_active_vault(self, index: int):
        self.state.selected_database = index
        self.state.vault_heading_content.set(f"Avaa {self.state.vaults[index][1]}")

    def swap_to_create_vault_view(self):
        self._app_controller.swap_view("create-vault")
