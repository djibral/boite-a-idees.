"""Étape 3 : récupération des visuels (vidéos Pexels ou images IA)."""

import os

import requests

from .config import secret


def _meilleur_fichier(video, hauteur_cible):
    """Choisit le rendu le plus proche de la résolution cible (et pas le premier venu)."""
    fichiers = [f for f in video["video_files"] if f.get("height") and f.get("link")]
    if not fichiers:
        return None
    portrait = [f for f in fichiers if f["height"] >= f["width"]] or fichiers
    assez_grands = [f for f in portrait if f["height"] >= hauteur_cible * 2 / 3]
    if assez_grands:
        return min(assez_grands, key=lambda f: abs(f["height"] - hauteur_cible))["link"]
    return max(portrait, key=lambda f: f["height"])["link"]


def _telecharger(url, chemin):
    with requests.get(url, stream=True, timeout=120) as r:
        r.raise_for_status()
        with open(chemin, "wb") as f:
            for bloc in r.iter_content(chunk_size=1 << 20):
                f.write(bloc)
    return chemin


def telecharger_videos_stock(requetes, nombre, dossier, config):
    """Télécharge `nombre` vidéos portrait, en alternant entre les requêtes (une par scène)."""
    headers = {"Authorization": secret(config, "pexels_api_key")}
    hauteur = config["video"]["hauteur"]
    if isinstance(requetes, str):
        requetes = [requetes]

    candidats = []
    for requete in requetes:
        r = requests.get(
            "https://api.pexels.com/videos/search",
            headers=headers,
            params={"query": requete, "per_page": max(nombre, 5), "orientation": "portrait"},
            timeout=30,
        )
        r.raise_for_status()
        candidats.append(r.json().get("videos", []))

    choisis, deja_vus = [], set()
    rang = 0
    while len(choisis) < nombre and any(rang < len(c) for c in candidats):
        for videos in candidats:
            if rang < len(videos) and len(choisis) < nombre:
                video = videos[rang]
                lien = _meilleur_fichier(video, hauteur)
                if lien and video["id"] not in deja_vus:
                    deja_vus.add(video["id"])
                    choisis.append(lien)
        rang += 1

    if not choisis:
        raise RuntimeError(f"Aucune vidéo Pexels trouvée pour : {requetes}")

    return [
        _telecharger(lien, os.path.join(dossier, f"stock_{i}.mp4"))
        for i, lien in enumerate(choisis)
    ]


def generer_images_ia(descriptions, dossier, config):
    """Génère une image verticale par description avec l'API d'images OpenAI."""
    import base64

    from openai import OpenAI

    client = OpenAI()
    modele = config["visuels"]["image_model"]
    fichiers = []
    for i, description in enumerate(descriptions):
        reponse = client.images.generate(
            model=modele,
            prompt=f"{description}. Vertical 9:16 composition, cinematic, no text.",
            size="1024x1792" if modele == "dall-e-3" else "1024x1536",
            n=1,
        )
        image = reponse.data[0]
        chemin = os.path.join(dossier, f"image_{i}.png")
        if image.url:
            _telecharger(image.url, chemin)
        else:  # les modèles gpt-image renvoient l'image en base64
            with open(chemin, "wb") as f:
                f.write(base64.b64decode(image.b64_json))
        fichiers.append(chemin)
    return fichiers
