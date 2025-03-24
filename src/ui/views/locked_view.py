from textual.containers import Vertical, Center, Horizontal, Container
from textual.widgets import Button, ListView, ListItem, Label, Input
from textual.reactive import reactive
from textual.widget import Widget

from util.discover_databases import discover_databases


class LockedView(Horizontal):
    def compose(self):
        yield LockedAside()
        yield LockedUnlockVault()


class LockedAside(Vertical):
    def compose(self):
        yield DatabaseList()
        yield CreateVaultButton("+ Uusi holvi")


class CreateVaultButton(Button):
    def press(self):
        pass  # TODO
        return super().press()


class DatabaseList(ListView):
    def compose(self):
        self.databases = discover_databases()

        for db_path, db_name in self.databases:
            yield ListItem(Label(db_name))

    def watch_index(self, old_index, new_index):
        self.parent.parent.query_one(
            LockedVaultTitle
        ).active_database_name = self.databases[new_index][1]
        return super().watch_index(old_index, new_index)


class LockedUnlockVault(Center):
    def compose(self):
        yield Container(
            LockedVaultTitle(),
            Input(placeholder="Salasana", password=True),
            Button("Avaa holvi", classes="open-button"),
            classes="password-container",
        )


class LockedVaultTitle(Widget):
    active_database_name = reactive(0, layout=True)

    def render(self):
        return f"Avaa {self.active_database_name}"
