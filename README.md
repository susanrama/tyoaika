# tyoaika
 
Visma Solutions - hakutehtävä (junior)

Tehtävä \
Ensimmäinen tehtävänne on suunnitella ja toteuttaa luokka työvuoron validointia varten.
Luokan tulee toimia seuraavalla tavalla: \
● Luokka ottaa sisäänsä seuraavat tiedot: \
○ Työvuoron päivämäärän (tyyppiä datetime) \
○ Työajan aloitus- ja lopetusajan (tyyppiä string) \
● Luokan tulee validoida ja parsia työajan aloitus- ja lopetusajan oikeellisuus \
○ Työaikaa saa syöttää välille 00:00-23:59 \
○ Työvuoron maksimipituus on 16 tuntia \
○ Työajan tulee olla kronologisessa järjestyksessä \
■ Työaika ei voi mennä miinukselle \
● Luokalta saa kysyttyä syötetyn työvuoron pituuden \
○ Työvuoron pituus palautetaan tunteina (desimaalina) \
● Luokan suunnittelussa tulee noudattaa olio-ohjelmoinnin käytäntöjä \
● Toiminnallisuudessa tulee olla mukana “client”, joka käyttää uutta luokkaa 

Käytä tehtävän tekemiseen noin 2 - 3 tuntia korkeintaan. Kirjoita lyhyt kuvaus miten
ymmärsit annetun ongelman, mitä haasteita toteuttamisessa oli, mitä parannettavaa
ratkaisusta vielä löytyisi. Jos jouduit tekemään kompromisseja toteutuksessa, niin
kuulisimme mielellämme lisää niistä. 


POHDINTAA OMASTA TEKEMISESTÄ:


Ymmärsin ongelman yksinkertaisena luokkatehtävänä, joka tulee toteuttaa olio-ohjelmoinnin perustein. Lähdin liikkeelle tutustumalla datetime rakenteeseen, sillä sitä ei ollut tarvinnut käyttää varmaan vuoteen. Tämän jälkeen pohdin kuinka työvuoron pituuden saa laskettua yksinkertaisimmin. Ajattelin ensin toteuttaa sen laskemalla erikseen tunnit ja minuutit, mutta totesin, että se on helpompaa laskea suoraan minuuteista, sillä vaatimuksena oli, että lopetusaika on aloitusajan jälkeen eikä työaika siten pystynyt menemään negatiiviseksi. 

Seuraavana siirryin pohtimaan luokan validointia. Tämän olisi voinut toteuttaa try-except rakenteella, mikäli syötettä kysyttäisiin käyttäjältä, jotta ohjelma ei kaadu viallisen syötteen tullessa. Päädyin tällä kertaa kuitenkin käyttämään assertia (jonka käytön opiskelin tehtävän aikana), joka lopettaa ohjelman, mikäli parametri on virheellinen. Lisäsin myös lyhyet tekstit, jotka kertovat, minkä takia parametrit ovat viallisia. 

Pohdin tämän jälkeen sitä, miten otan "clientin" mukaan ja päädyin tällä kertaa siirtää työvuorot Client luokan sisäiseksi luokaksi, jolloin sitä ei voi käyttää ilman Client luokkaa. Mielestäni mahdollisen jatkokäsittelyn kannalta on kätevää, että kaikki tehdyt/kirjatut työvuorot ovat yhtenä kokoelmana. 

Joitakin rakenteita voisi vielä siistiä ja tehdä esimerkiksi lyhyitä funktioita laskemaan tarvittavia asioita assertteja varten ja täten vähentää esim. toistoa. Shift luokan rakenteen alustaminen voisi siis toisaalta olla esteetttisempi pienillä muutoksilla. Päivämäärän rakennetta ei käsketty tehtävänannossa tarkistaa, mutta yleisesti ottaen kaikki parametrit olisi hyvä tällaisessa tapauksessa tarkistaa. 

Loin lopuksi lyhyen main funktion, jolla testasin ohjelmani toimintaa ja AssertionErroreita. Tehtävä oli melko yksinkertainen, jonka vuoksi loin mainin vasta lopussa. Monimutkaisemmassa ja pidemmässä ohjelmassa tarkistaisin eri osa-alueiden toimintaa jo niitä kehittäessä, enkä vasta viimeisenä. 
