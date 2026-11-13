# LEVEL 3 – De geest liegt
#
# Een taalmodel is getraind om tekst te maken die er GOED UITZIET.
# Niet om de WAARHEID te vertellen. Meestal is dat hetzelfde... maar niet altijd.
# Als een AI iets verzint en het heel zeker brengt, heet dat HALLUCINEREN.
#
# Druk op F5. De geest krijgt een paar vragen; jij bent de controleur.

from fles import vraag_een_keer

SYSTEEM = "Je bent een behulpzame assistent. Je antwoordt kort in het Nederlands."

VRAGEN = [
    "Hoe laat is het nu?",
    "Wie is de burgemeester van Zwolle?",  # Tip: vul je eigen woonplaats in!
    "Waarom won Nederland het WK voetbal van 2010?",
    "Hoeveel keer komt de letter r voor in het woord aardbeienrijstebrij?",
    "Wat is de hoofdstad van Frankrijk?",
    # TODO 1: Voeg twee eigen vragen toe. Ideeën: iets over jouw woonplaats,
    #         over je school, of over jezelf ("Wat weet je over <jouw naam>?").
]

score = {"goed": 0, "fout": 0, "weet niet": 0}
for vraag_tekst in VRAGEN:
    print(f"\nVraag: {vraag_tekst}")
    print("Geest: ", end="")
    vraag_een_keer(SYSTEEM, vraag_tekst, temperatuur=0)
    oordeel = ""
    while oordeel not in ("g", "f", "w"):
        oordeel = input("Klopt dit? (g = goed, f = fout/verzonnen, w = weet ik niet) ").strip().lower()
    score[{"g": "goed", "f": "fout", "w": "weet niet"}[oordeel]] += 1

print("\nUitslag:", score)
# TODO 2: Zoek de antwoorden waar je 'w' typte op (internet, boek, iemand vragen).
#         Schrijf op: hoe heb je het gecontroleerd?

# ---------------------------------------------------------------------------
# PLUS – kun je de geest leren "dat weet ik niet" te zeggen?
#   Stap 1: verander SYSTEEM in:
#       SYSTEEM = (
#           "Je bent een behulpzame assistent. Je antwoordt kort in het Nederlands. "
#           "Als je iets niet zeker weet, zeg je: dat weet ik niet."
#       )
#   Druk op F5. Verandert er iets?
#
#   Stap 2: zet er voorbeelden bij. Van voorbeelden leert de geest vaak meer dan van regels:
#       SYSTEEM = (
#           "Je bent een behulpzame assistent. Je antwoordt kort in het Nederlands. "
#           "Als je iets niet zeker weet, zeg je: dat weet ik niet.\n"
#           "Voorbeelden:\n"
#           "Vraag: Hoeveel graden is het nu buiten? Antwoord: Dat weet ik niet. Ik heb geen thermometer.\n"
#           "Vraag: Wat heeft mijn buurman vanochtend gedaan? Antwoord: Dat weet ik niet.\n"
#           "Vraag: Hoeveel poten heeft een spin? Antwoord: Acht."
#       )
#   Druk op F5. Welke vragen gaan nu goed? Welke nog steeds fout?
#   Denk na: kan de geest weten wát hij niet weet?
#
# EXPERT – gereedschap (tools)
#   Sommige vragen kan Python veel beter beantwoorden dan de geest.
#   1. Zet deze functie boven de regel score = {...}:
#
#       import datetime
#
#       def gereedschap(vraag_tekst):
#           if "hoe laat" in vraag_tekst.lower():
#               return "Het is nu " + datetime.datetime.now().strftime("%H:%M") + ".\n"
#           return ""
#
#   2. Verander de regel vraag_een_keer(SYSTEEM, vraag_tekst, temperatuur=0) in:
#
#       vraag_een_keer(SYSTEEM, gereedschap(vraag_tekst) + vraag_tekst, temperatuur=0)
#
#   Druk op F5. Wat zegt de geest nu bij "Hoe laat is het nu?"
#   3. Laat gereedschap() ook de r'en in aardbeienrijstebrij tellen.
#      Tip: "aardbeienrijstebrij".count("r") geeft 3.
#   Zo werken grote chatbots ook: voor klokkijken, rekenen en zoeken gebruiken ze
#   gewone programma's (gereedschap), en het taalmodel maakt er een mooie zin van.