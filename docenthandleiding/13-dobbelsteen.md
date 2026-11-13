# 3. De dobbelsteen in de geest

## Kernboodschap

AI kiest elk woord met kansen, niet met kennis: de temperatuur bepaalt hoe wild de dobbelsteen is, en de seed bepaalt hoe hij begint.

## In het kort

| | |
|---|---|
| **Tijd** | 20 minuten |
| **Vorm** | 💻💬 programmeren in tweetallen, daarna kort gesprek |
| **Materialen** | Laptop met de geest, `level2_temperatuur.py`, papier en pen voor de voorspelling; eventueel een echte dobbelsteen en een zak met gekleurde knikkers of briefjes voor de uitleg |
| **Leerdoel** | Het kind kan uitleggen wat temperatuur en seed doen, en waarom AI elke keer iets anders zegt |

## Achtergrond voor de docent

**Een kansverdeling over tokens.** Bij elke stap rekent het model voor **elk** token in zijn woordenlijst (bij Fietje ruim 50.000 tokens) een score uit. Die scores (*logits*) worden omgezet in kansen die samen 100% zijn. Die omzetting heet **softmax**. Voorbeeld na "De hoofdstad van Frankrijk is":

| Token | Kans (verzonnen voorbeeld) |
|---|---|
| Parijs | 92% |
| de | 4% |
| een | 1% |
| Lyon | 0,5% |
| … (50.000 andere) | samen de rest |

Daarna wordt er **getrokken** (*sampling*): het model "gooit een dobbelsteen" waarbij Parijs 92 van de 100 kanten heeft. Meestal komt Parijs eruit, soms iets anders. En omdat elk volgend woord afhangt van de eerdere, kan één ongebruikelijke keuze het hele vervolg een andere kant op sturen.

**Temperatuur.** Vóór de softmax worden de scores gedeeld door de temperatuur.

- **Temperatuur laag (richting 0):** de verschillen tussen de scores worden groter, de kans op het favoriete token gaat richting 100%. Bij **temperatuur 0** kiest Ollama gewoon steeds het token met de hoogste kans (*greedy*). Uitkomst: voorspelbaar, vaak wat saai, soms in herhaling vallend.
- **Temperatuur 1:** de kansen zoals het model ze heeft geleerd.
- **Temperatuur hoog (1,5–2):** de verschillen worden kleiner, onwaarschijnlijke tokens krijgen relatief veel meer kans. Uitkomst: verrassend, "creatief", en al snel onzin, rare woordcombinaties of overschakelen naar andere talen.

Intuïtie: temperatuur maakt de dobbelsteen **eerlijker** (hoog) of **meer verzwaard** (laag). De kennis van het model verandert niet; alleen hoe gewaagd het kiest.

**Top-k en top-p.** Naast temperatuur zijn er nog twee knoppen die voorkomen dat er compleet absurde tokens worden gekozen:

- **top-k**: trek alleen uit de *k* meest waarschijnlijke tokens (bijvoorbeeld de beste 40);
- **top-p** (*nucleus sampling*): trek alleen uit de kleinste groep tokens die samen p (bijvoorbeeld 90%) van de kans hebben.

Ollama gebruikt hiervoor standaardwaarden (volgens de documentatie onder meer top-k 40 en top-p 0,9; een model kan eigen waarden meekrijgen). De kinderen veranderen in dit level alleen de temperatuur. Omdat top-k en top-p de allergekste opties al wegfilteren, wordt temperatuur 1,8 vaak "creatief-rommelig" in plaats van totale wartaal, maar het verschil met 0 is goed zichtbaar.

**Seed.** Een computer kan niet echt dobbelen. Hij gebruikt een **pseudo-willekeurige getallengenerator**: een rekenregel die een reeks getallen maakt die willekeurig *lijken*. Die reeks begint bij een startgetal: de **seed**. Zelfde seed + zelfde model + zelfde vraag + zelfde instellingen = dezelfde "worpen" = hetzelfde antwoord. Zonder vaste seed kiest Ollama zelf een willekeurige startwaarde, dus krijg je elke keer iets anders. Kanttekening: op een andere computer, met een andere versie van Ollama of met andere hardware kan het antwoord bij dezelfde seed toch afwijken, door kleine afrondingsverschillen in de berekeningen. Op één laptop is het in de praktijk goed herhaalbaar.

**Waarom doet determinisme ertoe?**

- **Wetenschap en testen:** wie een AI wil testen (module K), wil dat een proef herhaalbaar is.
- **Fouten zoeken:** een programmeur wil een gek antwoord kunnen nadoen.
- **Games:** Minecraft gebruikt ook een seed om dezelfde wereld opnieuw te maken. Dat kennen veel kinderen; gebruik het!
- **Betrouwbaarheid:** in situaties waar je steeds hetzelfde antwoord wilt (een samenvatting, een classificatie) kiest men een lage temperatuur.

**Wat is "de goede" temperatuur?** Die bestaat niet. Voor feitenvragen en code liever laag; voor verhalen en brainstormen wat hoger. Grote chatbots kiezen een instelling voor je; bij veel ontwikkelaarsomgevingen kun je hem zelf instellen. In `fles.py` staat de standaard op 0,7.

**Let op de valkuil.** Temperatuur 0 maakt het antwoord **voorspelbaar**, niet **waar**. Als het meest waarschijnlijke antwoord fout is, krijg je bij temperatuur 0 steeds hetzelfde foute antwoord. Dat zie je in onderdeel 4: level 3 gebruikt temperatuur 0.

## Uitleg voor kinderen

- "Bij elk woord heeft de geest een **dobbelsteen** met heel veel kanten. Woorden die goed passen staan op veel kanten, woorden die raar zijn op weinig kanten. Na 'De hoofdstad van Frankrijk is…' staat 'Parijs' op bijna alle kanten."
- Met de zak knikkers (optioneel): 9 rode (Parijs), 1 blauwe (Lyon). "Meestal pak je rood. Maar soms…"
- "De **temperatuur** bepaalt hoe wild de dobbelsteen is. Bij 0 pakt hij altijd het woord met de meeste kanten: saai maar voorspelbaar. Bij 1,8 krijgen rare woorden ineens veel meer kans: creatief… of onzin."
- "Een computer kan niet echt gooien. Hij rekent een rij 'toevalsgetallen' uit die begint bij een startgetal: de **seed**. Net als in Minecraft: zelfde seed, zelfde wereld."
- Kernzin: **"AI kiest met kansen, niet met kennis."**

## Verloop

| Minuut | Docent | Kinderen |
|---|---|---|
| 0–3 | Uitleg dobbelsteen (eventueel met knikkers). Koppel terug naar onderdeel 1: "Wie had in het spel de rol 'temperatuur 0'?" | Luisteren, reageren |
| 3–5 | **TODO 1**: eerst voorspellen en opschrijven: wat gebeurt er bij temperatuur 0 als je drie keer hetzelfde vraagt? | Voorspelling opschrijven |
| 5–10 | Programma draaien: drie pogingen bij 0, 0,7 en 1,8 met de ijsjes-vraag. Kloppen de voorspellingen? | Draaien, vergelijken |
| 10–14 | **TODO 2**: een vraag met één goed antwoord ("Wat is de hoofdstad van Frankrijk?"). Bij welke temperatuur gaat het mis? Snelle tweetallen: plus (omslagtemperatuur zoeken) en expert (seed). | Programmeren |
| 14–20 | **Gesprek**: "Waarom zegt ChatGPT elke keer iets anders? Wanneer wil je een lage temperatuur, wanneer een hoge? Wie heeft de seed geprobeerd? Wat gebeurde er?" Laat de seed eventueel op de beamer zien. Sluit af met de kernzin. | Praten |

**Plus**: de "omslagtemperatuur" zoeken: vanaf welke temperatuur wordt het onzin?
**Expert**: `seed=42` meegeven. Drie keer hetzelfde antwoord? En met `seed=43`? Waarom handig voor wetenschappers en gamemakers?

## Vragen die kinderen stellen

**"Waarom zegt hij elke keer wat anders?"**
Bij elk woord gooit hij een soort dobbelsteen. Een andere worp bij één woord kan het hele antwoord een andere kant op sturen.

**"Bij temperatuur 0 zegt hij steeds hetzelfde. Is dat dan het goede antwoord?"**
Nee, het is het *meest waarschijnlijke* antwoord. Dat kan nog steeds fout zijn. Voorspelbaar is niet hetzelfde als waar.

**"Wat is de beste temperatuur?"**
Hangt af van wat je wilt. Voor sommen en feiten laag, voor verhalen en namen bedenken wat hoger.

**"Waarom heet het temperatuur? Wordt de laptop warm?"**
Nee, het is een leenwoord uit de natuurkunde: bij hoge temperatuur bewegen deeltjes wilder. Hier gaan de keuzes wilder.

**"Kun je hoger dan 2?"**
Technisch wel, maar dan wordt het vrijwel altijd wartaal. Probeer het gerust als expert.

**"Is de seed hetzelfde als in Minecraft?"**
Ja, hetzelfde idee: een startgetal voor een rij "toevalsgetallen". Zelfde seed, zelfde wereld, of hier: zelfde antwoord.

**"Is het dan wel echt toeval?"**
Niet helemaal: het is uitgerekend toeval (*pseudo-toeval*). Als je de seed weet, kun je het nadoen. Voor de geest maakt dat niet uit; het werkt alsof het toeval is.

**"Weet hij dan eigenlijk wel iets?"**
Hij heeft heel veel patronen geleerd, en die bepalen welke woorden veel kanten op de dobbelsteen krijgen. Maar hij controleert niet of iets klopt.

## Misvattingen

| Misvatting | Hoe het zit |
|---|---|
| "Een AI die elke keer iets anders zegt, is kapot." | Dat is zo ontworpen: er wordt getrokken uit kansen. |
| "Temperatuur 0 = waarheid." | Temperatuur 0 = voorspelbaar. Het meest waarschijnlijke antwoord kan fout zijn. |
| "Hoge temperatuur maakt de AI slimmer of creatiever." | Het maakt de keuzes gewaagder. Soms levert dat iets origineels op, vaak gewoon onzin. |
| "Met dezelfde seed krijg je overal ter wereld hetzelfde antwoord." | Alleen bij hetzelfde model, dezelfde instellingen en in de praktijk dezelfde software en hardware. |

## Als het misgaat

- **Bij temperatuur 0 toch verschillende antwoorden:** kan bij sommige combinaties van hardware en software. Gebruik het als bonusvraag: "Hoe zou dat komen?" (Kleine afrondingsverschillen.)
- **Bij 0,7 drie keer bijna hetzelfde antwoord:** de ijsjes-vraag heeft soms een heel waarschijnlijk antwoord. Laat kinderen een opener vraag kiezen ("Verzin een gedicht over een kat").
- **Bij 1,8 rare, Engelse of ongepaste woorden:** te verwachten. Benoem het, laat het venster sluiten als het ongepast is (hoofdstuk 01).
- **Het duurt lang** (9 vragen achter elkaar): laat de systeemprompt korte antwoorden vragen, of haal bij trage laptops één temperatuur weg. Bij de docent-server: dit level geeft veel tegelijke vragen; laat tweetallen om de beurt draaien.
- **Kinderen snappen "seed" niet:** de Minecraft-vergelijking werkt bijna altijd. Anders: "het is de bladzijde in een boek vol dobbelsteenworpen waar je begint te lezen."

## Verder lezen

- Ollama, documentatie over modelparameters (`temperature`, `seed`, `top_k`, `top_p`) in de Modelfile- en API-documentatie: <https://github.com/ollama/ollama/tree/main/docs>. Geraadpleegd: november 2026.
- Holtzman e.a., *The Curious Case of Neural Text Degeneration*, ICLR 2020 (het artikel dat top-p/nucleus sampling introduceerde). Geraadpleegd: november 2026.
- 3Blue1Brown, *But what is a GPT?* (2024): legt softmax en temperatuur visueel uit. Geraadpleegd: november 2026.
