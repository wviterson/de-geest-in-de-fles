# LEVEL 1 – Wek je geest
#
# Elke chatbot heeft een geheime instructie die jij niet ziet: de SYSTEEMPROMPT.
# Daarin staat wie de chatbot is en hoe hij moet praten.
# In dit level schrijf jij die instructie zelf.
#
# Druk op F5 om te starten. Typ 'stop' om te stoppen.

from fles import vraag

# TODO 1: Verander de systeemprompt. Wie is jouw geest?
#         Een piraat? Een chagrijnige oma? Een robot uit het jaar 3000?
#         Vertel hoe hij praat, wat hij leuk vindt en wat hij nooit zou zeggen.
SYSTEEM = (
    "Je bent een eeuwenoude geest die in een glazen fles woont. "
    "Je spreekt Nederlands en geeft korte, mysterieuze antwoorden."
)

# TODO 2: Geef je geest een naam. Die staat voor elk antwoord.
NAAM = "Geest"

berichten = [{"role": "system", "content": SYSTEEM}]

print(f"{NAAM} ontwaakt... (typ 'stop' om te stoppen)")
while True:
    vraag_tekst = input("\nJij: ")
    if vraag_tekst.strip().lower() == "stop":
        break
    berichten.append({"role": "user", "content": vraag_tekst})
    print(f"{NAAM}: ", end="")
    antwoord = vraag(berichten)
    berichten.append({"role": "assistant", "content": antwoord})

# ---------------------------------------------------------------------------
# PLUS
#   Laat je geest elk gesprek beginnen met een begroeting, nog voordat jij iets typt.
#   Tip: voeg vóór de while-lus een bericht toe en roep vraag() aan.
#
# EXPERT
#   Geef je geest een vaste vorm: hij moet ALTIJD in rijm antwoorden, of altijd
#   eindigen met een vraag. Lukt het hem altijd? Wat doe je als hij het vergeet?
#   Bedenk: is de systeemprompt een wet, of meer een sterke wens?
