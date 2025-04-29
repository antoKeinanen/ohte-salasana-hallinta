from __future__ import annotations
from typing import TYPE_CHECKING
from controller.view_controller import ViewController

if TYPE_CHECKING:
    from main import PasswordManagerApp
    from model.vault import Vault


class AppController:
    """
    Koko sovellusta ohjaava luokka.

    Attributes:
        app: viittaus ikkunaan
        view_controller: viittaus näkymä ajuriin
        active_vault: viittaus auki olevaan holviin jos sellainen on
        password: avoimen holvin salasana jos sellainen on
    """

    def __init__(self, app: PasswordManagerApp):
        """
        Alustaa luokan

        Args:
            app: viittaus ikkunaan johon sovellus piirretään
        """
        self.app = app
        self.view_controller = ViewController(self)
        self.active_vault: Vault | None = None
        self.password: str | None = None

    def run_main_loop(self):
        """Avaa ikkunan ja käsittelee tapahtumat"""
        self.app.mainloop()
