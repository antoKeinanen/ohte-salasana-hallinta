import sqlite3
from sqlite3 import Cursor
from collections.abc import Callable
from typing import Any
from pathlib import Path


def _perform_db_operation(path: Path, action: Callable[[Cursor], Any]):
    with sqlite3.connect(path) as connection:
        cursor = connection.cursor()
        return action(cursor)


def db_execute_script(path: Path, sql_script: str):
    """
    Ajaa scriptin tietokannassa.

    Args:
        path: tietokannan tiedostopolku
        sql_script: ajettava scripti
    """

    def execute_script(cursor: Cursor):
        cursor.executescript(sql_script)

    _perform_db_operation(path, execute_script)


def db_execute(path: Path, sql_command: str, arguments: list | None = None):
    """
    Suorittaa tietokannassa yksittäisen komennon.

    Args:
        path: tietokannan tiedostopolku
        sql_command: suoritettava komento
        arguments: lista komennon vaatimia argumentteja

    Returns:
        last_rowid: Viimeisimmän muuttuneen rivin id:n
    """

    def execute(cursor: Cursor):
        return cursor.execute(sql_command, arguments).lastrowid

    return _perform_db_operation(path, execute)


def db_fetch(
    path: Path, sql_command: str, arguments: list | None = None, size: int = 1
):
    """
    Hakee tietokannasta n riviä.

    Args:
        path: tietokannan tiedostopolku
        sql_command: suoritettava komento
        arguments: lista komennon vaatimia argumentteja
        size: haettavien rivien määrä. Oletus: 1

    Returns:
        rows: hakua vastaavat n riviä.
    """

    def fetch(cursor: Cursor):
        cursor.execute(sql_command, arguments)
        return cursor.fetchmany(size)

    return _perform_db_operation(path, fetch)


def db_fetch_all(path: Path, sql_command: str, arguments: list | None = None):
    """
    Hakee tietokannasta kaikki komentoa vastaavat rivit.

    Args:
        path: tietokannan tiedostopolku
        sql_command: suoritettava komento
        arguments: lista komennon vaatimia argumentteja

    Returns:
        rows: hakua vastaavat rivit
    """

    def fetch_all(cursor: Cursor):
        cursor.execute(sql_command, arguments)
        return cursor.fetchall()

    return _perform_db_operation(path, fetch_all)
