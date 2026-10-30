"""Étape 1 : génération du script structuré avec l'API OpenAI."""

import json

PROMPT = """Génère un script de vidéo Short virale (30 à 60 secondes) en {langue}.
Niche : {niche}
Style : {style}

Structure : HOOK percutant (3 s), CONTENU à forte valeur (20-50 s), CTA (3-5 s).
Le texte_tts est lu tel quel par une voix de synthèse : phrases courtes, pas
d'emojis, pas de didascalies, nombres écrits comme ils se prononcent.

Réponds UNIQUEMENT avec un objet JSON de cette forme :
{{
  "titre": "titre accrocheur (moins de 70 caractères)",
  "texte_tts": "texte complet de la voix off (hook + contenu + CTA)",
  "description": "description pour les réseaux sociaux",
  "hashtags": ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5"],
  "mots_cles_visuels": ["4 requêtes courtes EN ANGLAIS pour chercher des vidéos stock, une par scène"],
  "sections": [
    {{"type": "hook", "texte": "...", "visuel": "indication visuelle", "duree_estimee": 3}},
    {{"type": "contenu", "texte": "...", "visuel": "...", "duree_estimee": 25}},
    {{"type": "cta", "texte": "...", "visuel": "...", "duree_estimee": 5}}
  ]
}}"""

CHAMPS_REQUIS = ("titre", "texte_tts", "description", "hashtags", "mots_cles_visuels")


def generer_script(niche, style, config):
    from openai import OpenAI

    llm = config["llm"]
    client = OpenAI()
    reponse = client.chat.completions.create(
        model=llm["model"],
        temperature=llm["temperature"],
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "Tu es un scénariste expert en vidéos courtes virales."},
            {"role": "user", "content": PROMPT.format(niche=niche, style=style, langue=llm["langue"])},
        ],
    )
    return normaliser_script(json.loads(reponse.choices[0].message.content))


def normaliser_script(data):
    manquants = [c for c in CHAMPS_REQUIS if not data.get(c)]
    if manquants:
        raise ValueError(f"Script incomplet, champs manquants : {', '.join(manquants)}")

    hashtags = data["hashtags"]
    if isinstance(hashtags, str):
        hashtags = hashtags.split()
    data["hashtags"] = ["#" + h.lstrip("#").replace(" ", "") for h in hashtags if h.strip("# ")]

    mots_cles = data["mots_cles_visuels"]
    if isinstance(mots_cles, str):
        mots_cles = [m.strip() for m in mots_cles.split(",") if m.strip()] or [mots_cles]
    data["mots_cles_visuels"] = mots_cles
    return data
