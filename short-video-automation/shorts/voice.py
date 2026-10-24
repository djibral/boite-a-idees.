"""Étape 2 : synthèse vocale (ElevenLabs ou Google Cloud TTS)."""

import requests

from .config import secret


def generer_voix(texte, fichier_sortie, config):
    provider = config["voix"]["provider"]
    if provider == "elevenlabs":
        return voix_elevenlabs(texte, fichier_sortie, config)
    if provider == "google":
        return voix_google(texte, fichier_sortie, config)
    raise ValueError(f"Fournisseur de voix inconnu : {provider}")


def voix_elevenlabs(texte, fichier_sortie, config):
    voix = config["voix"]
    reponse = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voix['voice_id']}",
        headers={"xi-api-key": secret(config, "elevenlabs_api_key"), "Accept": "audio/mpeg"},
        json={
            "text": texte,
            "model_id": voix["model_id"],
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75,
                "speed": voix["vitesse"],
            },
        },
        timeout=120,
    )
    if not reponse.ok:
        raise RuntimeError(f"ElevenLabs {reponse.status_code} : {reponse.text[:300]}")
    with open(fichier_sortie, "wb") as f:
        f.write(reponse.content)
    return fichier_sortie


def voix_google(texte, fichier_sortie, config):
    # Authentification via GOOGLE_APPLICATION_CREDENTIALS (compte de service).
    from google.cloud import texttospeech

    voix = config["voix"]
    client = texttospeech.TextToSpeechClient()
    reponse = client.synthesize_speech(
        input=texttospeech.SynthesisInput(text=texte),
        voice=texttospeech.VoiceSelectionParams(
            language_code=voix["google_langue"], name=voix["google_voice"]
        ),
        audio_config=texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=voix["vitesse"],
        ),
    )
    with open(fichier_sortie, "wb") as f:
        f.write(reponse.audio_content)
    return fichier_sortie
