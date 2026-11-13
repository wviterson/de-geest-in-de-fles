# 6. De geest krijgt een stem

## Kernboodschap

Ook de stem van de geest is een klein neuraal netwerk dat van echte stemmen heeft geleerd; daarom kan AI tegenwoordig ook stemmen nadoen, en moet je niet alles geloven wat je hoort.

## In het kort

| | |
|---|---|
| **Tijd** | 15 minuten |
| **Vorm** | 💻 programmeren in tweetallen |
| **Materialen** | Laptop met de geest en Piper-stemmen, `level5_stem.py`, **koptelefoons of oortjes** |
| **Leerdoel** | Het kind kan zijn geest hardop laten praten |

## Achtergrond voor de docent

**Tekst-naar-spraak (TTS).** Een TTS-systeem zet geschreven tekst om in gesproken geluid. Vroeger gebeurde dat door stukjes opgenomen spraak aan elkaar te plakken of met regels die geluid "nabouwden"; dat klonk robotachtig. Moderne systemen gebruiken een **neuraal netwerk** dat getraind is op uren opnames van echte sprekers, met de bijbehorende tekst. Het netwerk leert zo hoe letters en woorden klinken, inclusief klemtoon en intonatie, en maakt zelf het geluid.

**Piper.** Onze geest praat met **Piper**, een open-source TTS-systeem dat oorspronkelijk is ontwikkeld voor het spraakassistent-project van Home Assistant (Rhasspy/Open Home Foundation). Belangrijke kenmerken:

- Het draait **offline** en snel, ook op gewone laptops en zelfs op een Raspberry Pi.
- Elke stem is een **apart klein model** (een `.onnx`-bestand van zo'n 60 MB in de *medium*-kwaliteit) plus een instellingenbestand (`.onnx.json`).
- Er zijn meerdere Nederlandse en Vlaamse stemmen. Standaard geïnstalleerd: `nl_NL-pim-medium`, `nl_NL-ronnie-medium` en `nl_BE-nathalie-medium` (Vlaams).
- Een stem is meestal getraind op opnames van één spreker, vaak uit openbaar beschikbare spraakdatasets. De herkomst en licentie verschillen per stem en staan in de modelkaart bij elke stem op Hugging Face.

Ter vergelijking: het taalmodel Fietje is ongeveer 2 GB, een Piper-stem ongeveer 60 MB. Spraak maken is een veel smallere taak dan "alles over taal weten", dus kan het netwerk veel kleiner.

**Hoe het werkt in de code.** `level5_stem.py` gebruikt de functie `zeg(tekst, stem=..., snelheid=...)` uit het hulpbestand `stem.py`. De geest maakt eerst zijn tekstantwoord (taalmodel), daarna zet Piper die tekst om in geluid (spraakmodel). Er zijn dus **twee AI-modellen** aan het werk, na elkaar. Grote spraakassistenten werken vaak ook zo: spraakherkenning → taalmodel → spraaksynthese. De nieuwste systemen combineren dat soms in één model dat direct met geluid werkt.

Werkt Piper niet, dan valt `zeg()` terug op de ingebouwde Windows-stem, die op de meeste laptops alleen Engels spreekt. Dat klinkt dan grappig fout; geen probleem voor de les.

**Stemmen klonen en deepfake-audio.** Hetzelfde principe kan worden gebruikt om een **specifieke** stem na te maken. Waar je vroeger uren opnames nodig had, kunnen moderne systemen een stem al redelijk overtuigend nadoen met korte opnames (soms enkele seconden tot minuten, afhankelijk van het systeem en de gewenste kwaliteit). Dat heeft goede toepassingen (mensen die hun stem verliezen door ziekte, nasynchronisatie), maar ook risico's:

- **Oplichting**: fraudeurs doen zich voor als familielid of collega ("Mam, ik zit in de problemen, kun je geld overmaken?"). Dat gebeurt al via tekstberichten; met een nagemaakte stem wordt het overtuigender.
- **Nepopnames** van bekende personen, bijvoorbeeld politici, om nepnieuws te verspreiden.
- **Pesten**: nepopnames van klasgenoten.

Tips die je kinderen kunt meegeven: bel bij een vreemd verzoek **zelf terug** op het bekende nummer; spreek in het gezin een **codewoord** af; wees voorzichtig met het online zetten van veel spraakopnames van jezelf.

**Regelgeving.** De Europese AI-verordening (EU AI Act) verplicht onder meer dat door AI gemaakte of bewerkte beeld-, geluids- en video-inhoud die op echt lijkt (*deepfakes*), als zodanig herkenbaar wordt gemaakt. Die transparantieregels (artikel 50) gelden sinds 2 augustus 2026; voor sommige verplichtingen gelden overgangstermijnen, en de precieze uitwerking en handhaving zijn nog in ontwikkeling.

## Uitleg voor kinderen

- "De geest kan nu schrijven, maar nog niet praten. Daarvoor halen we een **tweede, kleinere geest** erbij: een stemgeest."
- "Die stemgeest heeft uren geluisterd naar één echte persoon die zinnen voorlas. Zo heeft hij geleerd hoe tekst klinkt. Nu kan hij elke zin uitspreken, ook zinnen die die persoon nooit gezegd heeft."
- "Eerst schrijft de taalgeest het antwoord, dan leest de stemgeest het voor. Twee AI's die samenwerken."
- Kort gesprekje aan het eind: "Als een computer zo een stem kan leren… wat als iemand **jouw** stem of die van je moeder nadoet? Hoe weet je dan of een spraakbericht echt is?"

## Verloop

| Minuut | Docent | Kinderen |
|---|---|---|
| 0–2 | Koptelefoons uitdelen. Korte uitleg: twee geesten, eentje schrijft, eentje praat. Laat op de beamer één keer `zeg("Hallo, ik ben de geest!")` horen. | Luisteren |
| 2–9 | `level5_stem.py` openen. **TODO 1**: stem en snelheid kiezen. **TODO 2**: de systeemprompt van de eigen geest uit level 1 erin plakken. Praten met de geest. | Programmeren, luisteren |
| 9–11 | Snelle tweetallen: plus (past de stem bij de geest? alle stemmen proberen, snelheid 1.6) en expert (twee geesten met elk een eigen stem die met elkaar praten). | Programmeren |
| 11–15 | **Gesprekje**: "Ook deze stem is een klein neuraal netwerk, getraind op een echte spreker. Wat kan daar misgaan?" Bespreek stemmen klonen en oplichting met nagemaakte stemmen. Tip: zelf terugbellen, codewoord in het gezin. | Praten |

**Plus**: alle stemmen en snelheden uitproberen; past de stem bij de persona?
**Expert**: twee geesten met eigen systeemprompt én eigen stem laten praten; het antwoord van de één is de vraag voor de ander. Waar praten ze na zes beurten over? (Vaak dwalen ze af of gaan ze in herhaling: mooi gespreksonderwerp.)

## Vragen die kinderen stellen

**"Van wie is deze stem?"**
Van een echte persoon die zinnen heeft ingesproken; die opnames zijn openbaar gedeeld om er onder meer spraaktechnologie mee te maken. De computer heeft daarvan geleerd hoe die stem klinkt.

**"Kan hij ook mijn stem nadoen?"**
Deze stemmen niet; die zijn al klaar getraind. Maar er bestaan programma's die met een korte opname een stem kunnen nadoen. Daarom: wees voorzichtig met opnames van jezelf online.

**"Waarom spreekt hij sommige woorden raar uit?"**
De stem heeft niet alle woorden geleerd. Bij moeilijke, Engelse of verzonnen woorden moet hij raden hoe het klinkt. Getallen, afkortingen en emoji gaan ook vaak mis.

**"Waarom praat hij Engels / met een raar accent?"**
Waarschijnlijk werkt Piper niet en gebruikt de laptop de Windows-stem, die alleen Engels kent. Vraag een begeleider.

**"Is Siri / Alexa / Google ook zo?"**
Ongeveer: die gebruiken ook neurale netwerken om te spreken, maar veel grotere en meestal in de cloud.

**"Heeft de geest nu ook gevoelens, nu hij een stem heeft?"**
Nee. Een stem maakt hem levensechter, maar het is nog steeds tekst die wordt voorgelezen. Juist daarom moet je extra opletten: een stem voelt heel menselijk.

**"Kan hij ook zingen?"**
Piper niet echt. Er bestaan wel AI-modellen die muziek en zang maken.

**"Is het verboden om iemands stem na te maken?"**
Iemands stem namaken en gebruiken zonder toestemming kan onrechtmatig zijn, en voor oplichting gebruiken is strafbaar. Met toestemming en voor de grap thuis is iets anders. En in Europa moet nep-geluid dat echt lijkt, herkenbaar zijn als AI.

## Misvattingen

| Misvatting | Hoe het zit |
|---|---|
| "De computer leest gewoon opgenomen woorden voor." | Een neuraal netwerk maakt het geluid nieuw, ook voor zinnen die nooit zijn ingesproken. |
| "De stem en de geest zijn één AI." | Het zijn twee aparte modellen: één voor tekst, één voor spraak. |
| "Als ik iemands stem hoor, is hij het ook." | Stemmen zijn na te maken. Bij vreemde verzoeken: zelf terugbellen. |
| "Een stem maakt een AI slimmer of levender." | Het maakt hem alleen menselijker om te horen. |

## Als het misgaat

- **Geen geluid:** volume, koptelefoon, juiste geluidsuitgang in Windows. Test met `stem.py` (F5).
- **Engelse robotstem:** Piper werkt niet en `zeg()` valt terug op de Windows-stem. Controleer of de map `stemmen` de `.onnx`- én `.onnx.json`-bestanden bevat. Als het niet snel lukt: laat het zo; het is geen ramp.
- **Foutmelding over een onbekende stem:** stemnaam verkeerd getypt. Laat `print(stemmen())` zien welke er zijn (staat bovenaan het programma).
- **Het lokaal is een kakofonie:** koptelefoons, of afspreken dat alleen snelheid en stem kort getest worden en de rest met het geluid zacht.
- **De geest geeft lange antwoorden en blijft praten:** in de systeemprompt "antwoord kort" zetten. Het programma wacht tot de zin is uitgesproken.
- **Kinderen laten de geest ongepaste dingen zeggen** (met een stem is dat extra verleidelijk): hoofdstuk 01. Hardop ongepaste tekst laten uitspreken is niet de bedoeling.
- **Kinderen worden onrustig van het deepfake-onderwerp:** houd het kort en praktisch (terugbellen, codewoord). Het hoeft niet eng te worden.

## Verder lezen

- Piper, broncode en documentatie: <https://github.com/rhasspy/piper> (het project is inmiddels verhuisd naar de Open Home Foundation; de link verwijst daarnaar). Geraadpleegd: november 2026.
- Piper, voorbeelden van alle stemmen: <https://rhasspy.github.io/piper-samples/>. Geraadpleegd: november 2026.
- Europese Commissie, *AI Act* (beleidspagina over de Europese AI-verordening): <https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai>. Geraadpleegd: november 2026.
- Fraudehelpdesk.nl, informatie over oplichting via WhatsApp en telefoon. Geraadpleegd: november 2026.
