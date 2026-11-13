# MODULE B – Tokens: hoe "leest" de geest?
#
# Jij leest letters en woorden. De geest niet! Voordat hij iets leest, wordt
# elke tekst in STUKJES geknipt: TOKENS. Een kort woord is vaak één stukje,
# een lang woord wordt in meerdere stukjes geknipt. Elk stukje heeft een
# nummer, en de geest rekent alleen met die nummers.
#
# Dat knippen doet de TOKENIZER (de knipmachine). Die van onze geest is
# vooral op ENGELSE tekst gemaakt. Wat betekent dat voor Nederlands?
#
# Druk op F5. Het programma doet twee proeven:
#   Proef 1: de knipmachine – hoe worden woorden geknipt?
#   Proef 2: de teltest   – kan de geest letters tellen?

from fles import vraag_een_keer
import fles
import re

import requests

# TODO 1: Zet je eigen naam en drie eigen woorden in deze lijst.
#         Voorspel eerst: in hoeveel stukjes wordt elk woord geknipt?
WOORDEN = [
    "kat",
    "aardbeienrijstebrij",
    "strawberry",
    "ziekenhuisparkeerplaats",
    "Fatima",
    "🍓",
]

# TODO 2: Dezelfde zin in het Nederlands en in het Engels.
#         Welke kost meer stukjes? Bedenk zelf nog een paar zinnen.
ZINNEN = [
    "De kat zit op de mat.",
    "The cat sits on the mat.",
    "Ik vind pannenkoeken met stroop heerlijk.",
    "I love pancakes with syrup.",
]

# TODO 3: Welke woorden zijn moeilijk om letters in te tellen?
#         Zet er een paar eigen woorden bij (letter, woord).
TELTEST = [
    ("r", "aardbeienrijstebrij"),
    ("a", "banaan"),
    ("p", "appelflappen"),
    ("e", "ziekenhuisparkeerplaats"),
]
POGINGEN = 5       # elke telvraag 5 keer: de geest gooit met een dobbelsteen
fles.MAX_TOKENS = 30   # een getal is kort; zo hoeft niemand lang te wachten


# =========================================================================
# DE MACHINEKAMER – dit stuk hoef je niet te snappen.
# Hier haalt Python de woordenlijst van de geest op (ruim 50.000 stukjes)
# en knipt tekst op precies dezelfde manier als de geest dat doet.
# Scroll door naar "HIER BEGIN JIJ".
# =========================================================================

def haal_woordenlijst():
    try:
        r = requests.post(fles.SERVER + "/api/show",
                          json={"model": fles.MODEL, "verbose": True}, timeout=60)
    except requests.ConnectionError:
        raise SystemExit("Ik kan de geest niet bereiken. Is start.bat (of de docent-server) gestart?")
    info = r.json()["model_info"]
    plakregels = {}
    for nummer, regel in enumerate(info["tokenizer.ggml.merges"]):
        plakregels[tuple(regel.split(" "))] = nummer
    return info["tokenizer.ggml.tokens"], plakregels


def byte_letters():
    # De knipmachine werkt met bytes (de 0'en en 1'en achter elke letter).
    # Elke byte krijgt hier een eigen leesbaar teken.
    gewoon = list(range(33, 127)) + list(range(161, 173)) + list(range(174, 256))
    tekens = gewoon[:]
    extra = 0
    for b in range(256):
        if b not in gewoon:
            gewoon.append(b)
            tekens.append(256 + extra)
            extra += 1
    return dict(zip(gewoon, [chr(t) for t in tekens]))


TOKENS, PLAKREGELS = haal_woordenlijst()
NUMMER_VAN = {stukje: nummer for nummer, stukje in enumerate(TOKENS)}
NAAR_TEKEN = byte_letters()
NAAR_BYTE = {teken: b for b, teken in NAAR_TEKEN.items()}
# Eerst grof knippen: losse woorden (met de spatie ervoor), getallen, leestekens.
GROF = re.compile(r"""'s|'t|'re|'ve|'m|'ll|'d| ?[^\W\d_]+| ?\d+| ?[^\s\w]+|\s+(?!\S)|\s+|_+""")


def plak(letters):
    # Begin met losse letters en plak steeds het paar aan elkaar dat het
    # vaakst voorkwam in de trainingsteksten (de laagste regelnummer).
    while len(letters) > 1:
        beste = None
        for i in range(len(letters) - 1):
            nummer = PLAKREGELS.get((letters[i], letters[i + 1]))
            if nummer is not None and (beste is None or nummer < beste[0]):
                beste = (nummer, i)
        if beste is None:
            break
        i = beste[1]
        letters = letters[:i] + [letters[i] + letters[i + 1]] + letters[i + 2:]
    return letters


def knip(tekst):
    """Geeft een lijst van (stukje, nummer) terug, net zoals de geest knipt."""
    uitkomst = []
    for woord in GROF.findall(tekst):
        letters = [NAAR_TEKEN[b] for b in woord.encode("utf-8")]
        for stukje in plak(letters):
            leesbaar = bytes(NAAR_BYTE[t] for t in stukje).decode("utf-8", errors="replace")
            uitkomst.append((leesbaar, NUMMER_VAN.get(stukje)))
    return uitkomst


def toon(tekst):
    # Een spatie laten we zien als een puntje: ·
    stukjes = knip(tekst)
    print("|".join(s.replace(" ", "·") for s, _ in stukjes), f"  → {len(stukjes)} stukjes")


def tel_alles(tekst):
    verzoek = {"model": fles.MODEL, "stream": False,
               "messages": [{"role": "user", "content": tekst}],
               "options": {"num_predict": 1, "temperature": 0}}
    antwoord = requests.post(fles.SERVER + "/api/chat", json=verzoek, timeout=300).json()
    return antwoord["prompt_eval_count"]


def tel_bij_de_geest(tekst):
    """Vraagt aan de geest zelf hoeveel tokens hij leest (prompt_eval_count)."""
    # De geest telt ook de verborgen labels rond je bericht mee
    # (<|im_start|>user ... <|im_end|> en zo). Die trekken we eraf.
    labels = tel_alles("kat") - len(knip("kat"))
    return tel_alles(tekst) - labels


def eerste_getal(tekst):
    gevonden = re.search(r"\d+", tekst)
    if gevonden:
        return int(gevonden.group())
    woorden = ["nul", "een", "twee", "drie", "vier", "vijf", "zes", "zeven", "acht", "negen", "tien"]
    for woord in re.findall(r"[a-z]+", tekst.lower()):
        if woord in woorden:
            return woorden.index(woord)
    return None


# =========================================================================
# HIER BEGIN JIJ
# =========================================================================

print("=== Proef 1: de knipmachine ===")
print(f"De geest kent {len(TOKENS)} stukjes. Zo knipt hij jouw woorden:\n")
for woord in WOORDEN:
    toon(woord)

print()
for zin in ZINNEN:
    toon(zin)

print("\nKlopt mijn knipmachine? We vragen de geest zelf hoeveel stukjes hij leest:")
for zin in ZINNEN[:2]:
    print(f"  {zin!r}: knipmachine {len(knip(zin))}, geest {tel_bij_de_geest(zin)}")

print("\n=== Proef 2: de teltest ===")
SYSTEEM = "Je bent een rekenmeester. Je antwoordt alleen met een getal."
aantal_goed = 0
for letter, woord in TELTEST:
    echt = woord.count(letter)
    print(f"\nHoeveel keer '{letter}' in '{woord}'? Python telt: {echt}")
    print("  Zo ziet de geest het woord:", "|".join(s for s, _ in knip(woord)))
    for poging in range(1, POGINGEN + 1):
        antwoord = vraag_een_keer(
            SYSTEEM,
            f"Hoeveel keer komt de letter {letter} voor in het woord {woord}?",
            temperatuur=0.7, seed=poging, toon=False)
        getal = eerste_getal(antwoord)
        if getal == echt:
            aantal_goed += 1
        teken = "✅" if getal == echt else "❌"
        print(f"  Poging {poging}: {teken} geest zegt {antwoord[:40]!r}")

print(f"\nDe geest telde {aantal_goed} van de {len(TELTEST) * POGINGEN} keer goed.")
print("Python telde alles goed. Welk getal zei de geest het vaakst?")

# ---------------------------------------------------------------------------
# PLUS – stukjes zijn getallen
#   De geest ziet geen letters, maar NUMMERS. Laat ze zien:
#       for stukje, nummer in knip("Ik heet Fatima"):
#           print(stukje, nummer)
#   Welk nummer heeft " de"? En "de" zonder spatie ervoor? Is dat hetzelfde?
#
# PLUS 2 – help de geest tellen
#   Geef het woord met streepjes mee: "a-a-r-d-b-e-i-e-n-r-i-j-s-t-e-b-r-i-j".
#   Toon eerst hoe dat geknipt wordt. Telt de geest nu beter? Waarom?
#
# EXPERT – wat kost Nederlands?
#   Grote AI-bedrijven laten je betalen PER TOKEN, en elk token kost rekentijd.
#   Neem een lange Nederlandse tekst en dezelfde tekst in het Engels.
#   Reken uit: hoeveel tokens per woord kost elke taal?
#       aantal_woorden = len(tekst.split())
#       aantal_tokens = len(knip(tekst))
#   Wie is er duurder uit: een Nederlandse of een Engelse gebruiker?
#   Extra: zoek het langste stukje dat alleen uit gewone letters bestaat:
#       print(max((t for t in TOKENS if t.isascii() and t.isalpha()), key=len))
#   Snap jij waarom dat rare woord in de woordenlijst staat?
