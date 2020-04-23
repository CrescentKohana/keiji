# Käyttötapaukset
## Mitä sillä voi tehdä?
Luoda oman tunnuksen (lempinimi, käyttäjänimi, salasana, kielivalinta): 
```
INSERT INTO User 
    (nickname,username,password,language) 
    VALUES ("dev", "developer test", "test4200", "fi");
```
Luoda kategorioita tapahtumille ja klipeille: 
```
INSERT INTO Category 
    (user_id,date_created,date_modified,name,description) 
    VALUES (1, TIMESTAMP, TIMESTAMP, "Light novels", "Also called ラノベ (ranobe) in Japan");
```
Kirjata tapahtumia ajan kanssa: 
```
INSERT INTO Event 
    (category_id,date_created,date_modified,description,duration) 
    VALUES (1, TIMESTAMP, TIMESTAMP, "月光 (Gekkou)", 60);
```
Luoda muistiinpanoja / klippejä: 
```
INSERT INTO Clip 
    (category_id,date_created,date_modified,content) 
    VALUES (1, TIMESTAMP, TIMESTAMP, "eg. citate from a book");
```
Muokata kaikkea tallennettua dataa, jonka on itse luonut: 
```
UPDATE Event SET duration=90 WHERE id=1;
```
Katsoa ajankäytön kohdekielen parissa per kategoria: 
```
SELECT COALESCE(SUM(E.duration),0) 
    FROM Category as C LEFT JOIN Event as E 
    ON C.id = E.category_id 
    WHERE (C.account_id = 1) 
    GROUP BY C.id 
    ORDER BY C.id;
```

## Tarkemmin käyttäjän näkökulmasta
Kieltä opiskeleva henkilö voi haluta merkitä talteen paljon on käyttänyt aikaa kohdekielen parissa. Esimerkiksi: 
* "Luin tänään kirjaa Gekkou (月光, 間宮夏生, 2010) kaksi tuntia ja haluan merkitä sen ylös."
* "Tulen katsomaan tämän tunnin pituisen YouTube-videon ja haluan merkitä sen nyt ensin ylös."
* "Kuuntelin podcastia Spotify'sta matkalla opistolle 25 minuuttia tänään aamulla ja merkkaan sen nyt (illalla) ylös."

Käyttäjä pystyy nyt myöhemmin tarkistamaan tilasto-sivulta paljon hän on keskimäärin viettänyt aikaa kohdekielensä parissa ja pitäisiköhä hänen kenties lisätä aikaa esimerkiksi keskimäärin tunnilla, että pääsee kolme tunnin tavoitteeseen. 
  
Käyttäjä voi haluta myös ottaa talteen hyviä otteita kuluttamastaan viihteestä samaan palveluun. Esimerkiksi: 
* "Löysin tämän kivan twiitin, joka oli hienosti artikuloitu. Haluan sen talteen."
* "Lukemassani kirjassa oli mielenkiintoinen virke ja haluan sen talteen."

## Tulevaisuudessa
* Käännökset kieliominaisuudelle
* Integraatio palveluihin (esm. YouTube, Spotify) automaattiselle ajanseurannalle
