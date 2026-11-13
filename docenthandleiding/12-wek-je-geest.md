# 2. Wek je geest

## Kernboodschap

Met een verborgen instructie, de systeemprompt, bepaal je wie de geest is. Elke chatbot heeft er een.

## In het kort

| | |
|---|---|
| **Tijd** | 25 minuten |
| **Vorm** | 💻 programmeren in tweetallen |
| **Materialen** | Laptop met de geest, `level1_wek_je_geest.py` |
| **Leerdoel** | Het kind kan met een systeemprompt bepalen wie de geest is |

## Achtergrond voor de docent

**Rollen in een gesprek.** Een chatmodel krijgt een gesprek niet als één lange tekst, maar als een lijst berichten met elk een **rol**:

| Rol | Wie schrijft het? | Voorbeeld |
|---|---|---|
| `system` | De maker van de app (hier: het kind) | "Je bent een piraat die alleen in piratentaal praat." |
| `user` | De gebruiker | "Wat is je lievelingseten?" |
| `assistant` | Het model zelf (eerdere antwoorden) | "Arrr, scheepsbeschuit natuurlijk!" |

Ollama zet deze lijst om naar één tekst met speciale markeringen (het *chat template*) die het model tijdens zijn training heeft leren herkennen. Voor het model is het dus nog steeds één tekst waarin het het vervolg voorspelt; de rollen helpen het om te weten wie wat zei en welk deel "de opdracht" is.

**De systeemprompt.** Het `system`-bericht staat bovenaan het gesprek. Het model is er tijdens de training aan gewend geraakt dat dit bericht bepaalt hoe het zich gedraagt: toon, rol, regels, wat wel en niet mag. Alle grote chatbots hebben zo'n verborgen instructie, vaak honderden tot duizenden woorden lang, met regels over toon, veiligheid, opmaak en wat het model over zichzelf mag zeggen. Gebruikers zien die normaal niet. Bedrijven die een chatbot op hun website zetten (klantenservice, een "AI-vriendje" in een app) doen precies wat de kinderen nu doen: een bestaand model nemen en er een systeemprompt omheen schrijven.

**Een wens, geen wet.** De systeemprompt *stuurt* het model, maar dwingt niets af. Het model kiest woorden die waarschijnlijk zijn gegeven de hele tekst, en de systeemprompt is daar een (belangrijk) deel van. Bij een klein model als Fietje zie je dat het:

- de rol vaak goed oppakt, maar soms vergeet of half uitvoert;
- de rol op een onverwachte manier invult. Getest: met de geest-prompt antwoordde Fietje op "Wie ben jij?" met *"Ik ben een geest. Ik ben eeuwen geleden gestorven en nu geef ik je korte antwoorden."* Het model koppelt "geest" kennelijk aan "spook", niet aan de geest uit de lamp;
- lange of tegenstrijdige instructies slecht volgt. Korte, duidelijke zinnen werken beter;
- soms terugvalt in "assistent-taal" ("Als AI-taalmodel…") of overschakelt naar Engels.

Grote modellen volgen systeemprompts veel beter, maar ook daar is het geen garantie. Dat wordt belangrijk in onderdeel 5 (het geheime woord).

**Geheugen.** In `level1_wek_je_geest.py` wordt elk antwoord weer aan de berichtenlijst toegevoegd. Daardoor "onthoudt" de geest het gesprek: bij elke nieuwe vraag krijgt het model het **hele** gesprek opnieuw te lezen. Het model zelf onthoudt niets tussen twee vragen. Fietje kan maximaal 2048 tokens tegelijk lezen (het *contextvenster*); bij lange gesprekken gooit Ollama ongemerkt de oudste berichten weg. De systeemprompt blijft daarbij staan, maar de geest kan dan wel vergeten wat er eerder in het gesprek is gezegd. Noem het hier hoogstens als kinderen vragen waarom de geest na een lang gesprek "uit zijn rol valt".

**Waarom dit level belangrijk is.** Kinderen ontdekken dat het "karakter" van een chatbot geen eigenschap van de AI is, maar een **keuze van de maker**. Dat helpt later bij vragen als "waarom is die AI altijd zo vriendelijk?" en "wie bepaalt wat een chatbot wel en niet zegt?".

**Wet en wens: programmeren versus een model.** In dit level werken kinderen met twee heel verschillende dingen tegelijk:

| | Python (programmeren) | Het taalmodel |
|---|---|---|
| Hoe streng? | **Wet**: doet precies wat er staat, niets meer en niets minder | **Wens**: doet ongeveer wat je vraagt |
| Foutjes | Eén vergeten aanhalingsteken en het programma start niet (`SyntaxError`) | Tikfouten en rommelige zinnen begrijpt hij meestal toch |
| Herhalen | Zelfde code en invoer → altijd dezelfde uitkomst | Zelfde vraag → vaak een ander antwoord (onderdeel 3) |
| Als het misgaat | Een duidelijke foutmelding met regelnummer | Geen foutmelding: gewoon een raar of fout antwoord |

In `SYSTEEM = "Je bent een piraat."` zie je de grens letterlijk: de naam, het `=` en de aanhalingstekens zijn Python (wet); de zin ertussen is voor het model (wens). Wie een eigen model draait, speelt dus op de grens tussen wetten en wensen. Dat komt terug bij het geheime woord (onderdeel 5): wat écht moet kloppen, regel je met een wet (een Python-filter), niet alleen met een wens in de systeemprompt.

## Uitleg voor kinderen

- "De geest in de fles doet wat er op het **briefje in de fles** staat. Dat briefje is de **systeemprompt**: een geheime instructie die de gebruiker niet ziet."
- "Elke chatbot heeft zo'n briefje. Bij ChatGPT staat er bijvoorbeeld in dat hij behulpzaam en beleefd moet zijn. Bij de chatbot van een webwinkel staat erin dat hij over de producten moet praten. Wie het briefje schrijft, bepaalt wie de chatbot is."
- "Vandaag schrijven júllie het briefje."
- Na afloop: "Doet de geest altijd precies wat er op het briefje staat? Nee! Het briefje is een sterke **wens**, geen **wet**."
- "Python is juist wél een **wet**: vergeet je één aanhalingsteken, dan weigert hij. De geest snapt je tikfouten wel, maar doet niet altijd wat je vraagt. Jullie programma is Python dat een geest aanroept: jullie werken op de grens tussen wetten en wensen."

## Verloop

| Minuut | Docent | Kinderen |
|---|---|---|
| 0–4 | Leg uit: systeemprompt = briefje in de fles. Laat op de beamer `level1_wek_je_geest.py` zien: waar staat `SYSTEEM`, waar staat `NAAM`, hoe start je (F5), hoe stop je ('stop'). Laat zien dat de tekst tussen aanhalingstekens moet blijven. | Kijken |
| 4–6 | Thonny openen, bestand openen, één keer starten met de standaardgeest. | Starten, eerste vraag stellen |
| 6–18 | **TODO 1 en 2**: eigen systeemprompt en naam. Ideeën op het bord: piraat, chagrijnige oma, robot uit het jaar 3000, superheld, kat die alleen over vis wil praten, sportverslaggever. Moedig aan: "Vertel ook hoe hij praat en wat hij nooit zou zeggen." | Programmeren, testen, aanpassen |
| 18–21 | **Bij de buren kijken**: elk tweetal stelt een vraag aan de geest van het buurtweetal. Raad wie het is, en vraag de makers: "Deed hij wat jullie wilden?" | Rondkijken, praten |
| 21–25 | Twee of drie tweetallen laten hun geest op de beamer zien (of laat kinderen bij elkaar kijken). Gesprek: "Deed je geest altijd wat je zei? Wie bepaalt bij ChatGPT wat er op het briefje staat?" Sluit af met **wet en wens** (dia): "Wie kreeg een rode foutmelding? Python is een wet, de geest een wens." | Laten zien, praten |

**Plus** (onderaan het bestand): de geest begint zelf met een begroeting, nog vóór de eerste vraag.
**Expert**: de geest moet altijd rijmen of altijd eindigen met een vraag. Lukt dat altijd? Hier ontdekken kinderen zelf dat de systeemprompt een wens is en geen wet.

Snelle kinderen die klaar zijn met plus en expert: laat ze dezelfde vraag stellen aan twee totaal verschillende geesten en de antwoorden vergelijken.

## Vragen die kinderen stellen

**"Waarom doet mijn piraat niet de hele tijd piratentaal?"**
De systeemprompt is een sterke wens, geen wet. Een klein model als Fietje vergeet het soms. Probeer korte, duidelijke zinnen, of zet de belangrijkste regel twee keer neer.

**"Is mijn piraat nu een andere AI dan die van mijn buurman?"**
Nee, het is precies hetzelfde model met een ander briefje. Net als een acteur die een andere rol speelt.

**"Heeft ChatGPT ook zo'n briefje?"**
Ja. Bedrijven schrijven lange systeemprompts met regels. Je ziet ze normaal niet.

**"Kan ik de geest laten zeggen dat hij echt leeft?"**
Ja, als je dat in de systeemprompt zet, zal hij het zeggen. Dat maakt het niet waar: hij speelt alleen de rol die jij hebt geschreven. Daarom moet je ook bij echte chatbots niet alles geloven wat ze over zichzelf zeggen.

**"Hij zei dat hij eeuwen geleden gestorven is! Is hij een spook?"**
Hij heeft het woord "geest" gekoppeld aan spoken, omdat dat in veel teksten zo is. Hij verzint er een verhaal bij dat past. Schrijf in je prompt "een geest uit een toverlamp, zoals in Aladdin" en kijk wat er verandert.

**"Waarom antwoordt hij ineens in het Engels?"**
Fietje is gebouwd op een Engels model en heeft daarna Nederlands geleerd. Soms schiet hij terug. Zet in de systeemprompt "Je antwoordt altijd in het Nederlands."

**"Onthoudt hij mij de volgende keer?"**
Nee. Als je het programma stopt, is het gesprek weg. Binnen één gesprek "onthoudt" hij het, omdat de code het hele gesprek steeds opnieuw meestuurt.

**"Kan ik hem gemeen maken?"**
Een chagrijnige of brutale geest mag, een gemene geest die scheldt of beledigt niet. Houd het grappig.

## Misvattingen

| Misvatting | Hoe het zit |
|---|---|
| "De AI heeft een eigen karakter." | Het karakter komt grotendeels van de systeemprompt en van keuzes van de maker tijdens het trainen. |
| "Wat in de systeemprompt staat, gebeurt altijd." | Het is een sterke sturing, geen garantie. |
| "De geest onthoudt alles wat ik ooit tegen hem zei." | Alleen wat in de berichtenlijst van dít gesprek staat, en ook dat maar tot een maximum. |
| "Als de AI zegt dat hij blij is, is hij blij." | Hij schrijft woorden die passen bij de rol en het gesprek. Hij heeft geen gevoelens. |

## Als het misgaat

- **`SyntaxError` na het aanpassen:** meestal een vergeten aanhalingsteken, of een `'` in de tekst (bijvoorbeeld "'s avonds") binnen een tekst met dezelfde aanhalingstekens. Laat de foutregel zien en wijs naar de aanhalingstekens.
- **"Ik kan de geest niet bereiken":** `start.bat` opnieuw starten, of bij de docent-server het adres in `fles.py` controleren.
- **Geest doet niets met de nieuwe prompt:** is het bestand opgeslagen en opnieuw gestart (F5)? Het oude gesprek met de oude prompt loopt anders door.
- **Geest blijft maar doorpraten of herhaalt zichzelf:** kleine modellen raken soms in een lus. Bij onze tests schreef Fietje ooit meer dan 13.000 tokens op één vraag. Daarom kapt `fles.py` elk antwoord af na `MAX_TOKENS` (standaard 300). Wil een kind langere verhalen, dan mag het dat getal verhogen. Mooi gespreksmoment: "De geest weet niet zelf wanneer hij klaar is; hij voorspelt alleen een 'einde'-token, en soms komt dat niet."
- **Ongepaste persona** (bijvoorbeeld "een geest die scheldt"): bijsturen naar een grappige variant, zie hoofdstuk 01.
- **Kinderen blijven eindeloos kletsen met hun eigen geest:** geef op minuut 18 een duidelijk signaal voor het bij de buren kijken. Juist door andere geesten te zien, merken ze wat een systeemprompt doet.
- **Erg trage laptop:** laat de systeemprompt om korte antwoorden vragen ("antwoord in maximaal twee zinnen").

## Verder lezen

- Ollama API-documentatie, *Generate a chat completion* (berichten met rollen): <https://docs.ollama.com/api/chat>. Geraadpleegd: november 2026.
- Bram Vanroy, *Fietje: An open, efficient LLM for Dutch*, arXiv (2024). Over de chatversie van Fietje. Geraadpleegd: november 2026.
- OpenAI, *Model Spec* (openbaar document over hoe hun modellen met instructies van ontwikkelaars en gebruikers omgaan). Geraadpleegd: november 2026.
