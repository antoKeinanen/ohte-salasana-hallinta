# OHTE Salasana hallinta

Sovelluksen avulla käyttäjä voi tietoturvallisesti säilöä tunnuksia. Ohjelma tallentaa ja salaa käyttäjän syöttämät tunnukset sekä tarjoaa käyttöliittymän niiden hallinnoimiseen. Sovellus tukee monia käyttäjiä samalla laitteella ja jopa samassa kotihakemistossa.

## Dokumentaatio

- [Arkkitehtuuri](https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus/blob/main/dokumentaatio/arkkitehtuuri.md)
- [Vaatimusmäärittely](https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus/blob/main/dokumentaatio/changelog.md)
- [Työkirjanpito](https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus/blob/main/työkirjanpito.md)
- [Käyttöohje](https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus/blob/main/dokumentaatio/kayttoohje.md)
- [Testausdokumentti](https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus/blob/main/dokumentaatio/testaus.md)

## Asennus ja käyttö

```bash
# Kloonaa projekti
git clone https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus.git

# Asenna riippuvuudet
poetry install

# Käynnistä sovellus
poetry run invoke start
```

### Yksikkötestaus

```bash
# Suorita testit
poetry run invoke test

# Testikattavuuden mittaaminen. Mittauksen tulokset tulevat htmlcov kansioon
poetry run invoke coverage-report
```

### Koodin automaattinen muotoilu

```bash
poetry run invoke format
```

### Koodin laadun varmistus

```bash
poetry run invoke lint
```
