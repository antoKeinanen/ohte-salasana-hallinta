from pathlib import Path
from dataclasses import dataclass
from model.credential import Credential


@dataclass
class Vault:
    """
    Tietoluokka, joka kuvaa holvia

    Attributes:
        name: holvin nimi
        path: holvin tiedostopolku
        credentials: lista holvissa olevia tunnuksia
    """

    name: str
    path: Path
    credentials: list[Credential]
