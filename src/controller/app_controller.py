from controller.locked_controller import LockedController
from controller.create_vault_controller import CreateVaultController
from password_manager_app import PasswordManagerApp


class AppController:
    def __init__(self):
        self.app = PasswordManagerApp()

        self.controllers = {
            "locked": LockedController,
            "create-vault": CreateVaultController,
        }
        self.active_view = "locked"
        self.active_controller = self.controllers[self.active_view](
            self.app, self)
        self.active_controller.frame.grid(row=0, column=0, sticky="nsew")

    def swap_view(self, new_view: str):
        self.active_controller.frame.grid_remove()

        self.active_view = new_view
        self.active_controller = self.controllers[self.active_view](
            self.app, self)
        self.active_controller.frame.grid(row=0, column=0, sticky="nsew")

    def run_main_loop(self):
        self.app.mainloop()
