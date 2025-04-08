import shutil
import tempfile
from pathlib import Path
from unittest import TestCase
from service.vault_service import VaultService
from model.vault import Vault


class TestVaultService(TestCase):
    def setUp(self):
        self.path = Path(tempfile.mkdtemp())
        self.vault_service = VaultService(self.path)

    def tearDown(self):
        shutil.rmtree(self.path)

    def create_vault_object(self, name: str):
        vault_path = self.path.joinpath(name)
        name = name.removesuffix(".db")
        return Vault(name, vault_path, [])

    def test_discover_vaults_creates_base_path_if_not_exists(self):
        shutil.rmtree(self.path)
        self.assertFalse(self.path.exists())

        self.vault_service.discover_vaults()
        self.assertTrue(self.path.exists())

    def test_discover_vaults_returns_empty_list_when_no_vaults(self):
        vaults = self.vault_service.discover_vaults()
        self.assertEqual(vaults, [])

    def test_discover_vaults_finds_existing_vaults(self):
        db1 = self.create_vault_object("test1.db")
        db2 = self.create_vault_object("test2.db")
        db1.path.touch()
        db2.path.touch()

        vaults = self.vault_service.discover_vaults()

        self.assertEqual(len(vaults), 2)
        self.assertIn(db1, vaults)
        self.assertIn(db2, vaults)

    def test_create_vault_creates_new_vault(self):
        name = "new_vault"
        result = self.vault_service.create_vault(name)

        db_path = self.path.joinpath(f"{name}.db")
        self.assertTrue(db_path.exists())
        self.assertIsNone(result)

    def test_create_vault_returns_message_if_vault_exists(self):
        name = "existing_vault"
        db_path = self.path.joinpath(f"{name}.db")
        db_path.touch()

        result = self.vault_service.create_vault(name)

        self.assertEqual(result, f"Holvi {name} on jo olemassa")
        self.assertTrue(db_path.exists())

    def test_create_vault_returns_message_if_name_is_empty(self):
        result = self.vault_service.create_vault("")
        self.assertEqual(result, "Syötä holville nimi")

    def test_create_vault_returns_message_if_name_contains_invalid_characters(self):
        invalid_names = ["invalid name!", "name@", "name#"]
        for name in invalid_names:
            result = self.vault_service.create_vault(name)
            self.assertEqual(
                result,
                "Holvin nimi voi sisältää vain kirjaimia, numeroita, alaviivoja ja viivoja",
            )

    def test_create_vault_creates_vault_with_valid_name(self):
        name = "valid_name"
        result = self.vault_service.create_vault(name)

        db_path = self.path.joinpath(f"{name}.db")
        self.assertTrue(db_path.exists())
        self.assertIsNone(result)
