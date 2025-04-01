from typing import Literal
from tkinter import Frame
from view.locked_view import LockedView
from view.create_vault_view import CreateVaultView

ViewName = Literal["locked", "create-vault"]


class ViewController:
    def __init__(self):
        self._views: dict[ViewName, Frame] = {
            "locked": LockedView,
            "create-vault": CreateVaultView
        }
        self._current_view = "locked"
        self._active_view: Frame = self._views[self._current_view](self)
        self._active_view.grid(row=0, column=0, sticky="nsew")

    def swap_view(self, new_view: ViewName):
        self._active_view.grid_remove()

        self._current_view = new_view
        self._active_view = self._views[self._current_view](self)
        self._active_view.grid(row=0, column=0, sticky="nsew")
