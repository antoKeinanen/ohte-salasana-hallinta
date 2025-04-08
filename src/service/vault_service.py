from pathlib import Path
from glob import glob
import platformdirs
from model.vault import Vault
from service.database_service import db_execute_script


class VaultService:
    def __init__(self, base_path: None | Path = None):
        self.base_path = Path(
            base_path or platformdirs.user_data_path("password-manager")
        )

    def discover_vaults(self):
        if not self.base_path.exists():
            self.base_path.mkdir(parents=True)

        pattern = str(Path(self.base_path).joinpath("*.db"))
        matches = glob(pattern)

        paths = [Path(match) for match in matches]
        names = [path.name.removesuffix(".db") for path in paths]

        return [Vault(*vault, []) for vault in zip(names, paths)]

    def create_vault(self, name: str):
        if not name:
            return "Syötä holville nimi"
        if not all(c.isalnum() or c in "-_" for c in name):
            return "Holvin nimi voi sisältää vain kirjaimia, numeroita, alaviivoja ja viivoja"

        vault_path = self.base_path.joinpath(f"{name}.db")
        if vault_path.exists():
            return f"Holvi {name} on jo olemassa"

        vault_path.touch()

        self._seed_vault_db(vault_path)

        self.discover_vaults()

        return None

    def _seed_vault_db(self, vault_path: Path):
        script = """
        CREATE TABLE credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        );
        """
        db_execute_script(vault_path, script)


vault_service = VaultService()
