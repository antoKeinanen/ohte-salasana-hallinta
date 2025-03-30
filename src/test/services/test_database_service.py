import shutil
import tempfile
from pathlib import Path
from unittest import TestCase
from service.database_service import DatabaseService
from model.database import Database


class TestDatabaseService(TestCase):
    def setUp(self):
        self.path = Path(tempfile.mkdtemp())
        self.database_service = DatabaseService(self.path)

    def tearDown(self):
        shutil.rmtree(self.path)

    def create_database_object(self, name: str):
        db_path = self.path.joinpath(name)
        name = name.removesuffix(".db")
        return Database(db_path, name)

    def test_discover_databases_creates_base_path_if_not_exists(self):
        shutil.rmtree(self.path)
        self.assertFalse(self.path.exists())

        self.database_service.discover_databases()
        self.assertTrue(self.path.exists())

    def test_discover_databases_returns_empty_list_when_no_databases(self):
        databases = self.database_service.discover_databases()
        self.assertEqual(databases, [])

    def test_discover_databases_finds_existing_databases(self):
        db1 = self.create_database_object("test1.db")
        db2 = self.create_database_object("test2.db")
        db1.path.touch()
        db2.path.touch()

        databases = self.database_service.discover_databases()

        self.assertEqual(len(databases), 2)
        self.assertIn(db1, databases)
        self.assertIn(db2, databases)

    def test_create_database_creates_new_database(self):
        name = "new_database"
        result = self.database_service.create_database(name)

        db_path = self.path.joinpath(f"{name}.db")
        self.assertTrue(db_path.exists())
        self.assertIsNone(result)

    def test_create_database_returns_message_if_database_exists(self):
        name = "existing_database"
        db_path = self.path.joinpath(f"{name}.db")
        db_path.touch()

        result = self.database_service.create_database(name)

        self.assertEqual(result, f"Holvi {name} on jo olemassa")
        self.assertTrue(db_path.exists())

    def test_create_database_returns_message_if_name_is_empty(self):
        result = self.database_service.create_database("")
        self.assertEqual(result, "Syötä holville nimi")

    def test_create_database_returns_message_if_name_contains_invalid_characters(self):
        invalid_names = ["invalid name!", "name@", "name#"]
        for name in invalid_names:
            result = self.database_service.create_database(name)
            self.assertEqual(
                result,
                "Holvin nimi voi sisältää vain kirjaimia, numeroita, alaviivoja ja viivoja",
            )

    def test_create_database_creates_database_with_valid_name(self):
        name = "valid_name"
        result = self.database_service.create_database(name)

        db_path = self.path.joinpath(f"{name}.db")
        self.assertTrue(db_path.exists())
        self.assertIsNone(result)
