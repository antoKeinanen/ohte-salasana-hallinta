from __future__ import annotations
from typing import Literal, TYPE_CHECKING
from tkinter import Frame
from view.locked_view import LockedView
from view.create_vault_view import CreateVaultView
from view.vault_view import VaultView
from view.create_credential_view import CreateCredentialView

if TYPE_CHECKING:
    from controller.app_controller import AppController

ViewName = Literal["locked", "create-vault", "vault", "create-credential"]


class ViewController:
    def __init__(self, app_controller: AppController):
        self.app_controller = app_controller
        self._views: dict[ViewName, Frame] = {
            "locked": LockedView,
            "create-vault": CreateVaultView,
            "vault": VaultView,
            "create-credential": CreateCredentialView,
        }
        self._current_view = "locked"
        self._active_view: Frame = self._views[self._current_view](self)
        self._active_view.grid(row=0, column=0, sticky="nsew")

    def swap_view(self, new_view: ViewName):
        self._active_view.grid_remove()

        self._current_view = new_view
        self._active_view = self._views[self._current_view](self)
        self._active_view.grid(row=0, column=0, sticky="nsew")
