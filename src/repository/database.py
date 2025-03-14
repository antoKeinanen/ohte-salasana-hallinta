from glob import glob
import os
import sqlite3
import platformdirs

from src.constants import APP_NAME


class Database:
    path: None | os.PathLike = None
    connection: None | sqlite3.Connection = None

    @staticmethod
    def setup(path: os.PathLike):
        Database.path = path
        Database.connection = sqlite3.connect(path)

    @staticmethod
    def teardown():
        if Database.connection:
            Database.connection.close()
            Database.connection = None

    @staticmethod
    def discover_databases(path: None | os.PathLike):
        """
        Discover vault databases in the specified directory.

        If the path is not provided, it defaults to the user data path for the application.
        If the directory does not exist, it will be created.

        Args:
            path (None | os.PathLike): The directory path to search for vault databases.
                                    If None, the default user data path is used.

        Returns:
            list: A list of paths to the discovered vault databases.
        """
        path = path or platformdirs.user_data_path(APP_NAME)
        if not path.exists():
            os.makedirs(path)
        path.joinpath("*.sqlite")
        return glob(path)
