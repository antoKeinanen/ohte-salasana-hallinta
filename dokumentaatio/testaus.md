# Testaus

Sovellusta on testattu automatisoitujen yksikkötestien ja manuaalisten järjestelmätestien avulla.

## Yksikkötestit

### Sovelluslogiikka

Sovelluslogiikasta vastaavat luokat `CredentialService` ja `VaultService` on testattu automaattisilla yksikkötesteillä. Oliot alustetaan niin, että niille riippuvuus injektoidaan vaaditut repositorio oliot. Mock oliot imitoivat repositorio olioiden toimintaa, mutta eivät kuitenkaan tallenna tietoja tietokantaan vaan muistiin. Repositorio luokkia ei erikseen testata automaattisesti.

### Testikattavuus

```
Name                                      Stmts   Miss Branch BrPart  Cover
---------------------------------------------------------------------------
src/model/credential.py                       7      0      0      0   100%
src/model/vault.py                            8      0      0      0   100%
src/repository/credential_repository.py      35     23      0      0    34%
src/service/credential_service.py            24      0      0      0   100%
src/service/database_service.py              27      8      0      0    70%
src/service/vault_service.py                 41      4     10      0    92%
src/util/crypto.py                           20      0      0      0   100%
---------------------------------------------------------------------------
TOTAL                                       162     35     10      0    80%
```

## Järjestelmätestaus

Sovelluksessa ei ole automaattisia järjestelmätestejä, vaan ne tulee tehdä manuaalisesti.
