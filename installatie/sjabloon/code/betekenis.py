# Betekenis: hier maakt de computer van woorden een lijst getallen.
#
# Dit hulpbestand wordt gebruikt door module C (warm-koud) en module D (kennis).
# Je hoeft het niet te veranderen. Nieuwsgierig? Lees gerust verder.
#
# Een EMBEDDING is een lange lijst getallen die de betekenis van een tekst
# beschrijft. Teksten die op elkaar lijken, krijgen lijsten die op elkaar lijken.
# Het model dat dit doet heet bge-m3. Het praat niet: het maakt alleen getallen.

import math
import time

import requests

from fles import SERVER

EMBED_MODEL = "bge-m3"

# Elke tekst die al eens is omgerekend, onthouden we hier. Dat scheelt wachten.
_onthouden = {}


def embed(teksten):
    """Geeft voor elke tekst een lijst getallen (een embedding) terug.

    teksten: één tekst, of een lijst met teksten.
    Bij één tekst krijg je één lijst getallen terug, bij een lijst een lijst met lijsten.
    """
    los = isinstance(teksten, str)
    lijst = [teksten] if los else list(teksten)
    nieuw = [t for t in dict.fromkeys(lijst) if t not in _onthouden]
    if nieuw:
        verzoek = {"model": EMBED_MODEL, "input": nieuw}
        try:
            for poging in range(3):  # soms is de server even druk: dan nog eens proberen
                r = requests.post(SERVER + "/api/embed", json=verzoek, timeout=300)
                if r.ok:
                    break
                time.sleep(2)
        except requests.ConnectionError:
            raise SystemExit("\nIk kan de geest niet bereiken. Is start.bat (of de docent-server) gestart?")
        if not r.ok:
            raise SystemExit(f"\nHet betekenis-model ({EMBED_MODEL}) doet het niet: {r.text}")
        for tekst, getallen in zip(nieuw, r.json()["embeddings"]):
            _onthouden[tekst] = getallen
    resultaat = [_onthouden[t] for t in lijst]
    return resultaat[0] if los else resultaat


def gelijkenis(getallen_a, getallen_b):
    """Cosinusgelijkenis van twee lijsten getallen: 1 = zelfde richting, 0 = niets met elkaar te maken."""
    product = sum(a * b for a, b in zip(getallen_a, getallen_b))
    lengte_a = math.sqrt(sum(a * a for a in getallen_a))
    lengte_b = math.sqrt(sum(b * b for b in getallen_b))
    return product / (lengte_a * lengte_b)


def lijkt_op(tekst_a, tekst_b):
    """Hoeveel lijken twee teksten qua betekenis op elkaar? Een getal, meestal tussen 0 en 1."""
    a, b = embed([tekst_a, tekst_b])
    return gelijkenis(a, b)


def meest_op(tekst, kandidaten):
    """Sorteert de kandidaten: de tekst die het meest op 'tekst' lijkt, komt eerst.

    Geeft een lijst met (gelijkenis, kandidaat) terug.
    """
    getallen = embed([tekst] + list(kandidaten))
    vraag_getallen = getallen[0]
    scores = [(gelijkenis(vraag_getallen, g), k) for g, k in zip(getallen[1:], kandidaten)]
    return sorted(scores, reverse=True)
