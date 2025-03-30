# Ohjelmistotekniikka, harjoitustyö

## Asennus ja käyttö

```bash
# Kloonaa projekti
git clone https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus.git

# Asenna riippuvuudet
poetry install

# Käynnistä sovellus
poetry run invoke start
```

## Yksikkötestaus

Olettaen että olet suorittanut asennuksen vaiheet:

```bash
# Suorita testit
poetry run invoke test

# Testikattavuuden mittaaminen. Mittauksen tulokset tulevat htmlcov kansioon
poetry run invoke coverage-report
```
