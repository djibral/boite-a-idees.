"""Chargement de la configuration (config.json + variables d'environnement)."""

import copy
import json
import os

DEFAULTS = {
    "dossier_sortie": "output",
    "llm": {
        "model": "gpt-4o-mini",
        "temperature": 0.8,
        "langue": "français",
    },
    "voix": {
        "provider": "elevenlabs",  # "elevenlabs" ou "google"
        "voice_id": "21m00Tcm4TlvDq8ikWAM",
        "model_id": "eleven_multilingual_v2",
        "vitesse": 1.1,
        "google_voice": "fr-FR-Neural2-A",
        "google_langue": "fr-FR",
    },
    "visuels": {
        "source": "pexels",  # "pexels" ou "ia"
        "nombre_clips": 4,
        "image_model": "dall-e-3",
    },
    "video": {
        "largeur": 1080,
        "hauteur": 1920,
        "fps": 30,
        "bitrate": "8000k",
        "preset": "medium",
    },
    "sous_titres": {
        "mode": "highlight",  # "highlight" (mot actif coloré) ou "groupe"
        "whisper_model": "small",
        "langue": "fr",
        "mots_par_groupe": 3,
        "police": None,  # chemin vers un .ttf ; None = détection automatique
        "taille": 80,
        "couleur": "white",
        "couleur_highlight": "yellow",
        "contour": "black",
        "epaisseur_contour": 6,
        "marge_bas": 450,
        "majuscules": True,
    },
    "musique": {
        "fichier": "assets/musique_ambient.mp3",
        "volume": 0.1,
    },
    "publication": {
        "youtube": {
            "enabled": False,
            "privacy": "private",
            "category_id": "22",
            "contenu_synthetique": True,
            "client_secrets": "client_secret.json",
            "token": "youtube_token.json",
        },
        "tiktok": {"enabled": False, "cookies": "tiktok_cookies.txt"},
        "instagram": {"enabled": False},
    },
    "planification": {
        "heures": ["10:00", "18:00"],
        "style": "motivant et percutant",
        "niches": [
            "productivité", "finance personnelle", "psychologie",
            "motivation", "santé", "technologie",
        ],
    },
}

# Les clés secrètes ne vivent jamais dans le code : variables d'environnement
# (ou fichier .env), avec repli sur config.json.
SECRETS = {
    "openai_api_key": "OPENAI_API_KEY",
    "elevenlabs_api_key": "ELEVENLABS_API_KEY",
    "pexels_api_key": "PEXELS_API_KEY",
    "instagram_username": "INSTAGRAM_USERNAME",
    "instagram_password": "INSTAGRAM_PASSWORD",
}


def _fusionner(base, ajout):
    for cle, valeur in ajout.items():
        if isinstance(valeur, dict) and isinstance(base.get(cle), dict):
            _fusionner(base[cle], valeur)
        else:
            base[cle] = valeur
    return base


def charger_config(chemin="config.json"):
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    config = copy.deepcopy(DEFAULTS)
    if chemin and os.path.exists(chemin):
        with open(chemin, encoding="utf-8") as f:
            _fusionner(config, json.load(f))

    for cle, env in SECRETS.items():
        config[cle] = os.environ.get(env) or config.get(cle)
    if config.get("openai_api_key"):
        os.environ.setdefault("OPENAI_API_KEY", config["openai_api_key"])
    return config


def secret(config, cle):
    valeur = config.get(cle)
    if not valeur:
        raise RuntimeError(
            f"Clé manquante : définis la variable d'environnement {SECRETS[cle]} "
            f"(ou '{cle}' dans config.json)."
        )
    return valeur
