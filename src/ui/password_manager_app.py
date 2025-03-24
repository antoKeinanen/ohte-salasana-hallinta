from textual.app import App
from textual.widgets import Footer, Header
from ui.views.locked_view import LockedView


class PasswordManagerApp(App):
    CSS_PATH = "styles/styles.tcss"

    def compose(self):
        yield Header()
        yield Footer()
        yield LockedView()
