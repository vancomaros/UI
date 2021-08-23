## Z3
Eulerov kôň
Algoritmom slepého prehľadávania (do hĺbky) je možné nájsť (všetky) riešenia (v bežných 
výpočtových – čas a pamäť – podmienkach PC) iba pri šachovniciach do veľkosti 6x6, max 7x7. 
Implementujte tento algoritmus pre šachovnice s rozmermi 5x5 a 6x6 a skúste nájsť prvých 5 riešení 
pre každú šachovnicu tak, že pre šachovnicu 5x5 aj 6x6 si vyberte náhodne 5 východzích bodov (spolu 
teda 10 východzích bodov) s tým, že jeden z týchto bodov je (pre každú šachovnicu) ľavý dolný roh a 
pre každý z týchto bodov nájdite (skúste nájsť) prvé riešenie.

## Z3
Tento špecifický spôsob evolučného programovania využíva spoločnú pamäť pre údaje a inštrukcie. 
Pamäť je na začiatku vynulovaná a naplnená od prvej bunky inštrukciami. Za programom alebo od 
určeného miesta sú uložené inicializačné údaje (ak sú nejaké potrebné). Po inicializácii sa začne 
vykonávať program od prvej pamäťovej bunky. (Prvou je samozrejme bunka s adresou 000000.) 
Inštrukcie modifikujú pamäťové bunky, môžu realizovať vetvenie, programové skoky, čítať nejaké 
údaje zo vstupu a prípadne aj zapisovať na výstup. Program sa končí inštrukciou na zastavenie, po 
stanovenom počte krokov, pri chybnej inštrukcii, po úplnom alebo nesprávnom výstupe. Kvalita 
programu sa ohodnotí na základe vyprodukovaného výstupu alebo, keď program nezapisuje na 
výstup, podľa výsledného stavu určených pamäťových buniek.

## Z4  
Úlohou je vytvoriť jednoduchý dopredný produkčný systém.

Na začiatku programu používateľ zadá vstup. Môže si vybrať rodinné vzťahy alebo fiaty a tiež spôsob 
vykonania programu; krokovať, resp. ísť do konca. Podľa vstupu sa načítajú pravidlá a fakty zo 
súborov. Možnosti sú ‘family’ alebo ‘fiat’, nasledované medzerou a číslom 1, ktoré značí krokovanie 
do cieľa, alebo 2, čo znamená vykonať algoritmus až do konca. V prípade, že zadáme 1, môžeme číslo 
za behu programu upraviť.
