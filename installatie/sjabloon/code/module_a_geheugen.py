# MODULE A – Geheugen en context
#
# Een geheim: de geest heeft GEEN geheugen. Elke vraag is voor hem de
# allereerste. Toch lijkt het alsof een chatbot onthoudt wat je zei.
# Hoe kan dat? Het PROGRAMMA plakt elke keer het hele gesprek opnieuw
# in de fles. Dat gesprek heet de CONTEXT.
#
# Maar de fles is niet oneindig groot. Er passen maar 2048 tokens
# (stukjes woord) in. Dat heet het CONTEXTVENSTER. Wat gebeurt er als het
# gesprek groter wordt dan de fles?
#
# Druk op F5 en praat met de geest. Typ 'stop' om te stoppen.
# Typ 'verhaal' om in één keer een lang verhaal in de fles te gooien.

import json

import requests

from fles import SERVER, MODEL, MAX_TOKENS

SYSTEEM = (
    "Je bent een vriendelijke geest in een fles. "
    "Je antwoordt kort, in één of twee zinnen, in het Nederlands."
)

# TODO 1: Begin met False. Vertel de geest je naam en vraag daarna:
#         "Hoe heet ik?" Weet hij het nog? Zet dan ONTHOUDEN op True.
ONTHOUDEN = False

# TODO 2: Zet LAAT_ZIEN op True. Dan zie je wat het programma ELKE KEER
#         naar de geest stuurt. Wordt die lijst langer of niet?
LAAT_ZIEN = False

# TODO 3: Hoe vol is de fles? Kijk naar de meter onder elk antwoord.
#         Typ een paar keer 'verhaal' en vraag dan weer: "Hoe heet ik?"
#         Wat gebeurt er als de meter bijna vol is?

# TODO 4: Programmeer zelf een geheugen-wis: stuur alleen de laatste
#         paar berichten mee. Verander None in bijvoorbeeld 4.
#         Hoeveel berichten zijn nodig om je naam te onthouden?
LAATSTE_BERICHTEN = None

CONTEXTVENSTER = 2048   # zoveel tokens passen er in de fles van Fietje

VERHAAL = (
    "Er was eens een klein dorp aan een brede rivier. Elke ochtend liep "
    "bakker Joris met een mand vol broodjes over de brug naar de markt. "
    "Op een dag zag hij een fles in het water drijven. Er zat een briefje "
    "in, maar de letters waren te klein om te lezen. Joris nam de fles mee "
    "naar huis en zette hem op de vensterbank, naast de plantjes van zijn "
    "buurvrouw. 's Nachts begon de fles zachtjes te zoemen en te gloeien. "
) * 5   # het verhaal staat er 5 keer in, zo wordt hij lekker lang


def vraag_met_meter(berichten):
    """Stuurt de berichten naar de geest, print het antwoord woord voor woord
    en geeft (antwoord, aantal tokens in de fles) terug."""
    verzoek = {"model": MODEL, "messages": berichten, "stream": True,
               "options": {"temperature": 0.3, "num_predict": MAX_TOKENS}}
    antwoord = ""
    tokens = 0
    try:
        with requests.post(SERVER + "/api/chat", json=verzoek, stream=True, timeout=300) as r:
            for regel in r.iter_lines():
                if not regel:
                    continue
                stukje = json.loads(regel)
                antwoord += stukje["message"]["content"]
                print(stukje["message"]["content"], end="", flush=True)
                if stukje.get("done"):
                    # prompt_eval_count = hoeveel tokens de geest LAS
                    # eval_count        = hoeveel tokens hij SCHREEF
                    tokens = stukje.get("prompt_eval_count", 0) + stukje.get("eval_count", 0)
    except requests.ConnectionError:
        raise SystemExit("\nIk kan de geest niet bereiken. Is start.bat (of de docent-server) gestart?")
    print()
    return antwoord.strip(), tokens


def toon_meter(tokens):
    vol = min(20, round(20 * tokens / CONTEXTVENSTER))
    print(f"   Fles: [{'#' * vol}{'.' * (20 - vol)}] {tokens} van {CONTEXTVENSTER} tokens")


def kies_berichten(gesprek):
    """Welke berichten gaan er mee in de fles?"""
    if LAATSTE_BERICHTEN is None:
        return gesprek
    return gesprek[-LAATSTE_BERICHTEN:]


gesprek = []          # het hele gesprek: jouw berichten en die van de geest
vorige_meter = 0

print("De geest ontwaakt... (typ 'stop' om te stoppen, 'verhaal' voor een lang verhaal)")
while True:
    tekst = input("\nJij: ")
    if tekst.strip().lower() == "stop":
        break
    if tekst.strip().lower() == "verhaal":
        tekst = "Vertel in één zin waar dit verhaal over gaat: " + VERHAAL
        print("(Je gooit een lang verhaal in de fles...)")

    nieuw = {"role": "user", "content": tekst}
    if ONTHOUDEN:
        gesprek.append(nieuw)
        berichten = [{"role": "system", "content": SYSTEEM}] + kies_berichten(gesprek)
    else:
        berichten = [{"role": "system", "content": SYSTEEM}, nieuw]

    if LAAT_ZIEN:
        print(f"   [Het programma stuurt {len(berichten)} berichten naar de geest:]")
        for bericht in berichten:
            print(f"   - {bericht['role']}: {bericht['content'][:60]}")

    print("Geest: ", end="")
    antwoord, meter = vraag_met_meter(berichten)
    if ONTHOUDEN:
        gesprek.append({"role": "assistant", "content": antwoord})

    toon_meter(meter)
    if ONTHOUDEN and meter < vorige_meter:
        print("   😱 De meter is gezakt! Het begin van het gesprek zit niet meer in de fles.")
        if LAATSTE_BERICHTEN is None:
            print("      Het gesprek paste niet meer, dus de oudste berichten zijn weggegooid.")
        else:
            print("      Jouw geheugen-wis stuurt alleen de laatste berichten mee.")
    vorige_meter = meter

# ---------------------------------------------------------------------------
# PLUS – een notitieboekje, zoals ChatGPT
#   Sommige chatbots hebben een "geheugen". Dat werkt zo: ze schrijven
#   korte NOTITIES over jou op, en die zetten ze stiekem in de systeemprompt.
#   Maak een lijst NOTITIES = [] boven de while-lus. Als je typt
#   "onthoud: ik heb een hond die Bram heet", voeg je dat toe aan de lijst:
#       if tekst.lower().startswith("onthoud:"):
#           NOTITIES.append(tekst[8:].strip())
#   Zet de notities in de systeemprompt:
#       systeem = SYSTEEM + " Wat je weet over de gebruiker: " + " ".join(NOTITIES)
#   Werkt het, ook als LAATSTE_BERICHTEN = 2? Waarom wel?
#
# EXPERT – een samenvatting als geheugen
#   Gooi oude berichten niet weg, maar vat ze samen! Als het gesprek langer
#   is dan 6 berichten, laat je een TWEEDE geest de oudste berichten samenvatten:
#       from fles import vraag_een_keer
#       oud = "\n".join(b["role"] + ": " + b["content"] for b in gesprek[:-4])
#       samenvatting = vraag_een_keer(
#           "Je schrijft korte samenvattingen in het Nederlands.",
#           "Gesprek:\n" + oud + "\n\nSchrijf in één zin wat we weten over "
#           "de gebruiker. Begin met: De gebruiker",
#           temperatuur=0.3, toon=False)
#   Tip: zet de opdracht ÁCHTER het gesprek, anders herhaalt de geest
#   alleen maar het gesprek.
#   Zet de samenvatting in de systeemprompt en stuur alleen de laatste
#   4 berichten mee. Wat onthoudt hij nu wel, en wat raakt hij kwijt?
