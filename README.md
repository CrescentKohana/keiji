# Web-tietokantasovellus Keiji
Sovelluksen nimi tulee japaninkielisestä sanasta 計時, joka tarkoittaa _ottaa aikaa_. Se on suunniteltu kielten opiskelun kannalta. Sillä voi kartoittaa ajankäyttöä kohdekielen parissa, ja ottaa myös ylös muistiinpanoja. Sovellus löytyy osoitteesta: https://keiji-tsoha2020.herokuapp.com. Testikäyttäjätunnus on `dev` ja salasana sille on `test4200`. Sen nickname eli kirjautumisen jälkeen näkyvä nimi on `developer test`.

## Dokumentaatio
* [Käyttöohje](documentation/user_guide.md)
* [Käyttötapaukset](documentation/user_stories.md)
* [Tietokantakaavio](documentation/database_diagram.md)

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
Huom! Pythonin komento voi olla `python` (yleensä Windowsilla) tai `python3` (yleensä Linuxilla).

Seuraavaksi siirry kansioon `tsoha-2020` ja aja komento:  
```
python3 -m venv venv
```
Huom! Voit joutua antamaan activate-skriptille suoritusoikeudet. Linuxilla tämä onnistuu näin: `chmod +x venv\bin\activate`

Nyt käynnistä venv ajamalla skripti `venv\Scripts\activate` (Windows) tai `source venv\bin\activate` (Linux).

Viimeiseksi asenna tarvittavat riippuvuudet ajamalla komento: 
```
pip install -r requirements.txt
```
Halutessasi voit vielä laittaa päälle debug-moodin [run.py-tiedostosta](run.py) asettamalla debug-parametrin arvoon `True`.

Tässä kohtaa, jos haluat ajaa sovellusta lokaalisti aja seuraava komento: 
```
python3 run.py
```
Jos haluatkin ajaa sovellusta pilvessä (tässä esimerkkinä Heroku), se onnistuu ajamalla seuraava komento venv-ympäristössä: 
```
heroku create sovelluksesi-nimi
```
Nyt lähetetään vielä sovellus Herokun versionhallintaan: 
```
git remote add heroku https://git.heroku.com/sovelluksesi-nimi.git
git add .
git commit -m "Initial commit"
git push heroku master
```
