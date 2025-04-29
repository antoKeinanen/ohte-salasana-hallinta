from repository.credential_repository import CredentialRepository
from model.vault import Vault
from model.credential import Credential


class CredentialService:
    """
    Luokka, joka hallinnoi holvissa olevia tunnuksia ja luo rajapinnan holvin tunnus tietokannalle.

    Attributes:
        vault: viittaus auki olevaan holviin
        repository: viittaus matalantason tietokantaluokkaan. 
    """

    def __init__(
        self,
        vault: Vault,
        repository: CredentialRepository | None = CredentialRepository(),
    ):
        """
        Alustaa luokan annetun holvin ja repositorion mukaan.

        Args:
            vault: viittaus hallinnoitavaan holviin
            repository: käytettävä repository luokka. *vapaaehtoinen*
        """

        self.vault = vault
        self.repository = repository

    def get_all_credentials(self):
        """
        Hakee kaikki holvissa olevat tunnukset ja päivittää ne luokalle määritettyyn holviin.
        """
        credentials = self.repository.get_all_credentials(self.vault.path)
        self.vault.credentials = credentials

    def get_credential_by_id(self, credential_id: int):
        """
        Hakee holvista tietyn tunnuksen id:n perusteella.

        Args:
            id: haettavan tunnuksen id

        Returns:
            credential: tunnus jos sellainen löytyin holvista, muulloin None
        """
        return self.repository.get_credential(self.vault.path, credential_id)

    def add_credential(self, credential: Credential):
        """
        Lisää holviin uuden tunnuksen. Tunnuksen id:llä ei ole merkitystä,
            koska sille annetaan uusi id.

        Args:
            credential: lisättävä tunnus
        """
        credential_id = self.repository.create_credential(
            self.vault.path, credential)
        new_credential = self.repository.get_credential(
            self.vault.path, credential_id)
        self.vault.credentials.append(new_credential)

    def delete_credential(self, credential: Credential):
        """
        Poistaa holvista tunnuksen tunnuksen id:n perusteella.

        Args:
            credential: poistettava tunnus
        """

        self.repository.delete_credential(self.vault.path, credential)
        self.vault.credentials.remove(credential)

    def update_credential(self, credential: Credential):
        """
        Muokkaa holvissa olevaa tunnusta annetun tunnuksen id:n perusteella.

        Args:
            credential: muokattava tunnus
        """

        self.repository.update_credential(self.vault.path, credential)
        self.vault.credentials = [
            cred for cred in self.vault.credentials if cred.id != credential.id
        ]
        self.vault.credentials.append(credential)
