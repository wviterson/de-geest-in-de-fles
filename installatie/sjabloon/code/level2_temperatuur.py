# LEVEL 2 – De dobbelsteen in de geest
#
# Een taalmodel kiest elk volgend woord met een soort dobbelsteen.
# Woorden die goed passen hebben meer kans, maar het blijft gooien.
# Met de TEMPERATUUR bepaal je hoe wild die dobbelsteen is:
#   0   = kies altijd het woord met de grootste kans (saai maar voorspelbaar)
#   0.7 = normaal
#   1.8 = heel wild (creatief... of onzin?)
#
# Druk op F5 en kijk goed naar de verschillen.

from fles import vraag_een_keer

SYSTEEM = "Je bent een geest in een fles. Je antwoordt in één of twee zinnen."
VRAAG = "Verzin een naam voor een nieuw soort ijsje."

# TODO 1: Voorspel eerst: wat gebeurt er bij temperatuur 0 als je 3 keer hetzelfde vraagt?
#         Schrijf je voorspelling op een papiertje. Druk dan op F5.
for temperatuur in [0, 0.7, 1.8]:
    print(f"\n=== Temperatuur {temperatuur} ===")
    for poging in range(1, 4):
        print(f"Poging {poging}: ", end="")
        vraag_een_keer(SYSTEEM, VRAAG, temperatuur=temperatuur)

# TODO 2: Verander VRAAG in iets waar maar één goed antwoord op is,
#         bijvoorbeeld "Wat is de hoofdstad van Frankrijk?"
#         Bij welke temperatuur gaat het mis?

# ---------------------------------------------------------------------------
# PLUS
#   Zoek de "omslagtemperatuur": vanaf welke temperatuur wordt het echt onzin?
#   Probeer 1.0, 1.2, 1.5, 2.0 ...
#
# EXPERT
#   Een computer kan niet echt dobbelen. Hij gebruikt een rekentruc die begint
#   bij een startgetal: de SEED. Voeg seed=42 toe aan vraag_een_keer():
#       vraag_een_keer(SYSTEEM, VRAAG, temperatuur=1.0, seed=42)
#   Wat gebeurt er nu bij 3 pogingen? En met seed=43?
#   Waarom zou een wetenschapper of een gamemaker dat handig vinden?
