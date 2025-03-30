from controller.locked_controller import LockedController
from password_manager_app import PasswordManagerApp
from controller.create_vault_controller import CreateVaultController


class AppController:
    def __init__(self):
        self.app = PasswordManagerApp()

        self.controllers = {
            "locked": LockedController(self.app, self),
            "create-vault": CreateVaultController(),
        }
        self.active_view = "locked"

        self.controllers[self.active_view].frame.grid(row=0, column=0, sticky="nsew")

    def swap_view(self, new_view: str):
        self.controllers[self.active_view].frame.destroy()
        self.controllers[new_view].frame.grid(row=0, column=0, sticky="nsew")
        self.active_view = new_view

    def run_main_loop(self):
        self.app.mainloop()
