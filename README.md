# Z3
Tento špecifický spôsob evolučného programovania využíva spoločnú pamäť pre údaje a inštrukcie. 
Pamäť je na začiatku vynulovaná a naplnená od prvej bunky inštrukciami. Za programom alebo od 
určeného miesta sú uložené inicializačné údaje (ak sú nejaké potrebné). Po inicializácii sa začne 
vykonávať program od prvej pamäťovej bunky. (Prvou je samozrejme bunka s adresou 000000.) 
Inštrukcie modifikujú pamäťové bunky, môžu realizovať vetvenie, programové skoky, čítať nejaké 
údaje zo vstupu a prípadne aj zapisovať na výstup. Program sa končí inštrukciou na zastavenie, po 
stanovenom počte krokov, pri chybnej inštrukcii, po úplnom alebo nesprávnom výstupe. Kvalita 
programu sa ohodnotí na základe vyprodukovaného výstupu alebo, keď program nezapisuje na 
výstup, podľa výsledného stavu určených pamäťových buniek.


# Z4  
Úlohou je vytvoriť jednoduchý dopredný produkčný systém.

Na začiatku programu používateľ zadá vstup. Môže si vybrať rodinné vzťahy alebo fiaty a tiež spôsob 
vykonania programu; krokovať, resp. ísť do konca. Podľa vstupu sa načítajú pravidlá a fakty zo 
súborov. Možnosti sú ‘family’ alebo ‘fiat’, nasledované medzerou a číslom 1, ktoré značí krokovanie 
do cieľa, alebo 2, čo znamená vykonať algoritmus až do konca. V prípade, že zadáme 1, môžeme číslo 
za behu programu upraviť.
