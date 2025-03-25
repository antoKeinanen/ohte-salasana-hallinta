from model.locked_state import LockedState
from util.discover_databases import discover_vaults
from tkinter import StringVar, Widget


class LockedController:
    def __init__(self, context: Widget):
        vaults = discover_vaults()
        vault_heading_content = StringVar(context, "")
        if len(vaults):
            vault_heading_content.set(f"Avaa {vaults[0][1]}")

        self.state = LockedState(vaults, vault_heading_content)

    def set_active_vault(self, index: int):
        self.state.selected_database = index
        self.state.vault_heading_content.set(f"Avaa {self.state.vaults[index][1]}")
