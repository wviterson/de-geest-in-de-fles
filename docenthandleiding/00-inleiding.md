# De Geest in de Fles – docenthandleiding: inleiding

## Waar gaat deze cursus over?

In *De Geest in de Fles* bouwt elk kind zijn eigen **geest**: een taalmodel dat op de eigen laptop draait, zonder internet, en dat het kind met Python bestuurt. Het model heet **Fietje** (`bramvanroy/fietje-2b-chat`), een klein Nederlandstalig taalmodel. De motor die het laat draaien heet **Ollama**; de kinderen programmeren in **Thonny**.

Het doel is niet dat kinderen "leren werken met ChatGPT". Het doel is dat ze **snappen wat er onder de motorkap gebeurt**, zodat ze AI later kritisch, veilig en slim kunnen gebruiken. Elke keer als er iets nieuws gebeurt in de code, volgt een kort gesprek over wat dat betekent voor AI "in het echt".

Na de kernmiddag kan een kind onder meer:

- uitleggen dat een taalmodel steeds het volgende woord voorspelt;
- met een systeemprompt bepalen hoe een chatbot zich gedraagt;
- uitleggen waarom AI elke keer iets anders zegt (kansen, temperatuur, seed);
- een verzonnen antwoord herkennen en controleren;
- uitleggen waarom chatbots te "hacken" zijn met slimme vragen (prompt-injectie);
- een onderbouwde mening geven over AI bij huiswerk en AI als "vriend".

## Doelgroep

- **Kinderen van 11–14 jaar** (groep 8 tot en met klas 2), tot ongeveer 30 per keer, **in tweetallen** achter één laptop.
- Programmeerervaring is **niet** nodig. Kinderen die al kunnen programmeren, gaan door met de *plus*- en *expert*-opdrachten.
- **Docenten en begeleiders** hoeven geen AI-expert te zijn. Deze handleiding geeft per onderdeel de achtergrond die je nodig hebt. Basiskennis van computers is genoeg; Python-kennis is handig voor wie kinderen helpt met code.

## Hoe gebruik je deze handleiding?

1. Lees deze inleiding en hoofdstuk **01 – Veiligheid** helemaal. Dat laatste is verplichte kost voor **iedere** begeleider.
2. Lees per onderdeel minstens de **Kernboodschap**, het **Verloop** en **Als het misgaat**. De **Achtergrond voor de docent** is er voor wie zich wil voorbereiden op lastige vragen.
3. Probeer elk codebestand zelf één keer uit vóór de les. Fietje gedraagt zich niet altijd hetzelfde; het helpt als je zelf hebt gezien wat er kan gebeuren.
4. De installatie staat apart beschreven in `installatie\INSTALLATIE.md`.

### Vaste opbouw van elk hoofdstuk

| Kop | Wat staat er? |
|---|---|
| **Kernboodschap** | Het ene zinnetje dat kinderen mee naar huis moeten nemen |
| **In het kort** | Tijd, vorm, materialen, leerdoel |
| **Achtergrond voor de docent** | Hoe het echt zit, zonder versimpeling |
| **Uitleg voor kinderen** | Hoe je het uitlegt op hun niveau, met vaste beeldspraak |
| **Verloop** | Stap voor stap, met minuten |
| **Vragen die kinderen stellen** | Realistische vragen met korte, goede antwoorden |
| **Misvattingen** | Wat kinderen (en volwassenen) vaak denken, en hoe het zit |
| **Als het misgaat** | Praktische en didactische tips |
| **Verder lezen** | Betrouwbare bronnen, met datum van raadplegen |

Legenda vorm: 🔌 unplugged (zonder computer) · 💻 programmeren · 🎤 demo door de docent · 💬 gesprek of stelling

### Vaste beeldspraak

Gebruik deze beelden steeds opnieuw; herhaling helpt.

| Beeld | Betekent |
|---|---|
| **De geest in de fles** | Het taalmodel: machtig, maar het doet letterlijk wat er staat en weet niets van de wereld buiten de fles |
| **Autocomplete met superkrachten** | Het voorspellen van het volgende woord |
| **De dobbelsteen** | Het model kiest met kansen, niet met kennis |
| **De verborgen instructie** | De systeemprompt |
| **Gips of exoskelet** | AI die je lui maakt tegenover AI die je sterker maakt |

## Overzicht

### Kernmiddag (± 3,5 uur, inclusief pauze)

| # | Onderdeel | Tijd | Vorm | Code | Hoofdstuk |
|---|---|---|---|---|---|
| 0 | Opening: de geest ontwaakt | 15 | 🎤💬 | – | `10-opening.md` |
| 1 | Het menselijke taalmodel | 15 | 🔌 | – | `11-menselijk-taalmodel.md` |
| 2 | Wek je geest | 25 | 💻 | `level1_wek_je_geest.py` | `12-wek-je-geest.md` |
| 3 | De dobbelsteen in de geest | 20 | 💻💬 | `level2_temperatuur.py` | `13-dobbelsteen.md` |
| – | *Pauze* | 15 | | | |
| 4 | De geest liegt | 25 | 💻💬 | `level3_de_geest_liegt.py` | `14-de-geest-liegt.md` |
| 5 | Het geheime woord | 35 | 💻 | `level4_geheime_woord.py` | `15-geheime-woord.md` |
| 6 | De geest krijgt een stem | 15 | 💻 | `level5_stem.py` | `16-stem.md` |
| 7 | Afsluiting: AI en jij | 25 | 💬 | – | `17-afsluiting.md` |

Alle levels gebruiken het hulpbestand `fles.py`, dat de vraag naar Ollama stuurt (de functie `vraag(berichten, temperatuur=..., seed=...)`). Kinderen hoeven `fles.py` niet te begrijpen of aan te passen.

**Snelle kinderen:** elk level heeft onderaan een *plus*- en een *expert*-opdracht. Wie klaar is, gaat daarmee door; niemand hoeft te wachten. Trage tweetallen mogen plus en expert gerust overslaan.

Bijlagen: `90-problemen-oplossen.md` en `91-begrippenlijst.md`.

## Voorbereiding: checklist

**Twee weken of langer vooraf**

- [ ] Laptops geregeld (eigen laptops, schoollaptops of uitleenset). Minimaal 8 GB werkgeheugen; daaronder de docent-server gebruiken.
- [ ] Elke laptop gecontroleerd met **`controleer.bat`**. Let vooral op: te weinig geheugen, geblokkeerde scripts, een al geïnstalleerde Ollama.
- [ ] Bij schoollaptops: met de ICT-beheerder overlegd over geblokkeerde scripts, virusscanner en firewall.
- [ ] USB-sticks gevuld (route B in `INSTALLATIE.md`): 4 à 5 sticks voor een klas van 30, exFAT of NTFS, liefst USB 3.
- [ ] De **docent-server** getest op de echte locatie en het echte netwerk: kunnen laptops elkaar bereiken? Gastnetwerken blokkeren dat vaak. Zo nodig een eigen wifi-router meenemen.

**De week ervoor**

- [ ] Alle levels zelf doorlopen op een cursuslaptop, inclusief plus en expert.
- [ ] De vragen van level 3 zelf aan Fietje gesteld, zodat je weet wat voor antwoorden er ongeveer komen.
- [ ] Opgezocht wie de burgemeester is van de plaats waar je lesgeeft (voor level 3).
- [ ] Kladpapier en pennen voor elk tweetal (voor voorspellingen en antwoorden).
- [ ] Stellingen voor onderdeel 0 en 7 klaargezet (dia of groot papier).
- [ ] Voor onderdeel 1: papier en pennen voor groepjes van 4.
- [ ] **Begeleiders gebriefd over veiligheid** (hoofdstuk 01): wat te doen als de geest iets ongepasts zegt, de regels voor het geheime-woordspel, privacy.
- [ ] Ouders/school geïnformeerd dat er met een lokaal taalmodel wordt gewerkt en dat er geen gegevens naar internet gaan.

**Op de dag zelf**

- [ ] Installatie op alle laptops (`kopieer-naar-laptop.bat`), daarna `start.bat` en één testvraag per laptop. De eerste vraag laadt het model en duurt langer.
- [ ] Docentlaptop met beamer en geluid getest (onderdeel 0 en 6).
- [ ] Bedacht hoe je in de openingsdemo laat zien dat het netwerk uit staat (zie hoofdstuk 10).
- [ ] Koptelefoons of oortjes voor onderdeel 6 (anders praten 15 laptops door elkaar).

## Rollen

| Rol | Taken |
|---|---|
| **Docent** | Leidt de plenaire delen (opening, uitleg, gesprekken, afsluiting), bewaakt de tijd, beslist over het stoppen van een oefening. |
| **Begeleiders** | Lopen rond tijdens het programmeren, helpen met code en installatieproblemen, letten op wat de geesten zeggen, stellen doorvraag-vragen ("Waarom denk je dat hij dat zegt?"). |
| **Technisch aanspreekpunt** (mag een begeleider zijn) | Docent-server, USB-sticks, laptops die niet willen. |

**Verhouding:** reken op ongeveer **één begeleider per 8 kinderen** (dus 3–4 begeleiders bij 30 kinderen, naast de docent). Bij jonge groepen of veel installatieproblemen liever meer.

Tip: geef elke begeleider een vast "eiland" van ongeveer 4 tweetallen. Dan weet ieder kind bij wie het terechtkan en ziet de begeleider wat zijn kinderen doen.

## AI in één A4 – voor de docent

**Wat is een taalmodel (LLM)?**
Een *large language model* is een computerprogramma dat één ding doet: **het volgende stukje tekst voorspellen**. Je geeft het een tekst, het rekent uit welke stukjes (*tokens*: woorden of delen van woorden) waarschijnlijk volgen, kiest er één, plakt dat erachter en herhaalt dat. Een antwoord van een chatbot is dus een lange reeks van zulke voorspellingen. Je kunt het zien als **autocomplete op je telefoon, maar dan veel groter en veel beter**.

**Hoe leert het dat?**
Door **training**: het model krijgt enorme hoeveelheden tekst te zien (websites, boeken, Wikipedia, code) en oefent ontelbaar vaak "wat komt hierna?". Na elke fout worden de interne getallen een heel klein beetje bijgesteld. Daarna volgt meestal een tweede fase waarin het model leert om als behulpzame assistent te antwoorden, vaak met beoordelingen door mensen. In die fase leren de grote modellen ook om bepaalde vragen te weigeren. Bij Fietje is die tweede fase beperkt (zie hoofdstuk 01).

**Wat zijn parameters?**
De interne getallen die tijdens het trainen worden bijgesteld. Fietje heeft er ongeveer **2,7 miljard** (het is gebaseerd op Microsoft Phi-2). De grootste commerciële modellen hebben er naar schatting honderden miljarden of meer; de bedrijven maken het exacte aantal meestal niet bekend. Meer parameters betekent grofweg: meer ruimte voor patronen, vaak betere antwoorden, maar ook meer rekenkracht en geheugen nodig. De versie van Fietje die wij gebruiken is "gecomprimeerd" (*kwantisatie*: de getallen zijn afgerond, variant Q5_K_M) tot ongeveer 2 GB, zodat hij op een gewone laptop past.

**Eén model, drie namen.** Op Hugging Face heet het model `BramVanroy/fietje-2-chat` (de familie heet *Fietje 2*); in Ollama, en dus in onze code, heet de gecomprimeerde versie `bramvanroy/fietje-2b-chat:Q5_K_M`. Het is hetzelfde model.

**Waarom klinkt het zo zeker?**
Het model is getraind om tekst te maken die **klinkt** als een goed antwoord. Het heeft geen betrouwbaar ingebouwd besef van "dit weet ik niet zeker". Een verzonnen antwoord rolt er net zo vloeiend uit als een juist antwoord. Dat heet *hallucineren* (hoofdstuk 14).

**Weet het model wat het zegt?**
Daar zijn wetenschappers het niet over eens; hoeveel "begrip" er in zulke modellen zit, is een open vraag. Wat wél vaststaat: het model heeft geen gevoelens, geen eigen wil, geen geheugen tussen gesprekken (tenzij een programma dat toevoegt) en geen toegang tot de echte wereld, behalve via de tekst die je het geeft.

**Lokaal of in de cloud?**

| | Cloud (ChatGPT, Gemini, Copilot, Claude …) | Lokaal (onze geest) |
|---|---|---|
| Waar draait het? | In een datacenter van een bedrijf | Op je eigen laptop |
| Internet nodig? | Ja | Nee |
| Waar gaan je vragen heen? | Naar de servers van het bedrijf | Nergens heen |
| Grootte van het model | Heel groot | Klein (Fietje: ± 2 GB) |
| Kwaliteit | Meestal veel beter | Wisselend, maakt meer fouten |
| Extra's | Zoeken op internet, hulpmiddelen, filters | Alleen wat je zelf programmeert |

Het grote voordeel van lokaal voor deze cursus: **de kinderen zien het kale model**, zonder de laag van filters en hulpmiddelen die grote chatbots eromheen bouwen. Daardoor worden de zwakke plekken zichtbaar, en dat is precies wat we willen laten zien. Het nadeel: ook de filters ontbreken (zie hoofdstuk 01).

**Wat kost het aan energie?**
Schattingen lopen uiteen en zijn onzeker. Recente schattingen voor één gewone tekstvraag aan een grote chatbot liggen in de orde van **0,3 wattuur**: grofweg een ledlamp die een paar minuten brandt. Het vaak gehoorde "zo veel als een lamp die een uur brandt" is voor een gewone vraag overdreven. Maar: lange antwoorden, "redeneermodellen", plaatjes en video kosten veel meer, en het **trainen** van grote modellen plus de enorme aantallen gebruikers maken het totaal wél groot.

## Verder lezen

- 3Blue1Brown, videoserie *Neural networks*, met de aflevering *But what is a GPT?* (2024). Visueel en helder, Engelstalig. Geraadpleegd: november 2026.
- *Elements of AI*, gratis online cursus van de Universiteit van Helsinki, ook in het Nederlands. Geraadpleegd: november 2026.
- Ollama, documentatie en broncode: <https://github.com/ollama/ollama>. Geraadpleegd: november 2026.
- Bram Vanroy, *Fietje: An open, efficient LLM for Dutch*, arXiv (2024). Geraadpleegd: november 2026.
- Epoch AI, *How much energy does ChatGPT use?* (2025), voor de schatting van ± 0,3 Wh per vraag. Geraadpleegd: november 2026.
