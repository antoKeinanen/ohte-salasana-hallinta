import os
import sqlite3


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
