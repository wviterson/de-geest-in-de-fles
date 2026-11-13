# 0. Opening: de geest ontwaakt

## Kernboodschap

ChatGPT en zijn vrienden wonen in enorme datacenters, maar een (kleinere) geest past ook in jouw laptop, helemaal zonder internet.

## In het kort

| | |
|---|---|
| **Tijd** | 15 minuten |
| **Vorm** | 🎤💬 demo door de docent en stelling |
| **Materialen** | Docentlaptop met beamer en geluid, de geest geïnstalleerd en getest, stelling op dia of papier |
| **Leerdoel** | Het kind kan zeggen waar ChatGPT en dergelijke "wonen" (datacenter) en dat het ook op een laptop kan |

## Achtergrond voor de docent

**Waar "wonen" grote chatbots?** Als je een vraag typt in ChatGPT, Gemini, Copilot of Claude, gaat je tekst via internet naar een **datacenter**: een enorm gebouw vol servers met speciale rekenchips (meestal GPU's of vergelijkbare AI-chips). Daar draait het model, het antwoord wordt uitgerekend en via internet teruggestuurd. Die modellen zijn te groot voor een gewone computer: ze hebben tientallen tot honderden gigabytes aan geheugen nodig, verdeeld over meerdere chips. De bedrijven bouwen daarom steeds meer en grotere datacenters, wat veel stroom, koelwater en geld kost (verdieping in module I).

**Wat draait er op de laptop?** Ollama is een programma dat taalmodellen op je eigen computer laat draaien. Het model zelf is een groot bestand met getallen (de *parameters*). Fietje heeft ongeveer 2,7 miljard parameters; in de versie die wij gebruiken (Q5_K_M) zijn die getallen afgerond om ruimte te besparen, waardoor het bestand ongeveer **2 GB** is. Dat past in het werkgeheugen van een gewone laptop. Het rekenwerk gebeurt dan op de processor van de laptop. Daarom is de geest trager en minder slim dan ChatGPT, maar hij werkt **zonder internet**.

**Wie maakte Fietje?** Fietje is gemaakt door **Bram Vanroy** (KU Leuven) en in 2024 openbaar gemaakt. Het is gebaseerd op **Phi-2**, een klein Engelstalig model van Microsoft, dat verder is getraind op een grote hoeveelheid Nederlandse tekst. Daarna is er een chatversie van gemaakt die op vragen kan antwoorden. Het is een *open* model (*open weights*): iedereen mag het downloaden en gebruiken. De chatversie heeft wel een niet-commerciële licentie (CC BY-NC 4.0): geld verdienen ermee mag niet. Zie module J voor het verschil tussen open source en open weights.

**Waarom laten we zien dat het netwerk uit staat?** Veel kinderen (en volwassenen) denken dat AI "het internet" is of dat het antwoord wordt "opgezocht". Door het netwerk uit te zetten maak je zichtbaar dat het model **alles wat het kan in zichzelf meedraagt**: alleen de getallen die het tijdens de training heeft geleerd. Het zoekt niets op. Dat is meteen de basis voor onderdeel 4 (de geest weet niet hoe laat het is).

**Waarom een stelling al aan het begin?** De stelling *"Een AI die je altijd gelijk geeft, is een goede vriend"* komt terug in de afsluiting. Door kinderen er nu al een mening over te laten geven, kunnen ze aan het eind merken of hun mening is veranderd. Dat maakt het leereffect zichtbaar, voor hen én voor jou. Je hoeft de stelling nu nog niet te bespreken; alleen de handen tellen en noteren.

**Let op met de docent-server.** Gebruiken de kinderen jouw laptop als server (route D in `INSTALLATIE.md`), dan moet jouw netwerk aan blijven. Doe de demo dan vóórdat de kinderen hun laptops koppelen, of laat zien dat **een kinderlaptop** met het netwerk uit nog steeds werkt (als die zelf het model draait). Alternatief: haal kort de netwerkkabel eruit of laat het wifi-icoon zien met "geen verbinding", en zet het daarna weer aan.

## Uitleg voor kinderen

- "Wie heeft weleens ChatGPT of een andere chatbot gebruikt? Waar denk je dat die woont?"
- "ChatGPT woont in een **datacenter**: een gebouw zo groot als een paar voetbalvelden, vol computers die dag en nacht zoemen. Jouw vraag reist daar via internet naartoe en het antwoord reist terug."
- "Vandaag gaan we iets anders doen. We stoppen een **geest in een fles**, en die fles is jullie laptop. Hij is kleiner en dommer dan ChatGPT, maar hij woont bij jou. Hij heeft geen internet nodig, en niemand anders kan meelezen."
- "Een geest in een fles is machtig, maar hij doet wél **letterlijk** wat je zegt. En hij weet niets van wat er buiten de fles gebeurt. Onthoud dat; dat komt vanmiddag terug."

## Verloop

| Minuut | Docent | Kinderen |
|---|---|---|
| 0–3 | Welkom, korte voorstelronde van docent en begeleiders. "Wie heeft weleens met een chatbot gepraat?" (handen) | Steken handen op, noemen apps |
| 3–5 | "Waar woont ChatGPT?" Laat een foto van een datacenter zien. Leg uit: vraag gaat via internet heen en weer. | Raden, luisteren |
| 5–10 | **Demo.** Zet zichtbaar het netwerk uit (wifi-icoon op de beamer). Start `geest.py` en stel een vraag, bijvoorbeeld "Wie ben jij?" of "Vertel een mopje over een fiets." Laat het antwoord woord voor woord verschijnen. Vraag: "Hoe kan dit, zonder internet?" | Kijken, reageren, raden |
| 10–13 | **Stelling** (handen omhoog): *"Een AI die je altijd gelijk geeft, is een goede vriend."* Eens / oneens / weet niet. Tel en noteer de verhouding op het bord of een flap. "Daar komen we aan het eind op terug." | Kiezen een kant |
| 13–15 | Vooruitblik: "Vanmiddag gaan jullie je eigen geest wekken, laten liegen, hacken en laten praten." Laat de regels uit hoofdstuk 01 kort zien (geen persoonsgegevens, aardig blijven). | Luisteren |

Tip: oefen de demo vooraf met precies dezelfde vraag. Fietje kan wisselende antwoorden geven. Een raar antwoord is niet erg; benoem het gewoon ("Hij is nog wat slaperig").

## Vragen die kinderen stellen

**"Hoe kan hij antwoorden zonder internet?"**
Alles wat hij kan, zit al in het bestand op de laptop: ongeveer 2 GB aan getallen die hij tijdens zijn training heeft geleerd. Hij zoekt niets op.

**"Is dit ChatGPT?"**
Nee. Het is Fietje, een veel kleiner, Nederlands model. Het werkt wel op dezelfde manier als ChatGPT, alleen kleiner.

**"Waarom is hij zo langzaam?"**
Je laptop moet al het rekenwerk alleen doen. ChatGPT gebruikt duizenden supersnelle computers tegelijk.

**"Kan hij mijn laptop hacken of virussen maken?"**
Nee. Onze geest kan alleen tekst teruggeven aan ons Python-programma. Hij kan niets op je laptop aanzetten, openen of veranderen.

**"Leest iemand mee wat ik typ?"**
Bij onze geest niet: alles blijft op de laptop. Bij ChatGPT en andere apps gaan je berichten wél naar het bedrijf.

**"Is de geest levend?"**
Nee. Het is een programma dat woorden voorspelt. Het klinkt soms levend, omdat het heeft geleerd van teksten die door mensen zijn geschreven.

**"Waarom heet hij Fietje?"**
Dat heeft de maker zo bedacht; het past bij een klein Nederlands model. (Zeker weten waarom? Dat moet je de maker vragen.)

## Misvattingen

| Misvatting | Hoe het zit |
|---|---|
| "AI zoekt het antwoord op internet op." | Een taalmodel zelf zoekt niets op. Sommige chatbots hebben wél een extra zoekfunctie, maar het model is iets anders dan die zoekfunctie. |
| "AI is één groot brein ergens in de wolken." | Het zijn computerprogramma's die in gewone (wel enorme) gebouwen draaien. "De cloud" is gewoon de computer van iemand anders. |
| "Kleine modellen zijn nep of speelgoed." | Ze werken precies hetzelfde als grote; ze zijn alleen minder goed. |
| "Lokaal is altijd beter." | Lokaal is goed voor privacy en werkt offline, maar de kwaliteit is lager. Het is een afweging. |

## Als het misgaat

- **Geest reageert niet in de demo:** draait `start.bat`? De eerste vraag laadt het model en kan 10–30 seconden duren. Vul de stilte: "Hij moet nog wakker worden."
- **Netwerk uit en de docent-server draait:** zie de achtergrond hierboven. Test dit vooraf.
- **Raar of ongepast antwoord tijdens de demo:** rustig benoemen, er een grapje of leermoment van maken (hoofdstuk 01). Kies vooraf een veilige demovraag die je hebt getest.
- **Kinderen willen meteen beginnen:** houd de opening echt kort; 15 minuten is genoeg.
- **Discussie over de stelling barst los:** "Bewaar die gedachte! Aan het eind praten we erover."

## Verder lezen

- Ollama, documentatie en broncode: <https://github.com/ollama/ollama>. Geraadpleegd: november 2026.
- Bram Vanroy, *Fietje: An open, efficient LLM for Dutch*, arXiv (2024). Geraadpleegd: november 2026.
- Microsoft Research, aankondiging van *Phi-2: The surprising power of small language models* (december 2023). Geraadpleegd: november 2026.
- Fietje-modelpagina op Hugging Face (`BramVanroy/fietje-2-chat`). Geraadpleegd: november 2026.
