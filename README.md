# Web-tietokantasovellus Keiji
Sovelluksen nimi tulee japaninkielisestä sanasta 計時, joka tarkoittaa _ottaa aikaa_. Se on suunniteltu kielten opiskelun kannalta. Sillä voi kartoittaa ajankäyttöä kohdekielen parissa, ja ottaa myös ylös muistiinpanoja. Sovellus löytyy osoitteesta: https://keiji-tsoha2020.herokuapp.com. Testikäyttäjätunnus on `dev` ja salasana sille on `test4200`. Sen nickname eli kirjautumisen jälkeen näkyvä nimi on `developer test`.

Tietokantakaavio [täällä](documentation/database_diagram.md)
Käyttötapaukset [täällä](documentation/user_stories.md).
Käyttöohje [täällä](documentation/user_guide.md).

## Riippuvuudet
 * Python 3 (>= 3.5)
 * PostgreSQL (>= 12.2 || valinnainen, muuten SQLite)
 * requirements.txt

## Asennusohje
Asenna Python 3.5 tai uudempi, ja tässä vaiheessa myös PostgreSQL (12.2 tai uudempi) on hyvä asentaa, jos on aikomus käyttää sitä.

Kloonaa tämä repositorio kansioon komennolla: 
```
git clone https://github.com/Luukuton/tsoha-hy2020.git
```
Seuraavaksi siirry kansioon `tsoha-2020` ja aja komento (tai ilman numeroa kolme):  
```
python3 -m venv venv
```

Nyt käynnistä venv ajamalla skripti `venv\Scripts\activate` tai `venv\bin\activate`.

Viimeiseksi asenna tarvittavat riippuvuudet ajamalla komento: 
```
pip install -r requirements.txt
```

Sovellus käynnistyy nyt ajamalla komento (tai ilman numeroa kolme): 
```
python3 run.py
```
