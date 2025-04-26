from __future__ import annotations
from typing import TYPE_CHECKING
from controller.view_controller import ViewController

if TYPE_CHECKING:
    from main import PasswordManagerApp
    from model.vault import Vault


class AppController:
    def __init__(self, app: PasswordManagerApp):
        self.app = app
        self.view_controller = ViewController(self)
        self.active_vault: Vault | None = None
        self.password: str | None = None

    def run_main_loop(self):
        self.app.mainloop()
