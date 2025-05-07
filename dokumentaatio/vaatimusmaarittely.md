# Vaatimusmaarittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät voivat turvallisesti tallentaa salasanansa. Salasanat tallennetaan salattuna ja ovat käyttäjäkohtaisia, joten sovellus tukee montaa käyttäjää.

## Käyttäjät

Vaikka sovellus tukeekin montaa käyttäjää on käyttäjätyyppejä vain yksi.

## Toiminnallisuus

### Ennen kirjautumista
- [x] Käyttäjä voi luda uuden *holvin* johon voidaan säilöä salasanoja.
- [x] Käyttäjä näkee listan laitteella olevista holveista.
- [x] Käyttäjä voi kirjautua laitteella jo olemassa olevaan holviin.
- [x] Jos salasana ei ole oikein käyttäjä ei voi avata holvia.

### Kirjautumisen jälkeen
- [x] Käyttäjä voi lisätä uuden tunnuksen
- [x] Käyttäjä näkee listan holvissa olevista tunnuksista
- [x] Käyttäjä voi poistaa tunnuksen
- [x] Käyttäjä voi lukea tunnuksen tiedot
- [x] Käyttäjä voi muokata tunnusta
- [x] Käyttäjä voi sulkea avatun holvin

### Muita vaatimuksia
- [x] Holvin tulee olla salattu kun se ei ole käytössä
- [x] Holvin salauksen tulee olla kryptografisesti riittävän vahva *(RSA 2048 bits?)*.

## Käyttöliittymä
![](https://github.com/antoKeinanen/ohjelmistotekniikka-harjoitus/blob/main/dokumentaatio/media/K%C3%A4ytt%C3%B6liittym%C3%A4.png?raw=true)