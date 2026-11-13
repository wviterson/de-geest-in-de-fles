# De fles: hier woont de verbinding met de geest.
#
# Je hoeft dit bestand niet te veranderen, behalve als je docent een server gebruikt:
# zet dan hieronder bij SERVER het adres dat op het bord staat.
# Nieuwsgierig hoe het werkt? Lees gerust verder, of kijk in geest.py.

import json

import requests

SERVER = "http://127.0.0.1:11434"
MODEL = "bramvanroy/fietje-2b-chat:Q5_K_M"

# Kleine taalmodellen blijven soms eindeloos doorpraten. Na zoveel tokens
# (stukjes woord) houdt de geest daarom altijd op.
MAX_TOKENS = 300


def vraag(berichten, temperatuur=0.7, seed=None, toon=True):
    """Stuurt de berichten naar de geest en geeft zijn antwoord terug.

    berichten:   lijst met {"role": ..., "content": ...}
    temperatuur: 0 = altijd het meest waarschijnlijke woord, 2 = heel wild
    seed:        een getal; met dezelfde seed krijg je hetzelfde antwoord
    toon:        True = print het antwoord woord voor woord
    """
    opties = {"temperature": temperatuur, "num_predict": MAX_TOKENS}
    if seed is not None:
        opties["seed"] = seed
    verzoek = {"model": MODEL, "messages": berichten, "options": opties, "stream": True}

    antwoord = ""
    try:
        with requests.post(SERVER + "/api/chat", json=verzoek, stream=True, timeout=300) as r:
            r.raise_for_status()
            for regel in r.iter_lines():
                if regel:
                    stukje = json.loads(regel)["message"]["content"]
                    if toon:
                        print(stukje, end="", flush=True)
                    antwoord += stukje
    except requests.ConnectionError:
        raise SystemExit("\nIk kan de geest niet bereiken. Is start.bat (of de docent-server) gestart?")
    if toon:
        print()
    return antwoord.strip()


def vraag_een_keer(systeem, vraag_tekst, temperatuur=0.7, seed=None, toon=True):
    """Stelt één losse vraag aan een geest met deze systeemprompt (zonder geheugen)."""
    berichten = [
        {"role": "system", "content": systeem},
        {"role": "user", "content": vraag_tekst},
    ]
    return vraag(berichten, temperatuur, seed, toon)
