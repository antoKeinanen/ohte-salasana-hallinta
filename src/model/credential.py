from dataclasses import dataclass


@dataclass
class Credential:
    id: int
    name: str
    password: str
