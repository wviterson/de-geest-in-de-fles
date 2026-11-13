# De Geest in de Fles - startcode
# Druk op F5 (of op de groene knop) om je geest te wekken.

import json

import requests

from fles import MAX_TOKENS, MODEL, SERVER  # het adres van de geest staat in fles.py
from stem import zeg

# Dit is de complete code "onder de motorkap": zo praat Python met de geest.
# In de levels doet fles.py dit werk voor je.

# Dit is de "systeemprompt": de geheime instructie die bepaalt wie je geest is.
SYSTEEM = (
    "Je bent een eeuwenoude geest die in een glazen fles woont. "
    "Je spreekt Nederlands en geeft korte, mysterieuze antwoorden."
)

# Het geheugen van de geest: alle berichten tot nu toe.
berichten = [{"role": "system", "content": SYSTEEM}]


def vraag_de_geest(vraag):
    berichten.append({"role": "user", "content": vraag})
    verzoek = {"model": MODEL, "messages": berichten, "stream": True,
               "options": {"num_predict": MAX_TOKENS}}  # nooit eindeloos doorpraten

    antwoord = ""
    with requests.post(SERVER + "/api/chat", json=verzoek, stream=True, timeout=300) as r:
        r.raise_for_status()
        for regel in r.iter_lines():
            if regel:
                stukje = json.loads(regel)["message"]["content"]
                print(stukje, end="", flush=True)
                antwoord += stukje
    print()

    berichten.append({"role": "assistant", "content": antwoord})
    # Wil je dat de geest hardop praat? Haal het hekje weg op de volgende regel.
    # zeg(antwoord)
    return antwoord


print("De geest ontwaakt... (typ 'stop' om te stoppen)")
while True:
    vraag = input("\nJij: ")
    if vraag.strip().lower() == "stop":
        print("De geest kruipt terug in zijn fles.")
        break
    print("Geest: ", end="")
    try:
        vraag_de_geest(vraag)
    except requests.ConnectionError:
        print("\nIk kan de geest niet bereiken. Is start.bat (of de docent-server) gestart?")
        berichten.pop()
