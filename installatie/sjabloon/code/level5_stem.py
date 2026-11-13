# LEVEL 5 – De geest krijgt een stem
#
# Je geest kan nu ook praten. Dat doet een TWEEDE kleine AI: Piper.
# Piper heeft geleerd van opnames van echte mensen hoe tekst klinkt.
#
# Druk op F5. Zet je geluid aan!

from fles import vraag
from stem import stemmen, zeg

print("Deze stemmen staan op je laptop:", stemmen())

# TODO 1: Kies een stem uit het lijstje hierboven en een snelheid (1.0 = normaal).
STEM = "nl_NL-pim-medium"
SNELHEID = 1.0

# TODO 2: Plak hier de systeemprompt van jouw geest uit level 1.
SYSTEEM = (
    "Je bent een eeuwenoude geest die in een glazen fles woont. "
    "Je spreekt Nederlands en geeft korte, mysterieuze antwoorden."
)

berichten = [{"role": "system", "content": SYSTEEM}]
zeg("Ik ben ontwaakt. Wat is je wens?", stem=STEM, snelheid=SNELHEID)

while True:
    vraag_tekst = input("\nJij: ")
    if vraag_tekst.strip().lower() == "stop":
        zeg("Ik kruip terug in mijn fles.", stem=STEM, snelheid=SNELHEID)
        break
    berichten.append({"role": "user", "content": vraag_tekst})
    print("Geest: ", end="")
    antwoord = vraag(berichten)
    berichten.append({"role": "assistant", "content": antwoord})
    zeg(antwoord, stem=STEM, snelheid=SNELHEID)

# ---------------------------------------------------------------------------
# PLUS
#   Past de stem bij je geest? Een piraat met een rustige stem, of een robot
#   die heel snel praat (snelheid 1.6)? Probeer alle stemmen uit.
#
# EXPERT – twee geesten in gesprek
#   Maak twee geesten met elk een eigen systeemprompt én een eigen stem.
#   Laat ze om de beurt op elkaar reageren: het antwoord van de één wordt
#   de vraag voor de ander. Waar praten ze na 6 beurten over?
#   Let op: elke geest heeft zijn eigen berichtenlijst nodig.
#
# OM OVER NA TE DENKEN
#   Met een paar minuten opname kun je tegenwoordig iemands stem nadoen.
#   Wat betekent dat als je een spraakbericht krijgt van "je moeder"?
