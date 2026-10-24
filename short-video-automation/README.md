# 🎬 Automate de vidéos Shorts — de l'idée à la publication

```
IDÉE → SCRIPT → VOIX → VISUELS → TRANSCRIPTION → MONTAGE + SOUS-TITRES → EXPORT → PUBLICATION
       OpenAI   ElevenLabs Pexels   Whisper         MoviePy 2 + Pillow    MP4 9:16  YouTube / TikTok / Instagram
                / Google   / IA
```

Une commande produit un short vertical 1080×1920 avec voix off, B-roll,
musique de fond et sous-titres animés (mot actif surligné, style Hormozi),
puis le publie sur les plateformes activées.

## Installation

```bash
cd short-video-automation
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# ffmpeg doit être installé (apt install ffmpeg / brew install ffmpeg)

cp .env.example .env                # puis colle tes clés API
cp config.example.json config.json  # puis ajuste les réglages
```

Clés nécessaires : `OPENAI_API_KEY` (script + Whisper local, gratuit),
`ELEVENLABS_API_KEY` (ou Google TTS), `PEXELS_API_KEY` (gratuit). Les clés
restent dans `.env`, qui est ignoré par git.

Musique de fond : dépose un fichier libre de droits dans
`assets/musique_ambient.mp3` (ignoré s'il est absent ; bouclé s'il est trop court).

## Utilisation

```bash
# Un short, sans publier (recommandé pour commencer)
python -m shorts run --niche "productivité et habitudes" --style "motivant et percutant" --no-publish

# Refaire le montage à partir d'un script déjà généré (pas d'appel au LLM)
python -m shorts run --niche productivité --script output/20261024_101500/script.json --no-publish

# Production en masse
python -m shorts batch --niches "finance personnelle" productivité psychologie --nombre 5

# Publication automatique chaque jour aux heures de config.json (10:00 et 18:00 par défaut)
nohup python -m shorts schedule > scheduler.log 2>&1 &
```

Chaque exécution crée `output/<horodatage>/` avec `script.json`, `voix.mp3`,
les clips, `mots.json` (timestamps Whisper), `short_final.mp4` et
`resultat.json` (liens publiés).

En crontab plutôt qu'un processus permanent :

```
0 10,18 * * * cd /chemin/short-video-automation && .venv/bin/python -m shorts run --niche productivité
```

## Publication

| Plateforme | Méthode | Mise en place |
|---|---|---|
| YouTube Shorts | API officielle YouTube Data v3 | Crée un client OAuth « Application de bureau » dans Google Cloud, télécharge-le en `client_secret.json`, puis `python -m shorts auth-youtube` une fois. Mets `publication.youtube.enabled` à `true`. |
| TikTok | `tiktok-uploader` (non officiel) | `pip install tiktok-uploader`, exporte tes cookies dans `tiktok_cookies.txt`. |
| Instagram Reels | `instagrapi` (non officiel) | `pip install instagrapi`, `INSTAGRAM_USERNAME` / `INSTAGRAM_PASSWORD` dans `.env`. |

⚠️ TikTok et Instagram passent par des bibliothèques non officielles qui
enfreignent leurs conditions d'utilisation : risque de blocage du compte.
Pour un usage durable, préfère les API officielles (TikTok Content Posting
API, Instagram Graph API) ou un outil comme Buffer / Metricool / Publer.
Par défaut, YouTube publie en **privé** (`privacy`) et déclare le contenu
synthétique (`contenu_synthetique`), comme YouTube le demande pour les voix IA
réalistes.

## Réglages utiles (`config.json`)

- `voix.provider` : `elevenlabs` ou `google` ; `voix.vitesse` : 1.1 = un peu plus rapide.
- `visuels.source` : `pexels` (vidéos stock, une requête par scène) ou `ia` (images générées, avec zoom lent).
- `sous_titres.mode` : `highlight` (mot actif en couleur) ou `groupe` ; `whisper_model` : `small` (rapide) à `large` (précis) ; `police` : chemin d'un `.ttf` (sinon DejaVu/Liberation/Arial détectée).
- `llm.model` : n'importe quel modèle de chat OpenAI compatible JSON.

## Tests

```bash
python -m pytest tests/   # ou : python tests/test_montage.py
```

Le test monte un vrai short (petite résolution) avec des médias générés :
aucune clé API requise.

## Ce qui a été corrigé par rapport au guide d'origine

- SDK OpenAI ≥ 1.0 (`client.chat.completions.create`) au lieu de `openai.ChatCompletion`, et réponse en mode JSON garanti.
- MoviePy 2 (`subclipped`, `cropped`, `with_*`, effets `vfx`/`afx`) : le code du guide ne fonctionne plus avec la version actuelle.
- Sous-titres dessinés avec Pillow : plus besoin d'ImageMagick, et le mot actif est **vraiment** surligné (le guide créait le clip du mot sans jamais l'afficher).
- Pexels : choix du rendu le plus proche de 1920 px (le guide prenait le premier fichier, souvent en basse définition), téléchargement en flux, plusieurs requêtes pour varier les scènes.
- Musique bouclée si plus courte que la voix (le guide plantait), fondu de fin.
- Erreurs d'API remontées clairement ; l'échec d'une plateforme n'empêche pas les autres.
- Le planificateur reprend la rotation des niches après un redémarrage.

## Coûts mensuels indicatifs

| Service | Coût / mois | Volume |
|---|---|---|
| OpenAI (script) | quelques € | centaines de scripts |
| ElevenLabs | 5 – 22 € | 30 – 100 voix |
| Pexels, Whisper (local) | gratuit | illimité |
| Serveur VPS | 5 – 10 € | — |
