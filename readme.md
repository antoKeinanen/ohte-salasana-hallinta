# Ohjelmistotekniikka, harjoitustyö

Harjoitustyönä ajattelin tehdä salasanan hallinta ohjelman.

## Laskarit

- [viikko 1](https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus/blob/main/laskarit/viikko1.md)
- Viikko 2
  - [maksukortti](https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus/blob/main/laskarit/viikko2/maksukortti)
  - [unicafe](https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus/blob/main/laskarit/viikko2/unicafe)
- Viikko 3
  - [monopoli](https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus/blob/main/laskarit/viikko3/monopoli.md)
  - [unicafe](https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus/blob/main/laskarit/viikko3/sekvenssikaavio.md)

## Harjoitustyö

### Asennus ja käyttö

```bash
# Kloonaa projekti
git clone https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus.git

# Asenna riippuvuudet
poetry install

# Käynnistä sovellus
poetry run invoke start
```

### Yksikkötestaus

Olettaen että olet suorittanut asennuksen vaiheet:

```bash
# Suorita testit
poetry run invoke test

# Testikattavuuden mittaaminen. Mittauksen tulokset tulevat htmlcov kansioon
poetry run invoke coverage-report
```
