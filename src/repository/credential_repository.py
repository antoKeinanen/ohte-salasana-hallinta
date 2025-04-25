from pathlib import Path
from model.credential import Credential
from service.database_service import db_fetch_all, db_execute, db_fetch


class CredentialRepository:
    def get_all_credentials(self, path: Path):
        command = "SELECT id, name, username, password FROM credentials;"

        credentials = db_fetch_all(path, command, [])

        return [Credential(*credential) for credential in credentials]

    def get_credential(self, path: Path, credential_id: int):
        command = """
        SELECT id, name, username, password
        FROM credentials
        WHERE id = ?;
        """

        return db_fetch(path, command, [credential_id])

    def create_credential(self, path: Path, credential: Credential):
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
        command = """
        DELETE FROM credentials
        WHERE id = ?;
        """

        db_execute(path, command, [credential.id])

    def update_credential(self, path: Path, credential: Credential):
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
