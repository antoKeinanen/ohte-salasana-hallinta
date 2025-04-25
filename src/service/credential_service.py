from repository.credential_repository import CredentialRepository
from model.vault import Vault
from model.credential import Credential


class CredentialService:
    def __init__(
        self,
        vault: Vault,
        repository: CredentialRepository | None = CredentialRepository(),
    ):
        self.vault = vault
        self.repository = repository

    def get_all_credentials(self):
        credentials = self.repository.get_all_credentials(self.vault.path)
        self.vault.credentials = credentials

    def get_credential_by_id(self, credential_id: int):
        return self.repository.get_credential(self.vault.path, credential_id)

    def add_credential(self, credential: Credential):
        credential_id = self.repository.create_credential(self.vault.path, credential)
        new_credential = self.repository.get_credential(self.vault.path, credential_id)
        self.vault.credentials.append(new_credential)

    def delete_credential(self, credential: Credential):
        self.repository.delete_credential(self.vault.path, credential)
        self.vault.credentials.remove(credential)

    def update_credential(self, credential: Credential):
        self.repository.update_credential(self.vault.path, credential)
        self.vault.credentials = [
            cred for cred in self.vault.credentials if cred.id != credential.id
        ]
        self.vault.credentials.append(credential)
