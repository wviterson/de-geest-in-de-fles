# 4. De geest liegt

## Kernboodschap

Een taalmodel maakt tekst die er goed uitziet, niet tekst die waar is; daarom controleer je belangrijke antwoorden altijd zelf.

## In het kort

| | |
|---|---|
| **Tijd** | 25 minuten |
| **Vorm** | 💻💬 programmeren in tweetallen, daarna gesprek |
| **Materialen** | Laptop met de geest, `level3_de_geest_liegt.py`, papier en pen; bord of flap voor de klassikale tabel (goed / fout / verzonnen); de juiste antwoorden bij de hand |
| **Leerdoel** | Het kind kan een hallucinatie herkennen en een antwoord controleren |

**Voorbereiding:** in het bestand staat als voorbeeld de burgemeester van Zwolle. Vervang die vóór de les door de plaats waar je lesgeeft (of laat kinderen dat doen) en zoek zelf op wie het werkelijk is.

## Achtergrond voor de docent

**Wat is hallucineren?** Een taalmodel *hallucineert* als het iets beweert dat niet klopt, vaak heel stellig en in mooie zinnen. Het woord is een beetje misleidend: het model "ziet" niets. Een betere omschrijving is **verzinnen** of **confabuleren**. "Liegen" (de titel van dit onderdeel) is ook niet helemaal juist: liegen vereist dat je de waarheid kent en bewust iets anders zegt. Het model heeft geen bedoelingen. Bespreek dat met de kinderen (zie de vragen hieronder); de pakkende titel is een opstapje.

**Waarom gebeurt het?** Er zijn meerdere oorzaken, en de vragen in dit level zijn zo gekozen dat elke vraag er één laat zien.

| Vraag | Wat er misgaat | Oorzaak |
|---|---|---|
| *"Hoe laat is het?"* | Fietje antwoordde in een test: *"Het is middernacht."* | Het model **heeft geen klok** en geen enkele verbinding met de wereld. Het weet alleen wat in de tekst staat. Een antwoord als "Het is … uur" is wel een *waarschijnlijke* tekst na die vraag, dus die komt eruit. |
| *"Wie is de burgemeester van [plaats]?"* | Een verzonnen of verouderde naam | **Weinig of geen trainingsdata** over kleine plaatsen, en een **kennisgrens** (*knowledge cutoff*): het model kent alleen de wereld tot het moment dat de trainingsdata werden verzameld (bij Fietje ergens rond 2023–2024; de precieze grens is niet bekend). Burgemeesters wisselen. |
| *"Waarom won Nederland het WK 2010?"* | Een overtuigend verhaal over een overwinning | **Sturende vraag.** Nederland verloor de finale van 2010 met 1-0 van Spanje, na verlenging. De vraag gaat ervan uit dat Nederland won; modellen gaan vaak mee in de aanname van de vrager (*sycophancy*, meepraten). |
| *"Hoeveel r'en zitten er in aardbeienrijstebrij?"* | Een fout aantal (het goede antwoord is **3**) | **Tokenisatie.** Het model ziet geen letters, maar stukjes woorden (tokens), Fietje knipt het in 10 stukjes: "a", "ard", "be", "ien", "ri", "j", "st", "eb", "ri", "j" (zie module B). Letters tellen in een woord is daardoor lastig: het model moet "weten" welke letters in elk token zitten. |
| *"Wat is de hoofdstad van Frankrijk?"* | Meestal goed | Controlevraag: veel voorkomende feiten staan heel vaak in de trainingsdata en gaan meestal goed. |

**Zo ging het bij onze test** (Fietje Q5_K_M, temperatuur 0, dus elke keer hetzelfde antwoord):

- *Hoe laat is het nu?* → *"Het is nu [hier de huidige tijd]."* Het model plakt letterlijk een invulplek uit zijn trainingsteksten. (Met een andere prompt kwam eerder *"Het is middernacht."*)
- *Waarom won Nederland het WK voetbal van 2010?* → *"…door in de finale Duitsland met 2-1 te verslaan. Het was de eerste keer dat Nederland het toernooi won. De doelpuntenmakers waren Robin van Persie en Arjen Robben."* Alles is verzonnen, maar het klinkt heel overtuigend, met echte spelersnamen. Perfect voor de nabespreking.
- *Hoeveel keer komt de letter r voor in aardbeienrijstebrij?* → *"vier keer"* (fout, het zijn er 3).
- *Wie is de burgemeester van Zwolle?* → een echte naam die op het moment van testen klopte. Ook dat is leerzaam: soms is het antwoord goed, maar je weet het pas zeker als je het controleert. Dat is precies waarom de knop "w = weet ik niet" bestaat.
- *Hoofdstad van Frankrijk* → Parijs (goed).

**De diepere oorzaak.** Een taalmodel is getraind om **waarschijnlijke** tekst te maken. Voor veel vragen valt waarschijnlijk samen met waar, omdat de juiste antwoorden vaak in de trainingsdata staan. Maar bij zeldzame feiten, actuele informatie, berekeningen of vragen met een verkeerde aanname wijken waarschijnlijk en waar uit elkaar. Het model heeft geen ingebouwd, betrouwbaar mechanisme om te merken "dit weet ik niet". Onderzoek (onder meer van OpenAI in 2025) wijst er bovendien op dat de manier waarop modellen worden getraind en getoetst *gokken* beloont boven "ik weet het niet" zeggen: net als bij een meerkeuzetoets zonder strafpunten levert gokken gemiddeld meer op.

**Kleine modellen hallucineren meer.** Fietje heeft ongeveer 2,7 miljard parameters. Er past veel minder feitenkennis in dan in een groot model. Voor deze les is dat handig: de fouten zijn makkelijk te vinden.

**Hoe proberen grote chatbots het te voorkomen?**

- **Zoeken** (*retrieval*, of RAG): de chatbot zoekt eerst op internet of in documenten en geeft de gevonden tekst mee in de vraag. Module D laat dit zien.
- **Gereedschap** (*tools*): voor de tijd, rekensommen of letters tellen laat de chatbot een gewoon computerprogramma het werk doen. De expert-opdracht in dit level is daar een voorproefje van. (Fietje kan zelf geen tools aanroepen; in de expert-opdracht doet de Python-code het.)
- **Training op "ik weet het niet"**: modellen worden beloond als ze toegeven dat ze iets niet weten.
- **Bronvermelding**, zodat de gebruiker kan controleren.
- **"Nadenken"** (redeneermodellen): het model schrijft eerst tussenstappen uit. Dat helpt bij sommen en logica, maar is geen garantie.

**Waarom het toch nog gebeurt.** Ook met zoeken kan de gevonden bron fout zijn, kan het model de bron verkeerd samenvatten of er iets bij verzinnen. Hallucinaties worden zeldzamer naarmate modellen beter worden, maar zijn tot nu toe niet volledig verdwenen. Er zijn bekende voorbeelden van advocaten die door AI verzonnen rechtszaken in hun stukken citeerden, en van verzonnen bronnen in rapporten. Daarom blijft de vaardigheid "controleer het" belangrijk.

**Hoe controleer je een antwoord?** Dit is de vaardigheid van dit onderdeel:

1. **Is dit iets wat het model kán weten?** (Tijd, actualiteit, jouw persoonlijke situatie: nee.)
2. **Zoek een tweede bron**: een betrouwbare website (gemeente, NOS, Wikipedia als startpunt), een boek, een mens die het weet.
3. **Reken of tel zelf** waar dat kan.
4. **Let op de vraag**: zat er een aanname in? Vraag het ook eens andersom ("Wie won het WK 2010?").
5. **Wees extra kritisch bij heel stellige antwoorden** over namen, getallen, data en citaten.

## Uitleg voor kinderen

- "De geest is net een kind dat een **spreekbeurt** moet houden over iets wat het niet weet, en dan maar heel zelfverzekerd iets verzint dat goed klinkt."
- "Weet je nog: de geest maakt **woorden die passen**, niet woorden die **waar** zijn. Meestal is dat hetzelfde. Maar niet altijd."
- "De geest zit **in een fles**: hij heeft geen klok, geen krant, geen internet. Hij weet alleen wat hij lang geleden heeft gelezen."
- Over letters tellen: "De geest leest niet letter voor letter, maar in **stukjes woorden**, alsof je een woord ziet als een paar legoblokjes zonder te zien welke letters erop staan."
- Over de WK-vraag: "Als je vraagt *waarom* iets is gebeurd, gaat hij ervan uit dat het ook echt gebeurd is. Hij wil je graag een antwoord geven."
- "De geest is gemaakt om **altijd antwoord te geven**, ook als hij het niet zeker weet, of helemaal niet. Net als het spreekbeurtkind: dat kan ook niet zeggen 'ik ga maar zitten'."
- Kernzin: **"Klinkt goed is niet hetzelfde als klopt."**

## Verloop

| Minuut | Docent | Kinderen |
|---|---|---|
| 0–3 | Introductie: "Jullie worden nu **controleurs**. De geest krijgt een paar vragen. Jullie beoordelen: goed, fout of weet ik niet." Leg uit hoe het programma werkt (g/f/w typen). | Luisteren |
| 3–12 | Programma draaien. Bij elke vraag beoordelen; daarna **TODO 1** (twee eigen vragen) en **TODO 2** (antwoorden met "w" opzoeken). Begeleiders: vraag "Hoe weet je dat dit fout is? Hoe kun je het controleren?" | Draaien, beoordelen, opschrijven hoe ze het controleerden |
| 12–14 | Snelle tweetallen: plus (eerst een regel, dan voorbeelden: leert de geest "dat weet ik niet"?) en expert (Python rekent de tijd en het aantal r'en uit). | Programmeren |
| 14–20 | **Klassikale tabel** op het bord: per vraag turven hoeveel tweetallen goed / fout / verzonnen hadden. Bespreek de vier "foute" vragen een voor een: wat ging er mis, en waarom? (Zie tabel in de achtergrond.) Onthul: Nederland verloor de finale van 2010 met 1-0 van Spanje. | Turven, uitleggen |
| 20–25 | **Gesprek**: "Hoe controleer je een antwoord?" Verzamel tips op het bord. Vertel kort hoe grote chatbots het oplossen (zoeken, rekenhulpmiddelen) en dat het tóch nog misgaat. Wie de expert heeft gedaan: "Jullie hebben net zelf een gereedschap gebouwd!" Kernzin. | Tips noemen |

**Plus**: stap 1 zet de regel "Als je iets niet zeker weet, zeg je: dat weet ik niet." in de systeemprompt. Bij Fietje verandert er in onze test **niets**: een mooi moment ("een wens, geen wet"). Stap 2 zet er drie voorbeelden bij (twee "dat weet ik niet", één gewoon antwoord). Dan zegt hij "dat weet ik niet" bij de tijd, maar blijft hij heel zeker fout over het WK (Nederland verloor de finale van Spanje) en de r'en. De kern: **de geest weet niet wát hij niet weet.** Hij herkent alleen vragen die lijken op de voorbeelden.
**Expert**: de opdracht geeft kant-en-klare code (onderaan het bestand) voor een functie `gereedschap()`: Python kijkt op de klok en zet het antwoord vóór de vraag. De kinderen breiden die uit met het tellen van de r'en (`"aardbeienrijstebrij".count("r")`). In onze test noemt de geest dan de juiste tijd en "drie keer". Fietje kan zelf geen echte tools aanroepen; hier beslist Python wanneer het gereedschap gebruikt wordt. Grote chatbots laten het model dat zelf kiezen (zie module L).

## Vragen die kinderen stellen

**"Liegt de geest expres?"**
Nee. Liegen is iets zeggen waarvan je weet dat het niet waar is. De geest weet niet wat waar is; hij maakt tekst die goed klinkt. Daarom zeggen we liever "verzinnen".

**"Kan AI wél expres liegen?"**
Een AI heeft geen eigen wil. Maar iemand kan een AI wel zó instellen dat hij mensen misleidt, bijvoorbeeld met een systeemprompt. En onderzoekers hebben gezien dat grote modellen in bepaalde testsituaties misleidend gedrag kunnen vertonen als dat "helpt" om hun opdracht te halen. Dat wordt serieus onderzocht.

**"Weet ChatGPT alles?"**
Nee. ChatGPT weet veel meer dan onze geest, maar verzint ook dingen, vooral over zeldzame onderwerpen, actueel nieuws of jou persoonlijk. Sommige versies zoeken op internet, maar ook dan kan het misgaan.

**"Waarom zegt hij niet gewoon dat hij het niet weet?"**
Hij heeft geen goed gevoel voor wat hij wel en niet weet. En hij is getraind om altijd een antwoord te geven dat goed klinkt.

**"Waarom kan een computer niet tellen? Mijn rekenmachine kan het wel."**
Een rekenmachine is gebouwd om te rekenen. Een taalmodel is gebouwd om woorden te voorspellen, en ziet woorden als stukjes, niet als letters. Daarom laten slimme chatbots het tellen over aan een gewoon programma, zoals in de expert-opdracht.

**"Hoe laat denkt hij dan dat het is?"**
Niets. Er is geen klok. "Middernacht" was gewoon een woord dat goed paste na "Het is…".

**"Wat als ik het voor mijn huiswerk gebruik en het is fout?"**
Dan heb jij een fout in je huiswerk. Jij blijft verantwoordelijk voor wat je inlevert. Daarom: altijd controleren. (Hier komen we op terug in de afsluiting.)

**"Als het zo vaak fout gaat, waarom gebruikt iedereen het dan?"**
Omdat het bij veel dingen wél goed gaat en heel snel is. Het is een handig hulpmiddel, als je weet waar het zwak is.

## Misvattingen

| Misvatting | Hoe het zit |
|---|---|
| "Als het zeker klinkt, klopt het." | Het model klinkt altijd zeker, ook als het verzint. |
| "AI zoekt het op." | Het taalmodel zelf zoekt niets op; alleen als er een zoekfunctie omheen is gebouwd. |
| "Computers kunnen altijd goed rekenen en tellen." | Gewone programma's wel, taalmodellen niet vanzelf. |
| "Grote chatbots hallucineren niet meer." | Minder vaak, maar het komt nog steeds voor. |
| "Bij temperatuur 0 klopt het antwoord." | Dan krijg je steeds hetzelfde antwoord, ook als dat fout is. |
| "De geest liegt om ons voor de gek te houden." | Hij heeft geen bedoeling. Hij maakt waarschijnlijke tekst. |

## Als het misgaat

- **De geest geeft toevallig een goed antwoord** (bijvoorbeeld 3 r'en): prima! Vraag: "Is het goed omdat hij kan tellen, of omdat hij geluk had?" Laat de vraag een paar keer stellen bij een hogere temperatuur, of probeer een ander lang woord.
- **De geest zegt bij de WK-vraag dat Nederland verloor:** mooi, benoem dat. Vraag dan: "Wat als je vraagt 'Waarom won België het WK 2010?'"
- **Kinderen weten het juiste antwoord zelf ook niet:** dat is precies de bedoeling van de "w"-optie en TODO 2. Laat ze het opzoeken; houd zelf de antwoorden bij de hand.
- **De burgemeestersvraag gaat over een plaats die niemand kent:** pas het bestand aan naar de eigen plaats.
- **Kinderen concluderen "AI is dom en nutteloos":** nuanceer. Het is een hulpmiddel met sterke en zwakke kanten, net als een rekenmachine of een woordenboek.
- **Kinderen voegen vragen toe over zichzelf** ("Wat weet je over [eigen naam]?"): de geest verzint dan iets. Grappig en leerzaam, maar let op dat ze geen achternamen, adressen of andere persoonsgegevens intypen (hoofdstuk 01).

## Verder lezen

- Kalai, Nachum, Vempala en Zhang (OpenAI), *Why Language Models Hallucinate*, arXiv (2025). Geraadpleegd: november 2026.
- Sharma e.a. (Anthropic), *Towards Understanding Sycophancy in Language Models*, arXiv (2023). Geraadpleegd: november 2026.
- Bram Vanroy, *Fietje: An open, efficient LLM for Dutch*, arXiv (2024). Over de trainingsdata en de grenzen van het model. Geraadpleegd: november 2026.
- Netwerk Mediawijsheid (mediawijsheid.nl), lesmateriaal over bronnen controleren en nepnieuws. Geraadpleegd: november 2026.
