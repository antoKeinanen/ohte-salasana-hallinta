from dataclasses import dataclass
from tkinter import StringVar


@dataclass
class LockedState:
    vaults: list[tuple[str, str]]
    vault_heading_content: StringVar
    selected_vault_index: int = 0
