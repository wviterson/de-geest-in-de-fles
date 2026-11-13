# MODULE K – Is je geest goed?
#
# Hoe weet je of een AI goed is? Je kunt het niet zien aan één antwoord.
# Je moet hem TOETSEN, net als op school: een lijst vragen waarvan je het
# goede antwoord al weet. Zo'n toets voor AI heet een BENCHMARK.
#
# Dit programma laat de geest alle vragen beantwoorden, kijkt zelf na en
# geeft een cijfer. Maar let op: nakijken is moeilijker dan het lijkt!
#
# Druk op F5. Het duurt even: de geest maakt de toets een paar keer.

import fles
from fles import vraag_een_keer

fles.MAX_TOKENS = 60   # korte antwoorden: dan gaat de toets sneller

# De toets: (vraag, [woorden die in een goed antwoord moeten staan]).
# Staat ÉÉN van de woorden in het antwoord, dan rekent de computer het goed.
TOETS = [
    ("Wat is de hoofdstad van Frankrijk?", ["parijs"]),
    ("Hoeveel poten heeft een spin?", ["acht", "8"]),
    ("Wat is 7 keer 8?", ["56"]),
    ("Welke kleur krijg je als je blauw en geel mengt?", ["groen"]),
    ("Wie schilderde De Nachtwacht?", ["rembrandt"]),
    ("Wat is de grootste planeet van ons zonnestelsel?", ["jupiter"]),
    ("Hoeveel keer komt de letter r voor in aardbeienrijstebrij?", ["3", "drie"]),
    ("Wat is het tegenovergestelde van warm?", ["koud"]),
    # TODO 1: Voeg minstens drie eigen vragen toe. Kies vragen waarvan je
    #         ZEKER weet wat het goede antwoord is. Maak er ook één moeilijke.
]

# TODO 2: Verander de systeemprompt of de temperatuur. Wordt de geest beter?
#         Eerlijk vergelijken: verander maar ÉÉN ding tegelijk, en houd
#         SEEDS hetzelfde. Dan maakt de geest de toets met dezelfde dobbelstenen.
SYSTEEM = "Je bent een slimme geest. Je antwoordt kort, in één zin, in het Nederlands."
TEMPERATUUR = 0.7
SEEDS = [1, 2, 3]       # 3 seeds = de geest maakt de toets 3 keer


def nakijken(antwoord, sleutelwoorden):
    """Goed als één van de sleutelwoorden in het antwoord staat."""
    antwoord = antwoord.lower()
    for woord in sleutelwoorden:
        if woord in antwoord:
            return True
    return False


def maak_toets(seed):
    """De geest maakt de hele toets één keer. Geeft het aantal goed terug."""
    aantal_goed = 0
    for vraag_tekst, sleutelwoorden in TOETS:
        antwoord = vraag_een_keer(SYSTEEM, vraag_tekst, temperatuur=TEMPERATUUR,
                                  seed=seed, toon=False)
        goed = nakijken(antwoord, sleutelwoorden)
        if goed:
            aantal_goed += 1
        teken = "✅" if goed else "❌"
        kort = antwoord.replace("\n", " ")[:70]
        print(f"  {teken} {vraag_tekst}\n       geest: {kort}")
    return aantal_goed


def cijfer(aantal_goed, aantal_vragen):
    """Een schoolcijfer van 1 tot 10."""
    return round(1 + 9 * aantal_goed / aantal_vragen, 1)


cijfers = []
for seed in SEEDS:
    print(f"\n=== De geest maakt de toets (seed {seed}) ===")
    goed = maak_toets(seed)
    c = cijfer(goed, len(TOETS))
    cijfers.append(c)
    print(f"  Score: {goed} van {len(TOETS)} goed → cijfer {c}")

print(f"\nCijfers: {cijfers}")
print(f"Gemiddeld cijfer: {round(sum(cijfers) / len(cijfers), 1)}")

# TODO 3: Kijk alle ✅ en ❌ na met je eigen ogen. Is de computer een eerlijke
#         nakijker? Zoek een antwoord dat GOED is gerekend maar fout is,
#         of andersom. Hoe komt dat? Kun je nakijken() slimmer maken?
#         (Denk aan: "acht" staat ook in "achtentwintig"...)

# ---------------------------------------------------------------------------
# PLUS – twee geesten tegen elkaar
#   Maak een tweede systeemprompt, bijvoorbeeld een piraat of een geest die
#   "Denk eerst stap voor stap na" krijgt. Laat beide geesten de toets maken
#   met dezelfde SEEDS. Welke wint? Is het verschil groot genoeg om zeker te
#   zijn, of kan het ook toeval (de dobbelsteen) zijn? Probeer meer seeds.
#
# EXPERT – een geest als nakijker
#   Grote bedrijven laten vaak een AI de antwoorden van een AI nakijken.
#   Dat heet "LLM als rechter". Maak een functie:
#       def rechter(vraag_tekst, goed_antwoord, antwoord):
#           oordeel = vraag_een_keer(
#               "Je bent een strenge juf. Je antwoordt alleen GOED of FOUT.",
#               f"Vraag: {vraag_tekst}\nGoed antwoord: {goed_antwoord}\n"
#               f"Antwoord van de leerling: {antwoord}\nIs dit GOED of FOUT?",
#               temperatuur=0, toon=False)
#           return "GOED" in oordeel.upper()
#   Test de rechter eerst met antwoorden die JIJ verzint, waarvan je weet of
#   ze goed of fout zijn. Bijvoorbeeld: "Een spin heeft zes poten."
#   Is de rechter-geest eerlijk? Wie controleert de controleur?
