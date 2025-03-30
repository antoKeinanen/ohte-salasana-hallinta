from pathlib import Path
import platformdirs
from glob import glob
from model.database import Database


class DatabaseService:
    def __init__(self, base_path: None | Path = None):
        self.base_path = Path(
            base_path or platformdirs.user_data_path("password-manager")
        )

    def discover_databases(self):
        if not self.base_path.exists():
            self.base_path.mkdir(parents=True)

        db_pattern = str(Path(self.base_path).joinpath("*.db"))
        matches = glob(db_pattern)
        names = [Path(match).name.removesuffix(".db") for match in matches]
        paths = [Path(match) for match in matches]
        return [Database(*db) for db in zip(paths, names)]

    def create_database(self, name: str):
        if not name:
            return "Syötä holville nimi"
        if not all(c.isalnum() or c in "-_" for c in name):
            return "Holvin nimi voi sisältää vain kirjaimia, numeroita, alaviivoja ja viivoja"

        db_path = self.base_path.joinpath(f"{name}.db")
        if db_path.exists():
            return f"Holvi {name} on jo olemassa"

        db_path.touch()

        self.discover_databases()


database_service = DatabaseService()
