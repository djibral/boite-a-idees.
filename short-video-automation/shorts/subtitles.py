"""Étape 5 : transcription Whisper et sous-titres animés (style TikTok / Hormozi).

Les sous-titres sont dessinés avec Pillow plutôt qu'avec TextClip : pas besoin
d'ImageMagick, et on peut colorer le mot actif à l'intérieur de la phrase.
"""

import os

import numpy as np
from PIL import Image, ImageDraw, ImageFont

POLICES_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
]
PONCTUATION_FIN = (".", "!", "?", ",", ";", ":", "…")


def transcrire_audio(fichier_audio, config, texte_reference=None):
    """Retourne la liste des mots avec leurs timestamps : [{mot, debut, fin}, ...]."""
    import whisper

    st = config["sous_titres"]
    modele = whisper.load_model(st["whisper_model"])
    resultat = modele.transcribe(
        fichier_audio,
        language=st["langue"],
        word_timestamps=True,
        # Le script connu aide Whisper à orthographier correctement les mots.
        initial_prompt=texte_reference,
    )
    return [
        {"mot": w["word"].strip(), "debut": w["start"], "fin": w["end"]}
        for segment in resultat["segments"]
        for w in segment.get("words", [])
        if w["word"].strip()
    ]


def grouper_mots(mots, mots_par_groupe=3):
    """Regroupe les mots par paquets, en coupant aussi sur la ponctuation."""
    groupes, courant = [], []
    for mot in mots:
        courant.append(mot)
        if len(courant) >= mots_par_groupe or mot["mot"].endswith(PONCTUATION_FIN):
            groupes.append(courant)
            courant = []
    if courant:
        groupes.append(courant)
    return groupes


def _police(st):
    chemin = st.get("police")
    if chemin:
        return ImageFont.truetype(chemin, st["taille"])
    for candidat in POLICES_CANDIDATES:
        if os.path.exists(candidat):
            return ImageFont.truetype(candidat, st["taille"])
    return ImageFont.load_default(size=st["taille"])


def rendre_groupe(textes, index_actif, st, largeur_max, police=None):
    """Dessine un groupe de mots (avec retour à la ligne) → tableau RGBA."""
    police = police or _police(st)
    contour = st["epaisseur_contour"]
    espace = police.getlength(" ")
    hauteur_ligne = int(st["taille"] * 1.2)

    lignes, ligne, largeur = [], [], 0.0
    for i, texte in enumerate(textes):
        w = police.getlength(texte)
        if ligne and largeur + espace + w > largeur_max:
            lignes.append((ligne, largeur))
            ligne, largeur = [], 0.0
        largeur += (espace if ligne else 0) + w
        ligne.append((i, texte, w))
    lignes.append((ligne, largeur))

    marge = contour * 2
    img_w = int(min(largeur_max, max(l for _, l in lignes))) + 2 * marge
    img_h = hauteur_ligne * len(lignes) + 2 * marge
    image = Image.new("RGBA", (img_w, img_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    y = marge
    for ligne, largeur in lignes:
        x = marge + (img_w - 2 * marge - largeur) / 2
        for i, texte, w in ligne:
            couleur = st["couleur_highlight"] if i == index_actif else st["couleur"]
            draw.text((x, y), texte, font=police, fill=couleur,
                      stroke_width=contour, stroke_fill=st["contour"])
            x += w + espace
        y += hauteur_ligne
    return np.array(image)


def creer_sous_titres(mots, config, duree_max=None):
    """Construit les ImageClip de sous-titres à superposer à la vidéo."""
    from moviepy import ImageClip

    st = config["sous_titres"]
    largeur = config["video"]["largeur"]
    hauteur = config["video"]["hauteur"]
    police = _police(st)
    largeur_max = largeur - 120
    centre_y = hauteur - st["marge_bas"]

    def texte(m):
        return m["mot"].upper() if st.get("majuscules", True) else m["mot"]

    groupes = grouper_mots(mots, st["mots_par_groupe"])
    clips = []
    for g, groupe in enumerate(groupes):
        textes = [texte(m) for m in groupe]
        # Le groupe reste affiché jusqu'au suivant pour éviter le clignotement.
        fin_groupe = groupes[g + 1][0]["debut"] if g + 1 < len(groupes) else groupe[-1]["fin"]
        if duree_max is not None:
            fin_groupe = min(fin_groupe, duree_max)

        if st["mode"] == "highlight":
            segments = []
            for j, mot in enumerate(groupe):
                fin = groupe[j + 1]["debut"] if j + 1 < len(groupe) else fin_groupe
                segments.append((j, mot["debut"], fin))
        else:
            segments = [(None, groupe[0]["debut"], fin_groupe)]

        for index_actif, debut, fin in segments:
            if fin - debut <= 0.01:
                continue
            image = rendre_groupe(textes, index_actif, st, largeur_max, police)
            y = int(centre_y - image.shape[0] / 2)
            clips.append(
                ImageClip(image)
                .with_start(debut)
                .with_duration(fin - debut)
                .with_position(("center", y))
            )
    return clips
