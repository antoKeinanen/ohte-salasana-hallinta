# Arkkitehtuuri

## Rakenne

Sovellus toteuttaa model view controller rakenteen ja repository rakenteen yhdistelmää.


```mermaid
classDiagram

class Main
class PasswordManagerApp

namespace Controller {
    class AppController
    class ViewController
}

namespace Model {
    class Vault
    class Credential
}

namespace View {
    class VaultView
    class CreateCredentialView
    class UpdateCredentialView
    class LockedView
    class CreateVaultView
}

namespace Service {
    class VaultService
    class CredentialService
}

namespace Repository {
    class CredentialRepository
}

namespace util {
    class encrypt
    class decrypt
}

Main "1" -- "1" PasswordManagerApp
Main "1" -- "1" AppController
AppController "1" -- "1" PasswordManagerApp
AppController "1" -- "1" ViewController
ViewController "1" -- "1" VaultView
ViewController "1" -- "1" CreateCredentialView
ViewController "1" -- "1" LockedView
ViewController "1" -- "1" CreateVaultView
ViewController "1" -- "1" UpdateCredentialView
LockedView --> VaultService
CreateVaultView --> VaultService
VaultView --> CredentialService
CreateCredentialView --> CredentialService
UpdateCredentialView --> CredentialService
CredentialService --> CredentialRepository
Vault "1" -- "*" Credential
CredentialService --> Credential
AppController --> Vault
CredentialService --> encrypt
CredentialService --> decrypt

```

## Käyttöliittymä

Sovellus sisältää 5 eri näkymää:
- Lukittu holvi
- Luo holvi
- Avoin holvi
- Luo tunnus
- Muokkaa tunnusta

Näkymiä ohjaa ViewController ajuri, jonka tehtävänä on tuhota edellinen näkymä ennen seuraavan näkymän näyttöä.

## Sovellus logiikka

Sovelluksen toiminta perustuu palveluihin, repositorioihin ja malleihin. Mallit ovat vain "tyhmiä" dataluokkia, joiden tarkoituksena on mallintaa tietoa järkevänä rakenteena. Palvelut puolestaan suorittavat erilaisia CRUD operaatioita mallien perusteella. Palvelut kutsuvat repositorioiden funktioita, jotta käyttäjän tekemät toimenpiteet tallentuvat tietokantoihin.

## Tietojen tallennus

Salasanaholvit tallennetaan käyttöjärjestelmästä riippuen eri tiedostopolkuun. Lähtokohtaisesti polku on käyttöjärjestelmän määrittelemä käyttäjän data kansio:
- Windows: `C:\Users\<username>\AppData\Local\password-manager\`
- Linux: `/home/<username>/.local/password-manager/`
- Mac: `/Users/<username>/Library/Application Support/password-manager/`


Jokainen holvi tallennetaan erillisenä sqlite tietokantana, jonka rivit ovat salattu AES algoritmilla.


## Päätoiminnallisuudet

### Uuden holvin luominen

Käyttäjä voi luoda uuden holvin painamalla vasemmassa alanurkassa näkyvää "+ Luo uusi holvi" nappia. Tämän jälkeen käyttäjältä kysytään uuden holvin nimi ja salasana, jolla holvi saadaan auki.


```mermaid
sequenceDiagram
actor Käyttäjä
participant UI
participant VaultService

Käyttäjä ->> UI: paina "luo holvi" nappia

UI ->>+ VaultService: create_vault("holvi1", "salasana")
VaultService ->> VaultService: _seed_vault_db("<user_data_path>/holvi1.db", "salasana")
VaultService ->> VaultService: discover_vaults()
VaultService -->>- UI: None

UI -->> Käyttäjä: None
```

### Holvin avaaminen

Käyttäjä voi valita vasemmassa reunassa olevasta listasta holvin, jonka haluaa avata. Tämän jälkeen käyttäjältä kysytään salasana, jotta holvin salaus saadaan purettua.

```mermaid
sequenceDiagram
actor Käyttäjä
participant UI
participant VaultService
participant ViewController

Käyttäjä ->> UI: paina "Avaa holvi" nappia
UI ->> VaultService: validate_authentication("/holvin/polku/hovi.db", "salasana")
VaultService -->> UI: True
UI ->> ViewController: swap_view("vault")
ViewController -->> Käyttäjä: Holvi näkymä 
```

### Tunnuksen lisääminen holviin
Käyttäjä voi lisätä uuden tunnuksen holviin painamalla "Luo uusi tunnus nappia" holvi näkymän vasemmassa alanurkassa. Tämän jälkeen aukeaa uusi näkymä jossa käyttäjä voi syöttää tunnuksen tiedot.

```mermaid
sequenceDiagram
actor Käyttäjä
participant UI
participant Credential
participant CredentialService
participant CredentialRepository

Käyttäjä ->> UI: paina "Luo tunnus" nappia
UI ->> Credential: tunnus = Credential(-1, "nimi", "käyttäjä", "salasana")
Credential -->> UI: 
UI ->>+ CredentialService: add_credential(tunnus)
CredentialService ->> CredentialRepository: create_credential("/holvin/polku/hovi.db", tunnus, "holvin salasana")
CredentialRepository -->> CredentialService: tunnuksen_id
CredentialService ->> CredentialRepository: get_credential("/holvin/polku/hovi.db", tunnus, "holvin salasana")
CredentialRepository -->> CredentialService: uusi tunnus
CredentialService -->- UI: 

```

## Ongelmat sovelluksen rakenteessa
Credential luokka ottaa argumentiksi viittauksen Vault dataluokkaan. Kun Credential methodeja kutsutaan muokkaa se dataluokkaa paikallaan eikä palauta uutta erillistä instanssia. Mielestäni tämä rakenne voi olla hieman harhaanjohtava.

Ohjelma myös säilyttää ohjelmalle tärkeitä tietoja, kuten auki olevaa holvia ja sen salasanaa AppController luokassa. Tämän takia moni luokka alempana ohjelmassa joutuu hakemaan kyseiset tiedot aika ikävällä tavalla. Tältä olisi voinut välttyä luomalla koko ohjelman tilaa kuvaavan dataluokan ja käyttämällä sitä singleton rakenteen mukaisesti. 