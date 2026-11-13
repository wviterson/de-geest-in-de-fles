# Bijlage – Problemen oplossen

Deze bijlage is voor begeleiders die rondlopen. Installatieproblemen (poort bezet, scripts geblokkeerd, virusscanner, trage downloads) staan in `installatie\INSTALLATIE.md` onder *Problemen oplossen*. Hier staat wat er **tijdens de les** misgaat: foutmeldingen in Thonny, vreemd gedrag van de geest en dingen in de klas.

**Gouden regel:** los het niet op ván het kind, maar mét het kind. Vraag eerst: *"Wat zegt de foutmelding? Op welke regel?"* Thonny wijst de regel meestal goed aan; de fout zit vaak op die regel of de regel erboven.

---

## 1. De geest antwoordt niet

| Wat zie je? | Oorzaak | Oplossing |
|---|---|---|
| *"Ik kan de geest niet bereiken. Is start.bat (of de docent-server) gestart?"* | Ollama draait niet (laptop is in slaap geweest, venster gesloten) of het adres in `fles.py` klopt niet. | Dubbelklik `start.bat`. Bij de docent-server: kijk of `SERVER` in `fles.py` precies het adres van het bord bevat, met `http://` en `:11434`. |
| De eerste vraag duurt heel lang (10–60 s) | Het model wordt in het geheugen geladen. | Normaal. Daarna gaat het sneller. Na 5 minuten niets doen wordt het model weer uit het geheugen gehaald. |
| Het blijft heel lang stil, dan komt er een enorme lap tekst | Fietje praat door. Na `MAX_TOKENS` (300) stopt hij altijd. | Wacht, of druk op de rode **Stop**-knop in Thonny. Zie ook paragraaf 3. |
| Alles is traag op één laptop | Te weinig geheugen, of de laptop rekent op batterijstand. | Lader erin, browsers dicht. Blijft het traag: laat dit tweetal de docent-server gebruiken. |
| Alles is traag op álle laptops tegelijk (bij docent-server) | De server krijgt 15 vragen tegelijk. | Normaal; vragen staan in een rij. Laat sterke laptops lokaal draaien en alleen zwakke de server gebruiken. |
| `ReadTimeout` of `timed out` | De geest deed er langer dan 5 minuten over. | Komt bijna alleen voor bij een overbelaste docent-server. Opnieuw proberen. |

## 2. Foutmeldingen in Thonny

Thonny toont fouten onderin, in de *Shell*. De laatste regel is de belangrijkste.

| Melding (laatste regel) | Wat betekent het? | Wat er meestal mis is |
|---|---|---|
| `SyntaxError: unterminated string literal` | Een stuk tekst is niet afgesloten. | Een `"` vergeten aan het eind, of een `"` ín de tekst (`"Zeg "hoi""`). Tip: gebruik binnen de tekst enkele quotes: `"Zeg 'hoi'"`. |
| `SyntaxError: '(' was never closed` / `'[' was never closed` | Een haakje is niet dicht. | Tel de haakjes. Thonny kleurt het bijbehorende haakje als je de cursor erop zet. |
| `SyntaxError: invalid syntax. Perhaps you forgot a comma?` | Er ontbreekt een komma. | Vaak in een lijst (`VRAGEN`, `VOORBEELDEN`) tussen twee regels. Elke regel in een lijst eindigt op een komma. |
| `IndentationError: unexpected indent` / `expected an indented block` | Inspringing klopt niet. | Een regel begint met een spatie te veel of te weinig. Kopieer de inspringing van de regel erboven. Gebruik Tab niet door elkaar met spaties (Thonny maakt van Tab vanzelf 4 spaties). |
| `NameError: name 'xxx' is not defined` | Python kent dat woord niet. | Tikfout in een naam (`TEMPERATUUR` vs `temperatuur`; hoofdletters tellen!), of de regel die het maakt staat lager dan waar het gebruikt wordt. |
| `ModuleNotFoundError: No module named 'fles'` | Python vindt `fles.py` niet. | Het bestand is opgeslagen buiten de map `code\`. Sla op in dezelfde map als `fles.py` (Bestand → Opslaan als). |
| `ModuleNotFoundError: No module named 'requests'` | Het programma draait met een andere Python dan die van de cursus. | Start Thonny via `start.bat`, niet via een andere snelkoppeling. Rechtsonder in Thonny moet de Python uit de installatiemap staan. |
| `TypeError: ... takes ... positional arguments` | Een functie krijgt te veel of te weinig dingen mee. | Vergelijk de aanroep met het voorbeeld in de code. |
| `KeyError: 'message'` of `HTTPError: 404` | De server kent het model niet. | `MODEL` in `fles.py` is aangepast of het model is niet geïnstalleerd. Zet `MODEL` terug; controleer met `controleer.bat`. |
| `UnicodeEncodeError` | Een teken (emoji) kan niet worden getoond. | Komt zelden voor in Thonny. Haal de emoji weg of draai via `start.bat`. |
| `KeyboardInterrupt` | Iemand heeft op Stop gedrukt of Ctrl+C. | Geen fout. Opnieuw starten met F5. |

**Het bestand is helemaal stuk?** In de installatiemap staat de originele code nog in de bron (USB-stick of `installatie\sjabloon\code\`). Kopieer het bestand opnieuw, onder een nieuwe naam, zodat het eigen werk niet verloren gaat. Let op: de installer overschrijft bestaande code-bestanden bewust **niet**.

## 3. De geest doet raar

Dit is meestal **geen fout maar lesstof**. Vraag het tweetal: *"Waarom zou hij dat doen?"* en laat ze hun antwoord opschrijven.

| Wat gebeurt er? | Waarom? | Wat doe je? |
|---|---|---|
| Hij praat eindeloos door, herhaalt zichzelf | Kleine modellen raken in een lus. | `MAX_TOKENS` kapt hem af. Lagere temperatuur of een kortere systeemprompt ("Antwoord in maximaal twee zinnen") helpt. |
| Hij antwoordt in het Engels | Fietje is een Engels model (Phi-2) dat Nederlands heeft bijgeleerd. Bij Engelse woorden of code in de vraag schiet hij terug. | Systeemprompt: "Antwoord altijd in het Nederlands." Vraag in het Nederlands stellen. |
| Hij verzint dingen | Hallucinatie (hoofdstuk 14). | Prima lesmoment. Laat het controleren. |
| Hij speelt zijn rol niet (vergeet dat hij een piraat is) | De systeemprompt is te lang, te vaag of tegenstrijdig. | Kort en concreet maken. Een voorbeeldantwoord toevoegen werkt bij kleine modellen beter dan meer regels (zie hoofdstuk 15). |
| Hij geeft elke keer hetzelfde antwoord | Temperatuur 0 of een vaste `seed`. | Is zo bedoeld in level 2. Temperatuur omhoog of `seed` weg. |
| Hij zegt rare tekens, `<|im_end|>` of iets als `### Instruction` | Het model valt uit zijn chatsjabloon, vaak bij heel hoge temperatuur. | Temperatuur omlaag (onder 1,2). |
| Hij zegt iets ongepasts, gemeens of engs | Kleine modellen hebben weinig filters. | **Volg hoofdstuk 01 – Veiligheid.** Kort benoemen, niet uitvergroten, tweetal laten doorgaan of geest herstarten. Meld het bij de docent. |
| Hij "onthoudt" iets niet | In de meeste levels is er geen geheugen: elke vraag is los. | Dit is lesstof: vraag de tweetallen waarom dat zo is. |

## 4. In de klas

| Situatie | Tip |
|---|---|
| Het ene tweetal is klaar, het andere nog niet begonnen | Snelle tweetallen gaan naar *plus* en *expert*. Trage tweetallen slaan de TODO's over die met "(proberen)" zijn gemarkeerd. Niemand hoeft alles af te hebben. |
| Eén kind typt, de ander kijkt verveeld | Wissel elke TODO van toetsenbord. Of: één leest voor en bedenkt, de ander typt. |
| Kinderen kopiëren code van elkaar | Bij het geheime woord (level 4) is dat juist de bedoeling niet: woorden geheim houden. Bij andere levels: prima, als ze het kunnen uitleggen. |
| Kinderen proberen gemene of ongepaste dingen uit | Verwacht het; het hoort bij deze leeftijd. Grenzen staan in hoofdstuk 01. Richt de nieuwsgierigheid om: *"Wat denk je dat ChatGPT hier zou doen, en waarom?"* |
| Kinderen gaan op internet ChatGPT gebruiken | Mag soms, als vergelijking (afspraak docent). Maar de opdrachten werken met de eigen geest. |
| Een laptop crasht of valt uit | Opnieuw opstarten, `start.bat`. Werk in `code\` blijft bewaard als het was opgeslagen (Ctrl+S). Leer kinderen vaak op te slaan. |
| Geluid van 15 geesten tegelijk (level 5) | Koptelefoons of oortjes. Anders om de beurt laten spreken, of het volume laag. |
| Het netwerk valt uit | Lokaal draaien heeft geen netwerk nodig. Alleen tweetallen op de docent-server hebben last; zet die zo nodig lokaal. |

## 5. Snel controleren of een laptop in orde is

1. `controleer.bat` in de installatiemap dubbelklikken. Rood = probleem, met uitleg.
2. `start.bat`: Thonny opent met `level1_wek_je_geest.py`. Druk F5. Komt er een antwoord, dan werkt alles.
3. Werkt het niet en is de les al bezig: laat het tweetal meedoen bij een buurtweetal of op de docent-server, en los het na de les op. Een les staat niet stil voor één laptop.
