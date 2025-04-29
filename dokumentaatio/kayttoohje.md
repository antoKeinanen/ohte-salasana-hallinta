# Käyttöohje

Lataa projektin viimeisin julkaisu [releases](https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus/releases) sivulta, lähde valikon alta valitsemalla _Source code_.

## Asennus

Varmista että seuraavat riippuvuudet ovat asennettu:

- Python `^3.9`
- Poetry

Asenna loput riippuvuudet komennolla:

```shell
poetry install
```

## Ohjelman käynnistys

Ohjelma voidaan käynnistää komennolla:

```shell
poetry run invoke start
```

## Ohjelman käyttö

### Uuden holvin luominen

Sovellus aukeaa näkymään josta pääset valitsemaan minkä holvin haluat avata. Jos sinulla ei kuitenkaan ole holveja voit luoda uuden holvin painamalla vasemmassa alanurkassa olevaa "+ Luo uusi holvi" nappia.

Tämän jälkeen näkymä vaihtuu holvin luonti näkymään. Kirjoita holville nimi ja salasana. Salasanalla ei ole rajoitteita, mutta suosittelen, että salasana on vähintään 32 merkkiä pitkä parhaan turvallisuuden saavuttamiseksi.

Kun olet syöttänyt tarvittavat tiedot paina "Luo holvi" nappia.

### Holvin avaaminen

Kun olet luonut holvin sinut ohjataan automaattisesti lukittu holvi näkymään. Valitse vasemmasta reunasta holvi, jonka haluat avata ja syötä salasanasi. Kun olet valmis paina "Avaa holvi" nappia.

### Tunnuksen luonti

Kun holvi on auki voit näet kaikki holvissa olevat tunnukset. Jos tunnuksia ei ole voit luoda uuden tunnuksen painamalla vasemmassa alanurkassa olevaa "+ Luo uusi tunnus" nappia.

Tämän jälkeen avautuu tunnuksen luonti näkymä. Syötä kenttiin tunnuksen nimi, käyttäjätunnuksesi ja salasanasi. Lopuksi paina "Luo tunnus" nappia tallentaaksesi.

### Tunnuksen muokkaaminen

Jos sinun täytyy muuttaa tallentamasi tunnuksen tietoja valitse tunnus vasemmasta reunasta ja paina "Muokkkaa" nappia.

Tee tarvitsemasi muutokset ja tallenna painamalla "Muokkaa tunnusta" nappia.

### Tunnuksen poistaminen

Jos haluat poistaa tunnuksen valitse tunnus vasemmasta reunasta ja paina "Poista" nappia.
