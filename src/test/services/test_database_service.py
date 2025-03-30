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
        name = name.capitalize().removesuffix(".db")
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