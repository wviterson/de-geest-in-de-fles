# MODULE E – Zelf een taalmodel trainen
#
# Fietje heeft miljarden teksten gelezen. Maar wat is dat eigenlijk, "trainen"?
# Hier train je zelf een mini-geest. Hij leest het bestand versjes.txt en leert
# daarvan welke letter er meestal na welke letters komt. Daarna schrijft hij zelf
# nieuwe tekst, letter voor letter, met een dobbelsteen (net als in level 2).
#
# DEEL 1 – De tel-geest: trainen is hier gewoon TELLEN.
#   CONTEXT = hoeveel letters de geest terugkijkt voordat hij gooit.
#   Context 1: hij kijkt alleen naar de vorige letter. Context 6: naar de vorige zes.
# DEEL 2 – Het netje: een piepklein neuraal netwerk dat leert door te OEFENEN.
#   Je ziet de "fout" steeds kleiner worden.
#
# Je hebt hier geen Ollama en geen Fietje nodig. Alles gebeurt in dit bestand.

import math
import os
import random
import time

# Een vaste seed: dan krijg je dezelfde "worpen" als in de docenthandleiding.
random.seed(42)    # TODO 5 (als laatste): zet een # voor deze regel. Wat verandert er?

BESTAND = "versjes.txt"    # TODO 4: train de geest op je eigen tekst (zie hieronder)
# TODO 4: Maak in Thonny een nieuw bestand en typ er een tekst in die je ZELF hebt
#         geschreven: een rap, een verhaal, gedichtjes. Hoe meer, hoe beter!
#         Sla het op als mijn_tekst.txt in deze map en zet BESTAND = "mijn_tekst.txt".
#         Geen songteksten van internet en geen berichten van anderen.
CONTEXTEN = [1, 2, 3, 4, 6]
TEMPERATUUR = 1.0          # TODO 3: probeer 0, 0.5 en 2
LENGTE = 150               # hoeveel letters de geest schrijft
STUKJE = "de "             # TODO 2: welk stukje wil je onder de loep nemen?


def lees_tekst(bestandsnaam):
    """Leest de trainingstekst uit de map waar dit programma staat."""
    map_van_dit_bestand = os.path.dirname(os.path.abspath(__file__))
    pad = os.path.join(map_van_dit_bestand, bestandsnaam)
    with open(pad, encoding="utf-8-sig") as bestand:
        return bestand.read().lower().strip() + "\n"


# ---------------------------------------------------------------------------
# DEEL 1 – De tel-geest
# ---------------------------------------------------------------------------

def train(tekst, context):
    """TRAINEN = TELLEN. Na welke letters komt welke letter, en hoe vaak?
    De geest onthoudt ook de kortere stukjes, voor als hij een stukje niet kent."""
    model = {}
    for lengte in range(context + 1):
        for plek in range(lengte, len(tekst)):
            stukje = tekst[plek - lengte:plek]
            volgende = tekst[plek]
            telling = model.setdefault(stukje, {})
            telling[volgende] = telling.get(volgende, 0) + 1
    return model


def kies(telling, temperatuur):
    """De dobbelsteen: een letter die vaak voorkwam, heeft meer kans."""
    letters = list(telling)
    if temperatuur == 0:
        return max(letters, key=telling.get)    # altijd de grootste kans
    gewichten = [telling[letter] ** (1 / temperatuur) for letter in letters]
    return random.choices(letters, weights=gewichten)[0]


def schrijf(model, context, lengte, temperatuur):
    """De geest schrijft letter voor letter. Hij kijkt steeds naar de laatste
    letters. Kent hij dat stukje niet, dan kijkt hij naar een korter stukje."""
    tekst = "\n"
    for _ in range(lengte):
        for terug in range(context, -1, -1):
            stukje = tekst[max(0, len(tekst) - terug):]
            if stukje in model:
                break
        tekst += kies(model[stukje], temperatuur)
    return tekst[1:]


def langste_kopie(nieuw, tekst):
    """De papegaai-meter: wat is het langste stuk dat LETTERLIJK in de versjes staat?"""
    langste = ""
    for start in range(len(nieuw)):
        eind = start + len(langste) + 1
        while eind <= len(nieuw) and nieuw[start:eind] in tekst:
            langste = nieuw[start:eind]
            eind += 1
    return langste


def echte_woorden(nieuw, tekst):
    """Hoeveel procent van de woorden komt ook echt in de versjes voor?"""
    bekend = set(tekst.split())
    woorden = nieuw.split()
    if not woorden:
        return 0
    return round(100 * sum(woord in bekend for woord in woorden) / len(woorden))


def toon_dobbelsteen(model, stukje):
    """Laat zien wat de geest geleerd heeft over één stukje tekst."""
    telling = model.get(stukje)
    if telling is None:
        print(f"De geest heeft '{stukje}' nooit gezien.")
        return
    totaal = sum(telling.values())
    print(f"Na '{stukje}' kwam in de versjes {totaal} keer een letter. De dobbelsteen:")
    for letter, aantal in sorted(telling.items(), key=lambda paar: -paar[1])[:8]:
        procent = 100 * aantal / totaal
        print(f"  {letter!r:6} {procent:5.1f}%  " + "#" * round(procent / 2))


tekst = lees_tekst(BESTAND)
if len(tekst) < 20:
    raise SystemExit(f"In {BESTAND} staat (bijna) niets. Zet er meer tekst in en sla het op!")
print(f"De geest leest {BESTAND}: {len(tekst)} letters, {len(tekst.split())} woorden.")

# TODO 1: Schrijf eerst je voorspelling op: hoe ziet de tekst eruit bij context 1?
#         En bij context 6? Druk dan op F5.
for context in CONTEXTEN:
    begin = time.time()
    model = train(tekst, context)
    getallen = sum(len(telling) for telling in model.values())
    nieuw = schrijf(model, context, LENGTE, TEMPERATUUR)
    kopie = langste_kopie(nieuw, tekst)
    print(f"\n===== Context {context}: de geest kijkt {context} letter(s) terug =====")
    print(f"Getraind in {time.time() - begin:.2f} seconden. Getallen in zijn geheugen: {getallen}")
    print(nieuw)
    print(f"--> Echte woorden: {echte_woorden(nieuw, tekst)}%")
    print(f"--> Papegaai-meter: {len(kopie)} letters op een rij letterlijk overgeschreven:")
    print("    " + repr(kopie))

print("\n===== Wat heeft de geest geleerd? =====")
toon_dobbelsteen(train(tekst, len(STUKJE)), STUKJE)


# ---------------------------------------------------------------------------
# DEEL 2 – Het netje: leren door te oefenen
# ---------------------------------------------------------------------------
# Echte taalmodellen tellen niet. Ze hebben "draaiknopjes" (gewichten) en
# OEFENEN: raden, kijken hoe fout het was, alle knopjes een heel klein beetje
# bijdraaien, en opnieuw. Eén keer alle versjes oefenen heet een EPOCH.
# Dit netje kijkt maar 1 letter terug. Het begint met willekeurige knopjes.

EPOCHS = 100          # EXPERT: wat gebeurt er met 10 of 300 epochs?
LEERSNELHEID = 50     # EXPERT: probeer 1, 10 en 1000
LATEN_ZIEN = [0, 1, 2, 5, 10, 20, 50, 100, 200, 300]


def softmax(scores, temperatuur=1.0):
    """Maakt van scores kansen die samen 1 (= 100%) zijn."""
    hoogste = max(scores)
    machten = [math.exp((score - hoogste) / temperatuur) for score in scores]
    totaal = sum(machten)
    return [macht / totaal for macht in machten]


def schrijf_netje(knopjes, letters, lengte, temperatuur):
    tekst = "\n"
    for _ in range(lengte):
        kansen = softmax(knopjes[letters.index(tekst[-1])], temperatuur)
        tekst += random.choices(letters, weights=kansen)[0]
    return tekst[1:]


def train_netje(tekst):
    letters = sorted(set(tekst))
    nummer = {letter: plek for plek, letter in enumerate(letters)}
    paren = [(nummer[a], nummer[b]) for a, b in zip(tekst, tekst[1:])]
    n = len(letters)
    knopjes = [[random.gauss(0, 0.1) for _ in range(n)] for _ in range(n)]
    print(f"Het netje heeft {n} x {n} = {n * n} draaiknopjes.")

    begin = time.time()
    for epoch in range(EPOCHS + 1):
        # 1. Raden: bij elke letter de kansen op de volgende letter uitrekenen.
        kansen = [softmax(rij) for rij in knopjes]
        fout = 0.0
        bijdraaien = [[0.0] * n for _ in range(n)]
        for a, b in paren:
            # 2. Hoe fout was het? Weinig kans op de goede letter = grote fout.
            kans = max(kansen[a][b], 1e-100)    # nooit precies 0, anders kan log() niet
            fout -= math.log(kans)
            # 3. Onthoud welke kant je de knopjes op moet draaien.
            for k in range(n):
                bijdraaien[a][k] += kansen[a][k]
            bijdraaien[a][b] -= 1
        fout /= len(paren)

        if epoch in LATEN_ZIEN:
            voorbeeld = schrijf_netje(knopjes, letters, 60, 1.0).replace("\n", " / ")
            print(f"Epoch {epoch:3} | fout {fout:.2f} | twijfelt tussen ± {math.exp(fout):4.1f} letters"
                  f" | {voorbeeld}")

        # 4. Alle knopjes een klein beetje de goede kant op draaien.
        for a in range(n):
            for k in range(n):
                knopjes[a][k] -= LEERSNELHEID * bijdraaien[a][k] / len(paren)

    print(f"Klaar met oefenen in {time.time() - begin:.1f} seconden.")
    return knopjes, letters


def fout_van_telgeest(tekst):
    """Ter vergelijking: de fout van de tel-geest met context 1."""
    model = train(tekst, 1)
    fout = 0.0
    for a, b in zip(tekst, tekst[1:]):
        fout -= math.log(model[a][b] / sum(model[a].values()))
    return fout / (len(tekst) - 1)


antwoord = input("\nDruk op Enter voor DEEL 2: het netje gaat oefenen (of typ stop): ")
if antwoord.strip().lower() != "stop":
    print("\n===== Het netje oefent =====")
    knopjes, letters = train_netje(tekst)
    print(f"Ter vergelijking: de tel-geest met context 1 heeft fout {fout_van_telgeest(tekst):.2f}.")
    print("\nHet netje schrijft (temperatuur 1):")
    print(schrijf_netje(knopjes, letters, LENGTE, 1.0))

# ---------------------------------------------------------------------------
# PLUS – nieuwe namen verzinnen
#   Maak in Thonny een nieuw bestand, typ er 30 namen in (één per regel), en
#   sla het op als namen.txt in deze map. Bijvoorbeeld namen voor huisdieren,
#   draken of planeten die jullie zelf verzinnen, of plaatsnamen uit de atlas.
#   (Geen namen van klasgenoten!) Zet BESTAND = "namen.txt" en LENGTE = 200.
#   Welke context geeft de leukste NIEUWE namen? Wanneer gaat hij papegaaien?
#   Let op: "Echte woorden" betekent nu: namen die al in jouw lijst stonden.
#
# PLUS 2 – de papegaai
#   Zet CONTEXTEN = [8, 10]. Wat zegt de papegaai-meter nu?
#   Stel: iemand traint een geest op jouw verhalen en hij schrijft ze letterlijk
#   over. Van wie is die tekst dan? Schrijf je mening op.
#
# EXPERT – het netje
#   1. Verander LEERSNELHEID (1, 10, 1000). Wat gaat er mis als hij te klein
#      of te groot is?
#   2. Hoe laag kan de fout van het netje worden? Vergelijk met de tel-geest.
#      Waarom wordt het netje nooit zo goed als de tel-geest met context 4?
#   3. Moeilijk: laat het netje 2 letters terugkijken. Tip: geef elk PAAR
#      letters een eigen rij knopjes. Hoeveel knopjes heb je dan nodig?
