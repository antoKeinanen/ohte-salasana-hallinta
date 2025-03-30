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
        names = [Path(match).name.capitalize().removesuffix(".db") for match in matches]
        paths = [Path(match) for match in matches]
        return [Database(*db) for db in zip(paths, names)]


database_service = DatabaseService()
