# 1. Het menselijke taalmodel

## Kernboodschap

Een taalmodel doet steeds maar één ding: het volgende woord voorspellen, en dat heel vaak achter elkaar.

## In het kort

| | |
|---|---|
| **Tijd** | 15 minuten |
| **Vorm** | 🔌 unplugged, in groepjes van 4 |
| **Materialen** | Per groepje een A4 en een pen; een startzin per groepje (op een kaartje of op het bord); docentlaptop met `geest.py` |
| **Leerdoel** | Het kind kan uitleggen dat een taalmodel steeds het volgende woord voorspelt |

## Achtergrond voor de docent

**Volgende-token-voorspelling.** Een taalmodel krijgt tekst binnen en berekent voor elk mogelijk volgend stukje tekst hoe waarschijnlijk het is. Die stukjes heten **tokens**: vaak hele woorden, soms delen van woorden (Fietje knipt "aardbeienrijstebrij" bijvoorbeeld in 10 stukjes: a|ard|be|ien|ri|j|st|eb|ri|j), leestekens of spaties. Het model kiest één token, plakt dat achter de tekst en begint opnieuw, nu met de tekst *inclusief* dat nieuwe token. Dit herhaalt zich tot het model een speciaal "ik ben klaar"-token kiest of een maximumlengte bereikt. Een antwoord van honderd woorden is dus ruim honderd losse voorspellingen achter elkaar.

**Het model plant (grotendeels) niet vooruit.** Het schrijft geen heel antwoord in zijn hoofd en typt het dan uit. Elk token wordt gekozen op basis van alles wat er al staat. Onderzoek laat zien dat er binnen grote modellen wel enige vorm van vooruitkijken zit (bijvoorbeeld bij rijmwoorden), maar het basisprincipe blijft: één token tegelijk, en wat er eenmaal staat, staat er. Daarom kan een model zichzelf "vastschrijven": als het eenmaal "Nederland won het WK in 2010 omdat…" heeft geschreven, gaat het verder op die (foute) lijn.

**Wat het model gebruikt om te voorspellen.** Alles wat in het gesprek staat (systeemprompt, vraag, eerdere antwoorden) plus wat het tijdens de training heeft geleerd over welke woorden na welke woorden komen. Het "kijkt" naar de hele tekst tegelijk en weegt af welke eerdere woorden belangrijk zijn voor de volgende keuze (dat heet *attention*; de details hoeven kinderen niet te weten).

**De koppeling met het spel.** In het spel doen kinderen precies dit: ze horen wat er al staat en zeggen één woord dat er logisch achter past. Niemand kent het hele verhaal vooraf. Toch ontstaat er een (soms absurd) verhaal. Je zult zien dat:

- de verhalen grammaticaal meestal kloppen (iedereen kent de taal);
- de verhalen inhoudelijk vaak raar afslaan (niemand plant vooruit);
- sommige kinderen het "voor de hand liggende" woord kiezen en anderen juist een grappig woord.

Dat laatste is de brug naar **temperatuur** (onderdeel 3).

**Streaming.** In `geest.py` verschijnt het antwoord woord voor woord op het scherm. Dat is geen effect om het spannend te maken: het model maakt het antwoord écht stukje voor stukje, en Ollama stuurt elk stukje door zodra het klaar is (*streaming*). ChatGPT en andere chatbots doen hetzelfde; daarom zie je daar het antwoord ook "getypt" worden.

**Grenzen van de vergelijking.** Kinderen kiezen een woord met hun begrip van de wereld, gevoel voor humor en bedoelingen. Het model kiest op basis van statistische patronen uit tekst. Gebruik het spel om het *mechanisme* te laten voelen, niet om te suggereren dat het model denkt zoals een mens.

## Uitleg voor kinderen

- "Kennen jullie de woordvoorspelling op je telefoon? Je typt 'Ik kom zo…' en je telefoon stelt 'thuis' voor. Een taalmodel is **autocomplete met superkrachten**: het heeft zoveel tekst gelezen dat het heel goed kan raden wat er komt."
- "Maar het raadt steeds maar **één woord**. Dan nog één. Dan nog één. Net zo lang tot het antwoord af is."
- Na het spel: "Wisten jullie aan het begin hoe jullie verhaal zou aflopen? Nee! En toch kwam er een verhaal uit. Zo werkt de geest ook."
- "Het antwoord van de geest verschijnt woord voor woord. Dat is niet om het spannend te maken: hij weet zelf ook pas wat het volgende woord wordt als hij het vorige heeft gekozen."

## Verloop

| Minuut | Docent | Kinderen |
|---|---|---|
| 0–2 | Uitleg: groepjes van 4, één vel papier, startzin bovenaan (bijvoorbeeld *"Op een dag vond ik een fles op het strand en…"* of *"De geest in de laptop werd wakker en zei…"*). Om de beurt zegt ieder **precies één woord** hardop; **één kind per groepje schrijft** alles op (en doet zelf ook mee). Niet overleggen, niet vooruit plannen. | Vormen groepjes, kiezen een schrijver |
| 2–7 | Laat 5 minuten spelen. Loop rond. Roep halverwege "Nog 2 minuten! Probeer er een eind aan te breien." | Zeggen om de beurt een woord |
| 7–10 | Laat 3–4 groepjes hun verhaal voorlezen. Lach mee. | Voorlezen, luisteren |
| 10–12 | Nabespreking: "Wist iemand vooraf hoe het zou eindigen? Hoe kozen jullie je woord? Klopte de grammatica? Klopte het verhaal?" Kernzin: *"Een taalmodel doet precies dit: steeds één woord erbij."* | Antwoorden |
| 12–15 | **Demo**: start `geest.py` op de beamer en stel een vraag die een lang antwoord geeft ("Vertel een verhaal over een geest in een fles"). Laat zien hoe het woord voor woord verschijnt. *"Dat deden jullie net ook."* | Kijken |

### Varianten

- **Temperatuur 0 en temperatuur 2.** Geef in elk groepje twee kinderen stiekem een rolkaartje:
  - **"Temperatuur 0"**: kies altijd het meest voor de hand liggende woord.
  - **"Temperatuur 2"**: kies een verrassend of gek woord (maar wel een bestaand woord).
  - Laat de anderen na afloop raden wie welke rol had. Mooie opstap naar onderdeel 3.
- **Alleen het laatste woord horen.** De schrijver fluistert alleen het laatste woord in het oor van de volgende speler; niemand anders hoort het verhaal. Het verhaal wordt veel chaotischer. Dat is de les: het model kijkt naar **alles** wat er al staat (de *context*), en dat maakt het goed.
- **Hele klas in een kring.** Bij weinig tijd: de klas maakt samen één verhaal, ieder zegt één woord hardop.
- **Snelle variant op het bord.** De docent schrijft een zin, de klas roept welk woord er volgt, de docent turft de antwoorden. "Kijk, 12 keer 'thuis', 3 keer 'terug', 1 keer 'banaan'. Zo'n lijstje met kansen heeft de geest ook." (Opstap naar de dobbelsteen.)

## Vragen die kinderen stellen

**"Weet de geest dan niet wat hij gaat zeggen?"**
Niet zoals jij. Hij kiest steeds het volgende woord op basis van alles wat er al staat. Er is geen kant-en-klaar antwoord dat hij alleen nog uittypt.

**"Hoe weet hij welk woord goed is?"**
Hij heeft van heel veel tekst geleerd welke woorden vaak na elkaar komen. "Goed" betekent voor hem: "past hier waarschijnlijk", niet "is waar".

**"Waarom typt hij zo langzaam?"**
Voor elk woord moet de laptop miljarden rekensommetjes doen. Op een snelle computer gaat het veel sneller.

**"Is het niet gewoon nep, dat woord-voor-woord-verschijnen?"**
Nee, het model maakt het echt zo. Je ziet de woorden zodra ze klaar zijn.

**"Zijn het echt woorden, of letters?"**
Stukjes woorden, *tokens* genoemd. Een kort woord is vaak één token, een lang woord wordt in stukjes geknipt. (Meer daarover in het hoofdstuk over tekst.)

**"Als hij alleen woorden voorspelt, hoe kan hij dan sommen maken of code schrijven?"**
Hij heeft heel veel sommen en code gezien en geleerd welke tekens vaak volgen. Bij simpele dingen gaat dat goed; bij lastige sommen gaat het vaak mis. Dat zie je straks bij "De geest liegt".

**"Kan ik ook zo'n geest maken met alle tekst van mijn groepsapp?"**
In principe kun je een model trainen op allerlei tekst. Maar met zo weinig tekst wordt het niet slim, en tekst van anderen gebruiken zonder toestemming is niet oké.

## Misvattingen

| Misvatting | Hoe het zit |
|---|---|
| "AI schrijft eerst het hele antwoord en laat het dan langzaam zien." | Het antwoord ontstaat echt stukje voor stukje. |
| "AI zoekt een passend antwoord op uit een database." | Er is geen lijst met antwoorden. Elk antwoord wordt nieuw opgebouwd uit voorspellingen. |
| "Het model begrijpt het verhaal zoals een mens." | Het herkent patronen in tekst heel goed. Of en hoeveel het "begrijpt", is een open vraag, maar het is in elk geval anders dan bij mensen. |
| "Het voorspelde woord is het juiste woord." | Het is het *waarschijnlijke* woord. Waarschijnlijk is niet hetzelfde als waar. |

## Als het misgaat

- **Groepjes gaan overleggen of samen een plan maken:** herhaal de regel "één woord, niet overleggen". Of laat het juist gebeuren en vraag bij de nabespreking of het verhaal daardoor beter werd. (Dat lijkt op wat grote modellen intern doen met "nadenken".)
- **Kinderen schrijven grove of kwetsende woorden:** kort ingrijpen; de spelregel is "woorden die je ook tegen je juf zou zeggen".
- **Een kind vindt schrijven lastig (dyslexie, taalachterstand):** geen probleem, alleen de schrijver schrijft. Kies als schrijver een kind dat dat graag doet.
- **Tijd is op en niet iedereen heeft voorgelezen:** twee of drie verhalen is genoeg; hang de rest op.
- **De demo geeft een kort antwoord:** vraag om "een lang verhaal van minstens tien zinnen".

## Verder lezen

- 3Blue1Brown, *But what is a GPT? Visual intro to transformers* (2024), YouTube. Geraadpleegd: november 2026.
- Ollama API-documentatie, onderdeel *Generate a chat completion* (streaming): <https://docs.ollama.com/api/chat>. Geraadpleegd: november 2026.
- *Elements of AI*, gratis online cursus (Universiteit van Helsinki), ook in het Nederlands. Geraadpleegd: november 2026.
