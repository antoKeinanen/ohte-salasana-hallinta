# Vaatimusmaarittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät voivat turvallisesti tallentaa salasanansa. Salasanat tallennetaan salattuna ja ovat käyttäjäkohtaisia, joten sovellus tukee montaa käyttäjää.

## Käyttäjät

Vaikka sovellus tukeekin montaa käyttäjää on käyttäjätyyppejä vain yksi.

## Toiminnallisuus

### Ennen kirjautumista
- Käyttäjä voi luda uuden *holvin* johon voidaan säilöä salasanoja.
- Käyttäjä näkee listan laitteella olevista holveista.
- Käyttäjä voi kirjautua laitteella jo olemassa olevaan holviin.
- Jos salasana ei ole oikein käyttäjä ei voi avata holvia.

### Kirjautumisen jälkeen
- Käyttäjä voi lisätä uuden salasana
- Käyttäjä näkee listan holvissa olevista tunnuksista
- Käyttäjä voi lukea tunnuksen tiedot
- Käyttäjä voi muokata tunnuksia
- Käyttäjä voi poistaa tunnuksen

### Muita vaatimuksia
- Holvin tulee olla salattu kun se ei ole käytössä
- Holvin salauksen tulee olla kryptografisesti riittävän vahva *(RSA 2048 bits?)*.

## Käyttöliittymä
![](https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus/blob/main/dokumentaatio/media/K%C3%A4ytt%C3%B6liittym%C3%A4.png?raw=true)