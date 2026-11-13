# De stem van de geest.
#
# Gebruik in je eigen code:
#     from stem import zeg
#     zeg("Hallo, ik ben de geest!")
#     zeg("Goeiedag!", stem="nl_BE-nathalie-medium")
#
# Welke stemmen zijn er?  print(stemmen())
#
# De stemmen komen van Piper: een klein neuraal netwerk dat tekst omzet in geluid.
# Het draait helemaal op je eigen laptop, zonder internet.

import io
import wave
from pathlib import Path

STEMMEN_MAP = Path(__file__).resolve().parent.parent / "stemmen"
STANDAARD_STEM = "nl_NL-pim-medium"

_geladen = {}


def stemmen():
    """Geeft de namen van alle stemmen die op deze laptop staan."""
    return sorted(p.stem for p in STEMMEN_MAP.glob("*.onnx"))


def _piper_zeg(tekst, stem, snelheid):
    from piper import PiperVoice, SynthesisConfig
    import winsound

    if stem not in _geladen:
        _geladen[stem] = PiperVoice.load(str(STEMMEN_MAP / (stem + ".onnx")))
    geluid = io.BytesIO()
    with wave.open(geluid, "wb") as wav:
        _geladen[stem].synthesize_wav(tekst, wav, syn_config=SynthesisConfig(length_scale=1 / snelheid))
    winsound.PlaySound(geluid.getvalue(), winsound.SND_MEMORY)


def _windows_zeg(tekst, snelheid):
    import pyttsx3

    motor = pyttsx3.init()
    motor.setProperty("rate", int(170 * snelheid))
    motor.say(tekst)
    motor.runAndWait()


def zeg(tekst, stem=STANDAARD_STEM, snelheid=1.0):
    """Spreekt de tekst uit. snelheid 1.0 is normaal, 1.5 is sneller, 0.7 is langzamer."""
    if stem in stemmen():
        try:
            _piper_zeg(tekst, stem, snelheid)
            return
        except ImportError:
            pass
    # Geen Piper of stem niet gevonden: gebruik de (meestal Engelse) Windows-stem.
    _windows_zeg(tekst, snelheid)


if __name__ == "__main__":
    print("Gevonden stemmen:", stemmen())
    for s in stemmen():
        print("Nu spreekt:", s)
        zeg("Hallo! Ik ben de geest in de fles. Wat is je wens?", stem=s)
