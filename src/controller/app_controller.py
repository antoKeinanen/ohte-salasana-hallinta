from __future__ import annotations
from typing import TYPE_CHECKING
from controller.view_controller import ViewController

if TYPE_CHECKING:
    from main import PasswordManagerApp


class AppController:
    def __init__(self, app: PasswordManagerApp):
        self.app = app
        self.view_controller = ViewController()

    def run_main_loop(self):
        self.app.mainloop()
