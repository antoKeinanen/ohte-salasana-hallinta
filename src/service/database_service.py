import sqlite3
from pathlib import Path


def db_execute_script(path: Path, sql_script: str):
    with sqlite3.connect(path) as connection:
        cursor = connection.cursor()
        cursor.executescript(sql_script)


def db_execute(path: Path, sql_command: str, arguments: list | None = None):
    with sqlite3.connect(path) as connection:
        cursor = connection.cursor()
        cursor.execute(sql_command, arguments)
        return cursor.lastrowid


def db_fetch(path: Path, sql_command: str, arguments: list | None = None, size: int = 1):
    with sqlite3.connect(path) as connection:
        cursor = connection.cursor()
        cursor.execute(sql_command, arguments)
        return cursor.fetchmany(size)


def db_fetch_all(path: Path, sql_command: str, arguments: list | None = None):
    with sqlite3.connect(path) as connection:
        cursor = connection.cursor()
        cursor.execute(sql_command, arguments)
        return cursor.fetchall()
