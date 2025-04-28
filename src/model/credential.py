from dataclasses import dataclass


@dataclass
class Credential:
    """
    Dataluokka, joka mallintaa tunnusta

    Attributes:
        id: tunnuksen uniikki tunniste
        name: tunnuksen nimi
        username: tunnuksen käyttäjänimi
        password: tunnuksen salasana
    """

    id: int
    name: str
    username: str
    password: str
