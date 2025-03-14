import os
import unittest
from repository.database import Database
import tempfile


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.database = Database()

    def tearDown(self):
        self.database.teardown()

    def test_database_is_created_properly(self):
        self.assertIsNone(self.database.connection)

        base_path = tempfile.mkdtemp()
        path = os.path.join(base_path, "database.sqlite")
        self.database.setup(path)

        self.assertIsNotNone(self.database.connection)

    def test_database_is_torn_down_properly(self):
        base_path = tempfile.mkdtemp()
        path = os.path.join(base_path, "database.sqlite")
        self.database.setup(path)

        self.assertIsNotNone(self.database.connection)

        self.database.teardown()
        self.assertIsNone(self.database.connection)
