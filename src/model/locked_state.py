from dataclasses import dataclass
from tkinter import StringVar
from model.database import Database


@dataclass
class LockedState:
    vaults: list[Database]
    vault_heading_content: StringVar
    selected_vault_index: int = 0
