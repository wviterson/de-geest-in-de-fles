# De Geest in de Fles – installatie

Alles wat nodig is komt in **één map**: Ollama (de motor), Thonny (Python-editor, met Python erin) en de taalmodellen. Er wordt niets in Windows zelf geïnstalleerd en je hebt geen beheerdersrechten nodig. Weghalen gaat met één dubbelklik.

Er zijn drie routes:

| Route | Voor wie | Internet nodig |
|---|---|---|
| **A. Installatiescript** | Laptop met goed internet | Ja, ± 3,7 GB downloaden |
| **B. USB-stick** | Klas met slecht of geen netwerk | Alleen bij het vullen van de stick |
| **C. Handmatig** | Wie wil snappen wat er gebeurt | Ja |

En voor zwakke laptops of Chromebooks: **D. Docent-server** (zie onder).

---

## Wat heb je nodig?

- Windows 10 (versie 1809 of nieuwer) of Windows 11, 64-bits. Intel/AMD of ARM (Snapdragon).
- Minimaal **8 GB werkgeheugen** (met 6 GB werkt het krap; daaronder: gebruik de docent-server).
- **± 9 GB vrije ruimte** tijdens installeren, daarna ± 5,5 GB (of ± 3,5 GB met `-AlleenCpu`).
- Een **USB-stick van minimaal 8 GB**, geformatteerd als **exFAT of NTFS** (niet FAT32: daar passen geen bestanden groter dan 4 GB op).

**Controleer eerst** of een laptop geschikt is: dubbelklik `controleer.bat`. Dat meldt problemen zoals te weinig geheugen, een al geïnstalleerde Ollama, of door de school geblokkeerde scripts.

---

## Route A – Installatiescript

1. Kopieer de map `installatie` naar de laptop.
2. Dubbelklik **`installeer.bat`**.
3. Wacht. Afhankelijk van het netwerk duurt dit 5 tot 30 minuten.
4. Aan het eind opent de map `%USERPROFILE%\GeestInDeFles` (bijv. `C:\Users\Sanne\GeestInDeFles`).
5. Dubbelklik **`start.bat`**. Thonny opent met `level1_wek_je_geest.py`; druk op **F5**.

Is het downloaden onderbroken? Start `installeer.bat` gewoon opnieuw: het gaat verder waar het was.

**Opties** (in PowerShell, of achter `installeer.bat`):

| Optie | Betekenis |
|---|---|
| `-Doel E:\GeestInDeFles` | Andere installatiemap |
| `-AlleenCpu` | Laat de NVIDIA-onderdelen weg (scheelt 2 GB). Schoollaptops hebben vrijwel nooit een NVIDIA-kaart. |
| `-Modellen a,b` | Andere modellen (standaard: `bramvanroy/fietje-2b-chat:Q5_K_M`, `bge-m3`) |
| `-Stemmen a,b` | Andere Piper-stemmen (standaard: `nl_NL-pim-medium`, `nl_NL-ronnie-medium`, `nl_BE-nathalie-medium`) |
| `-BewaarDownloads` | Bewaar de gedownloade zip-bestanden in `_downloads` |
| `-Ja` | Geen vragen stellen (voor herhaald gebruik) |

---

## Route B – USB-stick

**Eenmalig, thuis of op een plek met goed internet:**

```
installeer.bat -Doel E:\GeestInDeFles -AlleenCpu
```

(vervang `E:` door de letter van je stick). De stick bevat daarna alles; er is geen internet meer nodig.

**In de klas, per laptop – kies één van twee:**

- **`kopieer-naar-laptop.bat`** (aanbevolen): kopieert alles naar `%USERPROFILE%\GeestInDeFles` en start de geest. Daarna is de stick weer vrij voor de volgende laptop. Kopiëren duurt 1 tot 5 minuten, afhankelijk van de stick.
- **`start.bat` direct vanaf de stick**: werkt zonder kopiëren, maar het laden van het model is trager en de stick moet de hele les in de laptop blijven. De code van het kind staat dan óp de stick.

> Tip: met 4 à 5 sticks is een klas van 30 snel klaar. Een USB 3-stick is merkbaar sneller dan USB 2.

---

## Route C – Handmatig, stap voor stap

Dit is precies wat `installeer.ps1` doet. Leuk voor wie het wil begrijpen (en het script is daarna ook goed te lezen).

1. **Map maken**: bijvoorbeeld `C:\Users\<naam>\GeestInDeFles`.
2. **Ollama** (de motor die taalmodellen draait):
   download `ollama-windows-amd64.zip` (of `-arm64.zip` voor Snapdragon) van
   <https://github.com/ollama/ollama/releases/tag/v0.40.16> en pak uit in de submap `ollama`.
   Optioneel: verwijder `ollama\lib\ollama\cuda_v12` en `cuda_v13` als je geen NVIDIA-kaart hebt.
3. **Thonny** (de Python-editor, met Python erin):
   download `thonny-5.0.1-windows-portable-x64.zip` van
   <https://github.com/thonny/thonny/releases/tag/v5.0.1> en pak uit in de submap `thonny`.
4. **Python-pakketten**: open een opdrachtprompt in je map en typ:
   ```
   thonny\python.exe -m pip install requests pyttsx3 piper-tts
   ```
   (Of in Thonny via het menu *Tools → Manage packages*.)
5. **Stemmen**: maak de submap `stemmen` en download daarin van
   <https://huggingface.co/rhasspy/piper-voices/tree/main/nl> per stem het `.onnx`- én het `.onnx.json`-bestand,
   bijvoorbeeld `nl_NL/pim/medium/nl_NL-pim-medium.onnx` en `nl_NL-pim-medium.onnx.json`.
6. **Ollama starten**: open een opdrachtprompt (`cmd`) in je map en typ:
   ```
   set OLLAMA_MODELS=%CD%\modellen
   ollama\ollama.exe serve
   ```
   Laat dit venster open. `OLLAMA_MODELS` zorgt dat de modellen in jouw map komen in plaats van ergens in Windows.
6. **Modellen ophalen**: open een tweede opdrachtprompt in dezelfde map:
   ```
   ollama\ollama.exe pull bramvanroy/fietje-2b-chat:Q5_K_M
   ollama\ollama.exe pull bge-m3
   ```
7. **Uitproberen**: `ollama\ollama.exe run bramvanroy/fietje-2b-chat:Q5_K_M` en stel een vraag. Of kopieer `installatie\sjabloon\code` naar de submap `code`, open `level1_wek_je_geest.py` in Thonny en druk op F5.

Opruimen: sluit beide vensters, verwijder de map en verwijder `%USERPROFILE%\.ollama` (als die er vóór stap 6 nog niet was).

---

## D. Docent-server (voor zwakke laptops)

Eén goede laptop draait het model, de rest van de klas gebruikt die via het netwerk.

1. Op de docentlaptop: dubbelklik **`docent-server.bat`**. Het venster toont het adres, bijvoorbeeld `SERVER = "http://<ip-docentlaptop>:11434"`.
2. Krijg je een melding van Windows Firewall? Kies *Toegang toestaan*. Dit vereist soms beheerdersrechten; regel dat vóór de les.
3. Laat de kinderen in `code\fles.py` de regel `SERVER = ...` vervangen door dat adres.

De server verwerkt 4 vragen tegelijk; de rest wacht even. Dat is meteen een mooi gesprek over *lokaal versus cloud*: zo werkt een datacenter ook, alleen veel groter.

Let op: veel schoolnetwerken (vooral gastnetwerken) laten laptops niet met elkaar praten. Test dit vooraf, of neem een eigen wifi-router mee.

---

## Wat staat er in de map?

| | |
|---|---|
| `start.bat` | Start Ollama (onzichtbaar op de achtergrond) en opent Thonny met `level1_wek_je_geest.py` |
| `stop.bat` | Stopt Ollama (Thonny blijft open) |
| `status.bat` | Laat versies, status en geïnstalleerde modellen zien |
| `docent-server.bat` | Start Ollama als server voor de hele klas |
| `kopieer-naar-laptop.bat` | Kopieert alles van de USB-stick naar de laptop |
| `controleer.bat` | Controleert of de laptop geschikt is |
| `opruimen.bat` | Verwijdert alles weer |
| `code\` | De Python-code van het kind |
| `modellen\` | De taalmodellen (± 3 GB) |
| `stemmen\` | De Piper-stemmen voor tekst-naar-spraak |
| `ollama\`, `thonny\` | De programma's |
| `beheer\` | De scripts achter de `.bat`-bestanden |
| `versies.txt` | Welke versies er zijn geïnstalleerd |

---

## Opruimen

Dubbelklik **`opruimen.bat`** en typ `JA`. Dit:

- stopt Ollama en Thonny;
- verwijdert de hele map, **inclusief de code in `code\`** (laat kinderen hun code eerst mailen of op een stick zetten als ze die willen houden);
- verwijdert `%USERPROFILE%\.ollama`, maar **alleen als De Geest in de Fles die map zelf heeft aangemaakt**. Ollama maakt daar altijd een paar kleine bestanden aan; stond er al een Ollama op de laptop, dan blijft die map onaangeroerd.

Daarna is de laptop weer zoals hij was. Er staat niets in het register, het Startmenu of Program Files.

---

## Stemmen (tekst-naar-spraak)

De geest praat met **Piper**: een klein neuraal netwerk dat tekst omzet in spraak, helemaal offline. De stemmen (± 60 MB per stuk) staan in de map `stemmen` en gaan dus gewoon mee op de USB-stick. Er hoeft niets in Windows geïnstalleerd te worden.

Standaard geïnstalleerd: `nl_NL-pim-medium`, `nl_NL-ronnie-medium` en `nl_BE-nathalie-medium` (Vlaams). Beluisteren: open `code\stem.py` in Thonny en druk op F5.

In eigen code:

```python
from stem import zeg
zeg("Hallo, ik ben de geest!")
zeg("Goeiedag!", stem="nl_BE-nathalie-medium", snelheid=1.2)
```

Andere stemmen: zie <https://rhasspy.github.io/piper-samples/> en installeer met bijvoorbeeld `-Stemmen nl_NL-alex-medium,nl_BE-rdh-medium`.

Werkt Piper onverhoopt niet, dan valt `zeg()` terug op de Windows-stem via `pyttsx3`. Die spreekt op de meeste laptops alleen Engels, wat kinderen overigens vaak hilarisch vinden.

---

## Problemen oplossen

| Probleem | Oplossing |
|---|---|
| *"Poort 11434 is al in gebruik"* | Er draait al een andere Ollama. Klik rechtsonder bij de klok op het Ollama-icoon → *Quit*, en start opnieuw. |
| *"Scripts zijn door een beheerder geblokkeerd"* | De school blokkeert PowerShell-scripts. Vraag de ICT-beheerder, gebruik route C, of gebruik de docent-server. |
| Virusscanner blokkeert `ollama.exe` | Gebeurt soms bij programma's vanaf een USB-stick. Gebruik `kopieer-naar-laptop.bat`, of vraag de beheerder om een uitzondering. |
| *"Ik kan de geest niet bereiken"* in Thonny | `start.bat` is niet gestart of Ollama is gestopt. Dubbelklik `start.bat` opnieuw. |
| Antwoorden zijn erg traag | Normaal op oudere laptops: de eerste vraag laadt het model (± 10–30 s). Sluit browsers en andere programma's. Te traag? Gebruik de docent-server. |
| Download blijft hangen | Druk Ctrl+C, start `installeer.bat` opnieuw; het gaat verder waar het was. Achter een proxy: stel `HTTPS_PROXY` in. |
| Iets anders | Kijk in `logs\ollama.log` in de installatiemap. |

---

## Voor de beheerder van dit lesmateriaal

- De versies staan bovenaan `installeer.ps1` (`$OllamaVersie`, `$ThonnyVersie`, `$PythonPakketten`) en in de standaardwaarde van `-Modellen`. Pas ze bewust aan en test daarna opnieuw; nieuwe versies kunnen zich anders gedragen.
- `installatie\sjabloon\` wordt 1-op-1 naar de installatiemap gekopieerd. Bestanden in `code\` worden nooit overschreven als ze al bestaan.
- Getest op: Windows 11 (build 26200), Windows PowerShell 5.1, Ollama 0.40.16, Thonny 5.0.1 (Python 3.14), piper-tts 1.8.0, november 2026.
