from dataclasses import dataclass


@dataclass
class Credential:
    id: int
    name: str
    username: str
    password: str
