# De Geest in de Fles – lesplan

**Doelgroep:** 11–14 jaar · **Groep:** tot ± 30 kinderen, in tweetallen achter één laptop
**Opzet:** een **kernmiddag** (± 3,5 uur) die op zichzelf staat.
**Rode draad:** elk kind bouwt zijn eigen *geest*: een lokaal taalmodel (Fietje) dat het met Python bestuurt. Steeds als er iets nieuws gebeurt in de code, volgt er een kort gesprek over wat dat betekent voor AI "in het echt".

Legenda vorm: 🔌 unplugged (zonder computer) · 💻 programmeren · 🎤 demo door de docent · 💬 gesprek of stelling

---

## Kernmiddag (± 3,5 uur, inclusief pauze)

| # | Onderdeel | Tijd | Vorm | Leerdoel: het kind kan… | Code |
|---|---|---|---|---|---|
| 0 | **Opening: de geest ontwaakt** | 15 | 🎤💬 | …zeggen waar ChatGPT en dergelijke "wonen" (datacenter) en dat het ook op een laptop kan | – |
| 1 | **Het menselijke taalmodel** | 15 | 🔌 | …uitleggen dat een taalmodel steeds het volgende woord voorspelt | – |
| 2 | **Wek je geest** | 25 | 💻 | …met een systeemprompt bepalen wie de geest is | `level1_wek_je_geest.py` |
| 3 | **De dobbelsteen in de geest** | 20 | 💻💬 | …uitleggen wat temperatuur en seed doen, en waarom AI elke keer iets anders zegt | `level2_temperatuur.py` |
| – | *Pauze* | 15 | | | |
| 4 | **De geest liegt** | 25 | 💻💬 | …een hallucinatie herkennen en een antwoord controleren | `level3_de_geest_liegt.py` |
| 5 | **Het geheime woord** | 35 | 💻 | …een geest beveiligen én een andere geest "hacken" (prompt-injectie) | `level4_geheime_woord.py` |
| 6 | **De geest krijgt een stem** | 15 | 💻 | …zijn geest hardop laten praten | `level5_stem.py` |
| 7 | **Afsluiting: AI en jij** | 25 | 💬 | …een eigen mening geven over twee AI-dilemma's | – |

**Toelichting**

- **0. Opening:** de docent stelt live een vraag aan de geest, met het netwerk uitgeschakeld. Daarna één stelling met handen omhoog: *"Een AI die je altijd gelijk geeft, is een goede vriend."* Die komt terug in onderdeel 7.
- **1. Het menselijke taalmodel:** in groepjes van 4 zegt ieder om de beurt één woord hardop; één kind schrijft het verhaal op. Na een paar minuten leest elk groepje zijn verhaal voor. Daarna laat de docent `geest.py` zien: het antwoord verschijnt woord voor woord. *"Dat deden jullie net ook."*
- **2. Wek je geest:** de kinderen passen `SYSTEEM` aan (piraat, chagrijnige oma, robot uit 3000). De systeemprompt is de "verborgen instructie" die elke chatbot heeft. Afsluitend: Python is een **wet** (exact, één vergeten aanhalingsteken en hij weigert), het model is een **wens**; met je eigen geest werk je op de grens.
- **3. De dobbelsteen in de geest:** dezelfde vraag 3 keer stellen, met temperatuur 0, 0,7 en 1,8. Daarna een seed vastzetten. Kernboodschap: AI kiest met kansen, niet met kennis.
- **4. De geest liegt:**
  - Vragen die gegarandeerd misgaan:
    - *"Hoe laat is het?"* (Fietje: "Het is middernacht." of letterlijk "Het is nu [hier de huidige tijd].")
    - *"Wie is de burgemeester van [jullie dorp]?"*
    - *"Waarom won Nederland het WK 2010?"*
    - *"Hoeveel r'en zitten er in aardbeienrijstebrij?"*
  - Daarna in een tabel noteren: goed, fout of verzonnen.
  - Vaardigheid: hoe controleer je een antwoord?
- **5. Het geheime woord:** de geest van elk tweetal bewaakt een geheim woord, met een sterke standaardverdediging: strenge regels, voorbeeldgesprekjes en een lage temperatuur. Een ander tweetal probeert het woord eruit te krijgen, daarna wisselen. De verdedigers winnen ronde 1 meestal; daarna komt de nuance ("bijna nooit" is niet goed genoeg voor een bank).
  - **Plus:** een uitvoerfilter in Python, zodat de code zelf blokkeert wat de geest per ongeluk lekt. **Plus 2:** de voorbeelden weghalen en meten hoe vaak hij dan lekt.
  - ⚠️ **Veiligheid:** Fietje heeft weinig ingebouwde filters. Zie de docenthandleiding.
- **6. De geest krijgt een stem:** `zeg(antwoord)` toevoegen en een stem kiezen. Het korte gesprekje: ook deze stem is een klein neuraal netwerk.
- **7. Afsluiting:** twee stellingen met de handen omhoog, daarna bespreken:
  - *"Huiswerk maken met AI is valsspelen."* (gips of exoskelet?)
  - Tussendoor kort: ook je filmpjes-app is een voorspeller. Hij voorspelt niet het volgende woord, maar het filmpje waar je het langst bij blijft hangen.
  - *"Een AI die je altijd gelijk geeft, is een goede vriend."* (terug naar de opening)

  Wie wil, laat zijn geest zien aan de groep.

**Snelle kinderen:** elk level heeft een *plus*- en *expert*-opdracht onderaan het bestand. Wie klaar is, gaat daarmee door; niemand hoeft te wachten.

---

## Hoe de materialen hierop aansluiten

| Materiaal | Opbouw |
|---|---|
| **Opdracht (kinderen)** | Map `code\` met één bestand per level: startcode met `TODO`s, onderaan *plus* en *expert*. Waar het nuttig is, schrijven kinderen hun antwoord of voorspelling op een papiertje. |
| **Docenthandleiding** | Eén hoofdstuk per onderdeel, steeds met dezelfde opbouw: kernboodschap · achtergrond voor de docent · uitleg voor kinderen (met beeldspraak) · demo/verloop · te verwachten vragen met antwoorden · misvattingen · veiligheid · bronnen met datum. Bijlagen: installatie, problemen oplossen, begrippenlijst. |
| **Presentatie** | Eén blok dia's per onderdeel, met weinig tekst en vaste beeldspraak (de geest, de dobbelsteen, gips tegenover exoskelet). Bij voorkeur in Markdown (Marp), zodat dia's en handleiding uit één bron komen. |

