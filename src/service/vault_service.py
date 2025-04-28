from pathlib import Path
from glob import glob
import platformdirs
from model.vault import Vault
from service.database_service import db_execute_script, db_execute, db_fetch


class VaultService:
    """
    Luokka, joka hallinnoi holveja.

    Attributes:
        base_path: tiedostopolku, johon uudet holvit luodaan
    """

    def __init__(self, base_path: None | Path = None):
        """
        Alustaa luokan

        Args:
            base_path: tiedostopolku, johon uudet holvit luodaan. vapaaehtoinen. Oletus: platformdirs.user_data_path("password-manager")
        """

        self.base_path = Path(
            base_path or platformdirs.user_data_path("password-manager")
        )

    def discover_vaults(self):
        """
        Hakee kaikki holvit luokalle määritellystä tiedostopolusta

        Returns:
            vaults: lista löydettyjä holveja
        """

        if not self.base_path.exists():
            self.base_path.mkdir(parents=True)

        pattern = str(Path(self.base_path).joinpath("*.db"))
        matches = glob(pattern)

        paths = [Path(match) for match in matches]
        names = [path.name.removesuffix(".db") for path in paths]

        return [Vault(*vault, []) for vault in zip(names, paths)]

    def create_vault(self, name: str, password: str):
        """
        Luo uuden holvin luokalle määriteltyyn tiedostopolkuun.

        Args:
            name: holvin nimi. voi sisältää vain kirjaimia, numeroita ja merkkejä `-` tai `_`.
            password: holvin salasana
        """

        if not name:
            return "Syötä holville nimi"
        if not all(c.isalnum() or c in "-_" for c in name):
            return "Holvin nimi voi sisältää vain kirjaimia, numeroita, alaviivoja ja viivoja"

        if not password:
            return "Holvilla tulee olla salasana"

        vault_path = self.base_path.joinpath(f"{name}.db")
        if vault_path.exists():
            return f"Holvi {name} on jo olemassa"

        vault_path.touch()

        self._seed_vault_db(vault_path, password)

        self.discover_vaults()

        return None

    def _seed_vault_db(self, vault_path: Path, password: str):
        script = """
        CREATE TABLE credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        );

        CREATE TABLE authentication_check (
            hash TEXT NOT NULL
        ); 
        """
        db_execute_script(vault_path, script)

        sql_command = """
        INSERT INTO authentication_check (hash) VALUES (?);
        """
        db_execute(vault_path, sql_command, [password])

    def validate_authentication(self, vault_path: Path, password: str):
        """
        Tarkistaa vastaako annettu salasana holville määriteltyä salasanaa.

        Args:
            vault_path: holvin tiedostopolku
            password: testattava salasana
        """

        sql_command = """
        SELECT hash
        FROM authentication_check
        LIMIT 1;
        """
        hash = db_fetch(vault_path, sql_command, [])
        hash = hash[0][0]

        return password == hash


vault_service = VaultService()
