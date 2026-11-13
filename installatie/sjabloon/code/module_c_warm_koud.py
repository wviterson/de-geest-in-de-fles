# MODULE C – Betekenis als getallen (het warm-koud-spel)
#
# Hoe weet een computer dat "fiets" en "bromfiets" op elkaar lijken?
# Hij rekent elk woord (of elke zin) om naar een lange lijst GETALLEN.
# Zo'n lijst heet een EMBEDDING. Woorden met een betekenis die op elkaar lijkt,
# krijgen lijsten die op elkaar lijken. Je kunt het zien als een plek op een
# enorme KAART: fiets en bromfiets liggen dicht bij elkaar, banaan ligt ver weg.
#
# Dit programma gebruikt niet Fietje, maar een tweede model: bge-m3.
# Dat model praat niet. Het maakt alleen getallen.
#
# Druk op F5. Eerst zie je een woord als getallen, dan vergelijk je woorden,
# en daarna speel je het warm-koud-spel: raad het geheime woord!
# (De eerste keer duurt het even: het model moet nog worden geladen.)

import random
import unicodedata

from betekenis import embed, gelijkenis, lijkt_op

# De computer zet elk woord in een zinnetje. Dan begrijpt het model beter
# dat "piraat" een persoon is, en niet alleen een woord dat op "piloot" lijkt.
ZIN = "Ik denk aan een {}."

# Deze woorden kent het spel. Een woord dat je raadt, mag ook een ander woord zijn.
WOORDEN = """
hond kat paard koe varken schaap kip eend konijn muis olifant leeuw tijger giraf
aap beer wolf vos uil vis haai walvis dolfijn slang spin vlinder bij mier kikker schildpad
appel peer banaan aardbei druif citroen sinaasappel tomaat wortel aardappel brood kaas
melk ei pizza patat pannenkoek soep chocolade snoep ijsje taart koekje hagelslag drop
fiets bromfiets scooter auto bus trein tram vliegtuig boot schip helikopter raket
vrachtwagen tractor motor step skateboard
school klas juf meester boek pen potlood gum schrift rugzak bord huiswerk toets les pauze vakantie
voetbal hockey tennis zwemmen schaatsen judo dansen turnen basketbal doelpunt scheidsrechter bal medaille
zon maan ster wolk regen sneeuw storm bliksem regenboog wind ijs vuur water zee strand
berg bos boom bloem gras rivier eiland woestijn vulkaan
huis kamer keuken bed stoel tafel deur raam dak trap tuin lamp bank kast spiegel
dokter politie brandweer bakker boer kok piloot astronaut leraar kapper soldaat
koning koningin prins prinses ridder piraat heks tovenaar draak geest robot
jas broek trui schoen sok muts sjaal jurk bril horloge
gitaar piano trommel viool fluit liedje muziek concert
hoofd hand voet oog oor neus mond tand haar hart buik
telefoon computer laptop televisie tablet spelcomputer internet camera radio
geld cadeau feest verjaardag kerst sinterklaas pasen kaars ballon
kasteel kerk winkel ziekenhuis bibliotheek museum dierentuin speeltuin zwembad stad dorp boerderij brug
lente zomer herfst winter ochtend nacht
vriend familie moeder vader broer zus opa oma baby
""".split()

# Uit deze woorden kiest de computer zijn geheim. Ze speelden goed in onze test.
GEHEIME_WOORDEN = ["fiets", "sneeuw", "gitaar", "voetbal", "vulkaan", "piraat",
                   "pizza", "dokter", "kasteel", "raket", "zwembad", "draak"]

# TODO 3: Laat het andere tweetal een geheim woord kiezen en hier invullen
#         (zonder dat jullie kijken!). Leeg laten = de computer kiest.
GEHEIM = ""

# Hoe warm is het? Dat hangt af van de PLEK van je woord in de lijst:
# plek 1 = het woord uit de lijst dat het meest op het geheim lijkt.
TEMPERATUREN = [
    (3, "🔥🔥 GLOEIEND HEET"),
    (10, "🔥 heet"),
    (25, "☀️ warm"),
    (60, "🙂 lauw"),
    (120, "❄️ koud"),
    (9999, "🧊 ijskoud"),
]


def toon_getallen(woord, aantal=10):
    """Laat zien hoe een woord eruitziet voor de computer: een lijst getallen."""
    getallen = embed(woord)
    stukje = ", ".join(f"{g:+.3f}" for g in getallen[:aantal])
    print(f"{woord:>10}: [{stukje}, ...]  ({len(getallen)} getallen)")


def vergelijk(a, b):
    """Print hoeveel twee woorden (of zinnen) op elkaar lijken."""
    score = lijkt_op(a, b)
    balkje = "█" * round(score * 20)
    print(f"{a:>12} ~ {b:<12} {score:.2f} {balkje}")


def maak_ranglijst(geheim):
    """Zet alle woorden uit de lijst op volgorde: het meest op het geheim lijkend eerst."""
    geheim_getallen = embed(ZIN.format(geheim))
    lijst = [w for w in WOORDEN if w != geheim]
    getallen = embed([ZIN.format(w) for w in lijst])
    scores = [(gelijkenis(geheim_getallen, g), w) for g, w in zip(getallen, lijst)]
    return sorted(scores, reverse=True)


def plek_van(gok, geheim, ranglijst):
    """Op welke plek zou de gok in de ranglijst staan?"""
    score = lijkt_op(ZIN.format(gok), ZIN.format(geheim))
    hoger = sum(1 for s, w in ranglijst if s > score and w != gok)
    return hoger + 1, score


def temperatuur(plek):
    for grens, woord in TEMPERATUREN:
        if plek <= grens:
            return woord


def zonder_accenten(woord):
    """pinguïn wordt pinguin, café wordt cafe: dan telt een gok zonder puntjes ook."""
    return "".join(t for t in unicodedata.normalize("NFD", woord) if not unicodedata.combining(t))


def hint(ranglijst, beste_plek, geraden):
    """Geeft een woord dat net iets warmer is dan je beste gok tot nu toe."""
    doel = max(2, beste_plek // 2)
    for score, woord in ranglijst[doel - 1:] + ranglijst:
        if woord not in geraden:
            return woord


# --- Deel 1: een woord als getallen ---------------------------------------
print("Deel 1: zo ziet een woord eruit voor de computer.\n")
for woord in ["fiets", "bromfiets", "banaan"]:
    toon_getallen(woord)

# --- Deel 2: woorden vergelijken ------------------------------------------
# 1.00 = precies hetzelfde. Hoe hoger, hoe meer de betekenis lijkt.
# TODO 1: Voeg eigen woordparen toe. Welk paar lijkt het meest? Welk het minst?
#         Kun je de computer verrassen? (Tip: probeer appel ~ computer.)
PAREN = [
    ("fiets", "bromfiets"),
    ("fiets", "auto"),
    ("fiets", "banaan"),
    ("blij", "vrolijk"),
    ("blij", "verdrietig"),
]
print("\nDeel 2: hoeveel lijken ze op elkaar?\n")
for a, b in PAREN:
    vergelijk(a, b)
# TODO 2: Zelfs fiets ~ banaan krijgt bijna 0.50. Waarom is het getal zelf
#         dan niet zo belangrijk, maar de VOLGORDE wel? Schrijf je antwoord op.

# --- Deel 3: het warm-koud-spel -------------------------------------------
geheim = GEHEIM.strip().lower() or random.choice(GEHEIME_WOORDEN)
print(f"\nDeel 3: het warm-koud-spel. De computer rekent {len(WOORDEN)} woorden om...")
ranglijst = maak_ranglijst(geheim)
print("Raad het geheime woord! Typ één woord. 'hint' = tip, 'stop' = opgeven.")

geraden = []
beste_plek = len(WOORDEN)
while True:
    gok = input("\nJouw gok: ").strip().lower()
    if not gok:
        continue
    if gok == "stop":
        print(f"Het geheime woord was: {geheim}")
        break
    if gok == "hint":
        tip = hint(ranglijst, beste_plek, geraden)
        print(f"💡 Probeer eens iets in de buurt van '{tip}'.")
        continue
    if zonder_accenten(gok) == zonder_accenten(geheim):
        print(f"🎉 GEVONDEN! Het was '{geheim}'. Dat lukte in {len(geraden) + 1} gokken.")
        break
    geraden.append(gok)
    plek, score = plek_van(gok, geheim, ranglijst)
    beste_plek = min(beste_plek, plek)
    print(f"{temperatuur(plek)}  (plek {plek} van {len(ranglijst)}, gelijkenis {score:.2f})")

print("\nDe 10 woorden die het meest op het geheim leken:")
print(", ".join(w for s, w in ranglijst[:10]))

# ---------------------------------------------------------------------------
# PLUS – rekenen met betekenis
#   Omdat woorden getallen zijn, kun je ermee rekenen! Een beroemde som is:
#   koning - man + vrouw = ?  (Hopelijk: koningin.) Plak dit onderaan en druk F5:
#
#       def reken(a, min_woord, plus_woord):
#           ga, gm, gp = embed([ZIN.format(a), ZIN.format(min_woord), ZIN.format(plus_woord)])
#           uitkomst = [x - y + z for x, y, z in zip(ga, gm, gp)]
#           kandidaten = [w for w in WOORDEN if w not in (a, min_woord, plus_woord)]
#           getallen = embed([ZIN.format(w) for w in kandidaten])
#           scores = sorted(((gelijkenis(uitkomst, g), w) for g, w in zip(getallen, kandidaten)), reverse=True)
#           print(f"{a} - {min_woord} + {plus_woord} = ", [w for s, w in scores[:3]])
#
#       reken("koning", "man", "vrouw")
#       reken("prins", "broer", "zus")
#
#   De woorden uit de som zelf doen niet mee als antwoord; anders wint vaak
#   gewoon een van die woorden.
#   Werkt het altijd? Probeer ook: reken("koe", "melk", "ei")  (je hoopt: kip).
#   Bedenk zelf sommen. (Tip: staat het antwoord dat je verwacht niet in
#   WOORDEN, zoals "kip"? Zet het er dan eerst bij.)
#
# EXPERT – zinnen vergelijken
#   Het model kan ook hele zinnen vergelijken. Probeer:
#       vergelijk("Ik heb honger.", "Ik wil graag iets eten.")
#       vergelijk("Ik heb honger.", "Ik heb geen honger.")
#       vergelijk("De hond bijt de man.", "De man bijt de hond.")
#   Welke zinnen lijken volgens de computer op elkaar, terwijl ze iets heel
#   anders betekenen? En andersom? Zo zoeken zoekmachines naar BETEKENIS in
#   plaats van naar precies dezelfde woorden.
#
# EXPERT 2 – leert de computer ook vooroordelen?
#   Het model leerde van heel veel teksten die mensen schreven. Vergelijk:
#       for beroep in ["verpleegkundige", "piloot", "ingenieur", "leraar"]:
#           vergelijk("man", beroep)
#           vergelijk("vrouw", beroep)
#   Ligt een beroep dichter bij "man" of bij "vrouw"? Hoe kan dat?
#   En waarom is dat een probleem als een computer zo cv's gaat sorteren?
