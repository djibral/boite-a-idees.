"""Test hors-ligne du montage : aucun appel API, médias générés à la volée.

    python -m pytest tests/      (ou)      python tests/test_montage.py
"""

import copy
import os
import sys
import tempfile

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from moviepy import AudioClip, ColorClip, VideoFileClip  # noqa: E402
from PIL import Image  # noqa: E402

from shorts.config import DEFAULTS  # noqa: E402
from shorts.montage import creer_short_complet  # noqa: E402
from shorts.script import normaliser_script  # noqa: E402
from shorts.subtitles import grouper_mots, rendre_groupe  # noqa: E402


def _config(dossier):
    config = copy.deepcopy(DEFAULTS)
    config["video"].update(largeur=270, hauteur=480, fps=12, preset="ultrafast", bitrate="500k")
    config["sous_titres"].update(taille=24, marge_bas=110, epaisseur_contour=2)
    config["musique"]["fichier"] = os.path.join(dossier, "musique.wav")
    return config


def _sinus(freq, duree, chemin):
    AudioClip(lambda t: np.stack([np.sin(2 * np.pi * freq * t)] * 2, axis=-1) * 0.3,
              duration=duree, fps=22050).write_audiofile(chemin, logger=None)
    return chemin


def test_short_complet():
    with tempfile.TemporaryDirectory() as dossier:
        config = _config(dossier)
        voix = _sinus(440, 4.0, os.path.join(dossier, "voix.wav"))
        _sinus(220, 1.5, config["musique"]["fichier"])  # plus courte que la voix → bouclée

        paysage = os.path.join(dossier, "paysage.mp4")
        ColorClip((640, 360), color=(200, 40, 40), duration=1.0).write_videofile(
            paysage, fps=12, logger=None)
        portrait = os.path.join(dossier, "portrait.mp4")
        ColorClip((360, 800), color=(40, 40, 200), duration=3.0).write_videofile(
            portrait, fps=12, logger=None)
        image = os.path.join(dossier, "image.png")
        Image.new("RGB", (600, 600), (40, 200, 40)).save(image)

        mots = [{"mot": m, "debut": i * 0.4, "fin": i * 0.4 + 0.35}
                for i, m in enumerate("Voici trois habitudes qui vont changer ta vie.".split())]

        sortie = creer_short_complet(voix, [paysage, portrait, image], mots, config,
                                     fichier_sortie=os.path.join(dossier, "short.mp4"))

        clip = VideoFileClip(sortie)
        assert clip.size == [270, 480]
        assert abs(clip.duration - 4.0) < 0.2
        assert clip.audio is not None
        clip.close()


def test_grouper_mots_coupe_sur_ponctuation():
    mots = [{"mot": m, "debut": 0, "fin": 0} for m in ["Salut,", "ça", "va", "bien", "aujourd'hui"]]
    assert [len(g) for g in grouper_mots(mots, 3)] == [1, 3, 1]


def test_rendu_highlight_colore_le_mot_actif():
    st = dict(DEFAULTS["sous_titres"], taille=40, epaisseur_contour=2)
    image = rendre_groupe(["UN", "DEUX"], 1, st, largeur_max=1000)
    pixels = image[image[..., 3] == 255][:, :3]
    jaunes = (pixels[:, 0] > 200) & (pixels[:, 1] > 200) & (pixels[:, 2] < 60)
    assert jaunes.any()


def test_normaliser_script():
    data = normaliser_script({"titre": "t", "texte_tts": "x", "description": "d",
                              "hashtags": "productivite #focus", "mots_cles_visuels": "desk, coffee"})
    assert data["hashtags"] == ["#productivite", "#focus"]
    assert data["mots_cles_visuels"] == ["desk", "coffee"]


if __name__ == "__main__":
    for nom, fonction in list(globals().items()):
        if nom.startswith("test_"):
            fonction()
            print(f"✅ {nom}")
