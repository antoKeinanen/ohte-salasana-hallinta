from pathlib import Path
from model.credential import Credential
from service.database_service import db_fetch_all, db_execute, db_fetch


class CredentialRepository:
    """Luokka, joka hallinnoi hovin tietokantaan kirjoittamista"""

    def get_all_credentials(self, path: Path):
        """
        Hakee tietokannasta kaikki holvissa olevat tunnukset.

        Args:
            path: holvin tiedostopolku

        Returns:
            credentials: lista holvissa olevista tunnuksista
        """
        command = "SELECT id, name, username, password FROM credentials;"

        credentials = db_fetch_all(path, command, [])

        return [Credential(*credential) for credential in credentials]

    def get_credential(self, path: Path, credential_id: int):
        """
        Hakee tietyn holvissa olevan tunnuksen

        Args:
            path: holvin tiedostopolku
            credential_id: haettavan tunnuksen id

        Returns:
            löydetty rivi tai None
        """
        command = """
        SELECT id, name, username, password
        FROM credentials
        WHERE id = ?;
        """

        return db_fetch(path, command, [credential_id])

    def create_credential(self, path: Path, credential: Credential):
        """
        Luo holviin uuden tunnuksen

        Args:
            path: holvin tiedostopolku
            credential: luotava tunnus. Id:llä ei ole merkitystä.
        """

        command = """
        INSERT INTO credentials 
            (name, username, password)
        VALUES (?, ?, ?);
        """

        return db_execute(
            path,
            command,
            [
                credential.name,
                credential.username,
                credential.password,
            ],
        )

    def delete_credential(self, path: Path, credential: Credential):
        """
        Poistaa holvista tunnuksen.

        Args:
            path: holvin tiedostopolku
            credential: poistettava tunnus
        """

        command = """
        DELETE FROM credentials
        WHERE id = ?;
        """

        db_execute(path, command, [credential.id])

    def update_credential(self, path: Path, credential: Credential):
        """
        Muokkaa holvissa olevaa tunnusta tunnuksen id:n perusteella

        Args:
            path: holvin tiedostopolku
            credential: muokattava tunnus
        """
        command = """
        UPDATE credentials
        SET
            name = ?,
            username = ?,
            password = ?
        WHERE id = ?;
        """

        db_execute(
            path,
            command,
            [
                credential.name,
                credential.username,
                credential.password,
                credential.id,
            ],
        )
