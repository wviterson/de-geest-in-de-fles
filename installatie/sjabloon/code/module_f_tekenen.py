# MODULE F – AI die tekent
#
# Een tekenende AI begint NIET met een leeg wit vel, maar met RUIS:
# een plaatje vol willekeurige gekleurde puntjes, zoals sneeuw op een oude tv.
# Bij elke STAP haalt het model een beetje ruis weg. Jouw WENS (de prompt)
# vertelt hem welke kant hij op moet: "zie je daar een vos in? Maak hem duidelijker!"
# Dit heet DIFFUSIE: van ruis naar beeld.
#
# Alles draait op deze laptop, zonder internet. Het model (LCM Dreamshaper)
# heeft het tekenen geleerd van miljoenen plaatjes met een beschrijving erbij.
# Het verstaat vooral ENGELS, dus schrijf je wens in het Engels.
#
# Druk op F5. Het laden duurt de eerste keer even (10 tot 30 seconden).
# Je plaatjes komen in de map "tekeningen" naast dit bestand.

import os
import random
import struct
import sys
import time
import zlib
from pathlib import Path

WENS = "a happy cartoon fox in a forest, colorful"   # TODO 1: verzin je eigen wens
STAPPEN = 4          # TODO 2: probeer 1, 2, 4 en 8. Wat zie je? Hoe lang duurt het?
SEED = 42            # TODO 3: zelfde seed = zelfde plaatje? Probeer 42 twee keer, dan 43.
                     #         (Net als de dobbelsteen in level 2.)
                     #         Zet SEED = None voor elke keer een nieuwe dobbelsteenworp.
KIJK_MEE = False     # TODO 4: zet op True en kijk hoe het plaatje uit de ruis komt.
                     #         (Dat duurt wel wat langer.)

# Een heel simpel filter (zoals je dat in level 4 kon bouwen). Begeleiders kijken ook mee.
VERBODEN = ["naked", "nude", "naakt", "sexy", "blood", "bloed", "gore", "dead", "dood"]

# Waar staan de tekenmotor en de plaatjes?
CODE_MAP = Path(__file__).resolve().parent
TEKENEN_MAP = CODE_MAP.parent / "tekenen"
TEKENINGEN_MAP = CODE_MAP / "tekeningen"
GROOTTE = 512        # pixels breed en hoog


def vrij_geheugen():
    """Hoeveel werkgeheugen (GB) is er nog vrij op deze laptop?"""
    import ctypes

    class Status(ctypes.Structure):
        _fields_ = [("lengte", ctypes.c_ulong), ("bezet", ctypes.c_ulong),
                    ("totaal", ctypes.c_ulonglong), ("vrij", ctypes.c_ulonglong),
                    ("rest", ctypes.c_ulonglong * 5)]
    status = Status()
    status.lengte = ctypes.sizeof(Status)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status))
    return status.vrij / 1024 ** 3


def laad_tekenmotor():
    """Laadt het tekenmodel. Dat duurt even, dus we doen het maar één keer."""
    if not (TEKENEN_MAP / "model" / "unet").exists():
        print("De tekenmotor is niet geïnstalleerd op deze laptop.")
        print("Vraag het aan je begeleider, of kijk mee op het grote scherm.")
        print("(Docent: installatie\\installeer-tekenen.bat)")
        sys.exit()
    if vrij_geheugen() < 4:
        print(f"Let op: er is maar {vrij_geheugen():.1f} GB werkgeheugen vrij. Tekenen heeft")
        print("ongeveer 5 GB nodig. Sluit andere programma's (en de geest: stop.bat),")
        print("anders wordt het heel traag.")
    sys.path.insert(0, str(TEKENEN_MAP / "pakketten"))
    import openvino_genai
    pijplijn = openvino_genai.Text2ImagePipeline(str(TEKENEN_MAP / "model"))
    instellingen = pijplijn.get_generation_config()
    pijplijn.reshape(1, GROOTTE, GROOTTE, instellingen.guidance_scale)
    pijplijn.compile("CPU", CACHE_DIR=str(TEKENEN_MAP / "cache"))
    return pijplijn


def teken(pijplijn, wens, stappen=4, seed=42, tussenstappen=None):
    """Tekent één plaatje en geeft de pixels terug (rood, groen, blauw, rood, ...).
    Geef je een lijst mee als tussenstappen, dan stopt hij daar na elke stap
    in wat hij op dat moment denkt dat het plaatje wordt."""
    tussenstanden = []

    def na_elke_stap(stap, aantal, tussenstand):
        if tussenstappen is not None:
            tussenstanden.append(tussenstand.data.copy())    # even bewaren, straks bekijken
        return False    # False = niet stoppen, gewoon doorgaan
    plaatje = pijplijn.generate(wens, num_inference_steps=stappen, rng_seed=seed,
                                callback=na_elke_stap)
    pixels = bytes(plaatje.data)    # meteen kopiëren: de tekenmotor hergebruikt zijn geheugen
    if tussenstappen is not None:
        import openvino
        for stand in tussenstanden:
            tussenstappen.append(bytes(pijplijn.decode(openvino.Tensor(stand)).data))
    return pixels


def ruis(pijplijn):
    """Zo begint de AI: alleen maar willekeurige getallen (ruis), als plaatje."""
    import numpy
    import openvino
    getallen = numpy.random.default_rng().standard_normal((1, 4, GROOTTE // 8, GROOTTE // 8))
    return bytes(pijplijn.decode(openvino.Tensor(getallen.astype(numpy.float32))).data)

def bewaar(plaatje, naam, breedte=GROOTTE, hoogte=GROOTTE):
    """Slaat een plaatje op als PNG-bestand en geeft het pad terug."""
    TEKENINGEN_MAP.mkdir(exist_ok=True)
    rij = breedte * 3
    regels = b"".join(b"\x00" + plaatje[y * rij:(y + 1) * rij] for y in range(hoogte))

    def blok(soort, data):
        controle = zlib.crc32(soort + data) & 0xFFFFFFFF
        return struct.pack(">I", len(data)) + soort + data + struct.pack(">I", controle)

    kop = struct.pack(">IIBBBBB", breedte, hoogte, 8, 2, 0, 0, 0)
    pad = TEKENINGEN_MAP / f"{naam}.png"
    pad.write_bytes(b"\x89PNG\r\n\x1a\n" + blok(b"IHDR", kop)
                    + blok(b"IDAT", zlib.compress(regels, 6)) + blok(b"IEND", b""))
    return pad


def strook(plaatjes):
    """Zet plaatjes op een rij (op halve grootte), zodat je ze kunt vergelijken."""
    half = GROOTTE // 2
    rijen = []
    for y in range(half):
        rij = b""
        for plaatje in plaatjes:
            begin = (y * 2) * GROOTTE * 3
            regel = plaatje[begin:begin + GROOTTE * 3]
            rij += b"".join(regel[x * 6:x * 6 + 3] for x in range(half))
        rijen.append(rij)
    return b"".join(rijen), half * len(plaatjes), half


def bestandsnaam(wens, seed):
    """Maakt een nette bestandsnaam van de wens."""
    letters = "".join(t if t.isalnum() else "_" for t in wens.lower())[:40].strip("_")
    return f"{letters}_seed{seed}_{time.strftime('%H%M%S')}"


def toegestaan(wens):
    """Kijkt of er een verboden woord in de wens staat (alleen hele woorden)."""
    woorden = "".join(t if t.isalnum() else " " for t in wens.lower()).split()
    for woord in VERBODEN:
        if woord in woorden:
            print(f"Die wens teken ik niet (\"{woord}\"). Verzin iets anders.")
            return False
    return True


def maak_plaatje(pijplijn, wens):
    """Tekent de wens met de instellingen van bovenaan, bewaart en opent het plaatje."""
    seed = SEED if SEED is not None else random.randrange(1_000_000)
    tussenstappen = [] if KIJK_MEE else None
    print(f"Ik teken: \"{wens}\" ({STAPPEN} stappen, seed {seed})...")
    begin = time.time()
    plaatje = teken(pijplijn, wens, STAPPEN, seed, tussenstappen)
    print(f"Klaar in {time.time() - begin:.1f} seconden.")
    naam = bestandsnaam(wens, seed)
    pad = bewaar(plaatje, naam)
    print(f"Opgeslagen: tekeningen\\{pad.name}")
    if KIJK_MEE:
        pixels, breedte, hoogte = strook([ruis(pijplijn)] + tussenstappen)
        pad = bewaar(pixels, naam + "_stappen", breedte, hoogte)
        print("Van links naar rechts: de ruis waarmee hij begon, en na elke stap")
        print("wat de AI denkt dat het plaatje wordt. De laatste is het eindplaatje.")
    os.startfile(pad)


if __name__ == "__main__":
    print("De tekenende geest wordt wakker...")
    pijplijn = laad_tekenmotor()
    print("Klaar! Typ een wens in het Engels, of druk op Enter voor de WENS uit de code.")
    print("Typ 'stop' om te stoppen.\n")
    while True:
        wens = input("Wat zal ik tekenen? ").strip()
        if wens.lower() == "stop":
            break
        if wens == "":
            wens = WENS
        if toegestaan(wens):
            maak_plaatje(pijplijn, wens)
        print()

# ---------------------------------------------------------------------------
# PLUS 1 – Varianten
#   Teken drie keer dezelfde wens met dezelfde seed, maar zet er telkens een
#   stijlwoord achter: ", watercolor painting", ", pixel art", ", photo".
#   Wat verandert er? Wat blijft hetzelfde?
#
# PLUS 2 – Nederlands of Engels?
#   Probeer "een rode vos in een bos" en daarna "a red fox in a forest".
#   Welke lukt beter? Waarom denk je dat dat zo is?
#
# PLUS 3 – Teken een dokter
#   Typ "a doctor" en zet SEED = None. Maak er 6. Typ dan "a nurse" (verpleegkundige).
#   Wie tekent de AI? Mannen of vrouwen? Jong of oud? Welke huidskleur?
#   Schrijf op wat je ziet. Waar komt dat vandaan?
#
# EXPERT 1 – De geest vertaalt
#   Laat Fietje je Nederlandse wens eerst naar het Engels vertalen. Zet dit in
#   maak_plaatje(), vóór de regel met print(f"Ik teken: ...":
#       from fles import vraag_een_keer
#       wens = vraag_een_keer("Vertaal naar het Engels. Geef alleen de vertaling.", wens,
#                             temperatuur=0, toon=False).strip()
#   Dit werkt alleen als de geest ook draait. Vertaalt Fietje goed?
#
# EXPERT 2 – Tijd meten
#   Maak een lijst met de tijd voor 1, 2, 4 en 8 stappen. Hoeveel langer duurt
#   elke extra stap? Is 8 stappen ook mooier dan 4?
