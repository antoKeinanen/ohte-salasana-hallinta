from pathlib import Path
from dataclasses import dataclass
from model.credential import Credential


@dataclass
class Vault:
    name: str
    path: Path
    credentials: list[Credential]
