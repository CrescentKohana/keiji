# Web-tietokantasovellus Keiji
Sovelluksen nimi tulee japaninkielisestä sanasta 計時, joka tarkoittaa _ottaa aikaa_. Se on suunniteltu kielten opiskelun kannalta. Sillä voi kartoittaa ajankäyttöä kohdekielen parissa, ja ottaa myös ylös muistiinpanoja. Sovellus löytyy osoitteesta: https://keiji-tsoha2020.herokuapp.com. Testikäyttäjätunnus on `dev` ja salasana sille on `test4200`. Sen nickname eli kirjautumisen jälkeen näkyvä nimi on `developer test`.

Käyttötapaukset [täällä](documentation/user_stories.md).
## Tietokantakaavio
**Categories** eli kategoriat, **Events** eli tapahtumat, **Clips** eli muistiinpanot tai tekstiklipit ja **Users** eli käyttäjät. **Primary keyt** ovat lihavoitu ja **foreign keyt** ovat merkitty _id liitteellä. 

![tietokantakaavio](documentation/database_diagram.png)

## Riippuvuudet
 * Python 3 (>= Python 3.5)
 * PostgreSQL 12.2 (valinnainen, muuten SQLite)
 * requirements.txt
