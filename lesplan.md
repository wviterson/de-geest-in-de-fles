# De Geest in de Fles – lesplan

**Doelgroep:** 11–14 jaar · **Groep:** tot ± 30 kinderen, in tweetallen achter één laptop
**Opzet:** een **kernmiddag** (± 3,5 uur) die op zichzelf staat, plus **uitbreidingsmodules** voor een lessenreeks.
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

## Uitbreidingsmodules (lessenreeks)

Elke module duurt 50–90 minuten en bouwt voort op de kernmiddag. Ze zijn los te kiezen. ★ = sterk aanbevolen.

| Module | Onderwerp | Vorm | Kernvraag | Code |
|---|---|---|---|---|
| **A** ★ | **Geheugen en context** | 💻 | Waarom vergeet de geest wat je eerder zei? (berichtenlijst, contextvenster van 2048 tokens) | `module_a_geheugen.py` |
| **B** | **Tokens** | 🎤💻 | Hoe "leest" een AI? Tokenizer-demo van KU Leuven; waarom tellen moeilijk is | `module_b_tokens.py` |
| **C** ★ | **Betekenis als getallen** | 💻 | Hoe weet een computer dat *fiets* en *bromfiets* op elkaar lijken? Warm-koud-spel met embeddings | `module_c_warm_koud.py` |
| **D** ★ | **De geest leert lezen (RAG)** | 💻 | Hoe geef je een AI kennis die hij niet heeft? De geest beantwoordt vragen uit een eigen tekstbestand | `module_d_kennis.py` |
| **E** ★ | **Zelf een taalmodel trainen** | 💻 | Wat is "trainen" eigenlijk? Een mini-model in pure Python leert van versjes: van wartaal naar woorden | `module_e_trainen.py` |
| **F** | **AI die tekent** | 🎤💻 | Hoe maakt AI plaatjes? Diffusie: van ruis naar beeld (OpenVINO GenAI met LCM Dreamshaper; optionele installatie) | `module_f_tekenen.py` |
| **G** ★ | **AI als vriend?** | 💬🔌 | Waarom geeft AI je altijd gelijk? Vleierij, AI-vriendjes (zoals Snapchat My AI), wanneer je met een mens moet praten | – |
| **H** | **Echt of nep?** | 💬💻 | Deepfakes, labelplicht (EU AI Act), en wat er gebeurt als AI van AI-teksten leert | – |
| **I** | **De prijs van AI** | 💬🔌 | Energie en water, de mensen die data labelen, geld en de AI-race, grondstoffen. Klopt "lokaal is groener"? | – |
| **J** | **Van wie is jouw data?** | 💬 | Privacy, gebruiksvoorwaarden, digitale soevereiniteit, open source tegenover open weights | – |
| **K** | **Is je geest goed?** | 💻 | Hoe test je een AI? Een eigen toetsset met vragen en goede antwoorden; benchmarks | `module_k_testen.py` |
| **L** | **En nu verder: AI die dingen doet** | 🎤💬 | Tools, MCP en agents, als theorie met een demo door de docent (ander model dan Fietje). AGI: de koffietest. Wie is er aansprakelijk? | – |

**Voorbeeld van een reeks van 6 lessen:**

1. Kernonderdelen 0–3
2. Kernonderdelen 4–6
3. Module A en C
4. Module D en G
5. Module E
6. Module I of J als debat, en presentatie van "mijn geest"

---

## Hoe de materialen hierop aansluiten

| Materiaal | Opbouw |
|---|---|
| **Opdracht (kinderen)** | Map `code\` met één bestand per level of module: startcode met `TODO`s, onderaan *plus* en *expert*. Waar het nuttig is, schrijven kinderen hun antwoord of voorspelling op een papiertje. |
| **Docenthandleiding** | Eén hoofdstuk per onderdeel of module, steeds met dezelfde opbouw: kernboodschap · achtergrond voor de docent · uitleg voor kinderen (met beeldspraak) · demo/verloop · te verwachten vragen met antwoorden · misvattingen · veiligheid · bronnen met datum. Bijlagen: installatie, problemen oplossen, begrippenlijst. |
| **Presentatie** | Eén blok dia's per onderdeel of module, met weinig tekst en vaste beeldspraak (de geest, de dobbelsteen, gips tegenover exoskelet). Bij voorkeur in Markdown (Marp), zodat dia's en handleiding uit één bron komen. |

## Open punten

- [x] Module F (tekenen): optioneel apart installatiescript `installatie\installeer-tekenen.ps1`; de docent kiest per laptop.
- [x] Module L: demomodel `ministral-3:3b` (Mistral AI, Frankrijk) op de docentlaptop. In onze test riep het 5 van de 5 tools goed aan en sprak het goed Nederlands. Het is bewust een Europees model; zie module J over digitale soevereiniteit.
