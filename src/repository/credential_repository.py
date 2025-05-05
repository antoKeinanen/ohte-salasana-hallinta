from pathlib import Path
from model.credential import Credential
from service.database_service import db_fetch_all, db_execute, db_fetch
from util.crypto import decrypt, encrypt


class CredentialRepository:
    """Luokka, joka hallinnoi hovin tietokantaan kirjoittamista"""

    def _encrypt_credential(self, credential: Credential, password: str):
        credential.username = encrypt(credential.username, password)
        credential.name = encrypt(credential.name, password)
        credential.password = encrypt(credential.password, password)
        return credential

    def _decrypt_credential(self, credential: Credential, password: str):
        credential.username = decrypt(credential.username, password)
        credential.name = decrypt(credential.name, password)
        credential.password = decrypt(credential.password, password)
        return credential

    def get_all_credentials(self, path: Path, password: str):
        """
        Hakee tietokannasta kaikki holvissa olevat tunnukset.

        Args:
            path: holvin tiedostopolku
            password: salasana

        Returns:
            credentials: lista holvissa olevista tunnuksista
        """
        command = "SELECT id, name, username, password FROM credentials;"

        credentials = db_fetch_all(path, command, [])

        return [
            self._decrypt_credential(Credential(*credential), password)
            for credential in credentials
        ]

    def get_credential(self, path: Path, credential_id: int, password: str):
        """
        Hakee tietyn holvissa olevan tunnuksen

        Args:
            path: holvin tiedostopolku
            credential_id: haettavan tunnuksen id
            password: salasana

        Returns:
            löydetty rivi tai None
        """
        command = """
        SELECT id, name, username, password
        FROM credentials
        WHERE id = ?;
        """

        credential = db_fetch(path, command, [credential_id])
        credential = Credential(*credential[0])

        return self._decrypt_credential(credential, password)

    def create_credential(self, path: Path, credential: Credential, password: str):
        """
        Luo holviin uuden tunnuksen

        Args:
            path: holvin tiedostopolku
            credential: luotava tunnus. Id:llä ei ole merkitystä.
            password: salasana
        """

        command = """
        INSERT INTO credentials 
            (name, username, password)
        VALUES (?, ?, ?);
        """

        credential = self._encrypt_credential(credential, password)

        return db_execute(
            path,
            command,
            [
                credential.name,
                credential.username,
                credential.password,
            ],
        )

    def delete_credential(self, path: Path, credential: Credential, password: str):
        """
        Poistaa holvista tunnuksen.

        Args:
            path: holvin tiedostopolku
            credential: poistettava tunnus
            password: salasana
        """

        command = """
        DELETE FROM credentials
        WHERE id = ?;
        """

        db_execute(path, command, [credential.id])

    def update_credential(self, path: Path, credential: Credential, password: str):
        """
        Muokkaa holvissa olevaa tunnusta tunnuksen id:n perusteella

        Args:
            path: holvin tiedostopolku
            credential: muokattava tunnus
            password: salasana
        """
        command = """
        UPDATE credentials
        SET
            name = ?,
            username = ?,
            password = ?
        WHERE id = ?;
        """

        credential = self._encrypt_credential(credential, password)

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
