from tkinter import Frame
from controller.locked_controller import LockedController
from view.create_vault_view import CreateVaultView
from view.locked_view import LockedView
from view.password_manager_app import PasswordManagerApp


class AppController:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(AppController, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.app = PasswordManagerApp()

        locked_controller = LockedController(self.app, self)

        self.views: dict[str, Frame] = {
            "locked": LockedView(locked_controller, master=self.app),
            "create-vault": CreateVaultView(master=self.app),
        }
        self.active_view = "locked"

        self.views["locked"].grid(row=0, column=0, sticky="nsew")

    def swap_view(self, new_view: str):
        self.views[self.active_view].destroy()
        self.views[new_view].grid(row=0, column=0, sticky="nsew")
        self.active_view = new_view

    def run_main_loop(self):
        self.app.mainloop()
