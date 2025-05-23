from unittest import TestCase
from service.credential_service import CredentialService
from model.vault import Vault
from model.credential import Credential


class DummyCredentialRepository:
    def __init__(self):
        self.credentials = [
            Credential(id=1, name="cred1", username="user1", password="pass1"),
            Credential(id=2, name="cred2", username="user2", password="pass2"),
        ]

    def get_all_credentials(self, _path, _password):
        return self.credentials.copy()

    def get_credential(self, _path, credential_id, _password):
        for cred in self.credentials:
            if cred.id == credential_id:
                return cred
        return None

    def create_credential(self, _path, credential, _password):
        new_id = (
            max(cred.id for cred in self.credentials) +
            1 if self.credentials else 1
        )
        credential.id = new_id
        self.credentials.append(credential)
        return new_id

    def delete_credential(self, _path, credential):
        self.credentials.remove(credential)

    def update_credential(self, _path, updated_credential, _password):
        for index, cred in enumerate(self.credentials):
            if cred.id == updated_credential.id:
                self.credentials[index] = updated_credential


class TestCredentialService(TestCase):
    def setUp(self):
        self.repo = DummyCredentialRepository()
        self.vault = Vault(name="dummy", path="/dummy/path", credentials=[])
        self.service = CredentialService(
            vault=self.vault,
            repository=self.repo,
            password="test password",
        )

    def test_get_all_credentials(self):
        self.service.get_all_credentials()

        self.assertEqual(self.vault.credentials, self.repo.credentials)

    def test_get_credential_by_id(self):
        credential = self.service.get_credential_by_id(1)

        self.assertIsNotNone(credential)
        self.assertEqual(credential.username, "user1")

    def test_add_credential(self):
        new_credential = Credential(
            id=None,
            name="cred3",
            username="user3",
            password="pass3",
        )

        self.assertEqual(len(self.vault.credentials), 0)

        self.service.add_credential(new_credential)
        self.assertEqual(len(self.vault.credentials), 1)

        added_cred = self.vault.credentials[0]
        self.assertIsNotNone(added_cred.id)
        self.assertEqual(added_cred.username, "user3")

        self.assertIn(added_cred, self.repo.credentials)

    def test_delete_credential(self):
        self.service.get_all_credentials()

        credential_to_delete = self.vault.credentials[0]

        self.assertIn(credential_to_delete, self.vault.credentials)
        self.assertIn(credential_to_delete, self.repo.credentials)

        self.service.delete_credential(credential_to_delete)

        self.assertNotIn(credential_to_delete, self.vault.credentials)
        self.assertNotIn(credential_to_delete, self.repo.credentials)

    def test_update_credential(self):
        self.service.get_all_credentials()
        original_credential = self.vault.credentials[0]

        updated_credential = Credential(
            id=original_credential.id,
            name="updated_cred",
            username="updated_user",
            password="updated_pass",
        )

        self.assertIn(original_credential, self.vault.credentials)

        self.service.update_credential(updated_credential)

        self.assertNotIn(original_credential, self.vault.credentials)

        self.assertIn(updated_credential, self.vault.credentials)

        repo_credential = self.repo.get_credential(
            None, updated_credential.id, "test password")
        self.assertEqual(repo_credential.name, "updated_cred")
        self.assertEqual(repo_credential.username, "updated_user")
        self.assertEqual(repo_credential.password, "updated_pass")
