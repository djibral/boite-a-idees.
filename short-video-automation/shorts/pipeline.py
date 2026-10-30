"""Orchestrateur : idée → script → voix → visuels → montage → sous-titres → publication."""

import json
import os
import traceback
from datetime import datetime

from . import publish
from .config import charger_config
from .montage import creer_short_complet
from .script import generer_script, normaliser_script
from .subtitles import transcrire_audio
from .visuals import generer_images_ia, telecharger_videos_stock
from .voice import generer_voix


def _titre_etape(texte):
    print("\n" + "=" * 50 + f"\n{texte}\n" + "=" * 50)


def _ecrire_json(chemin, data):
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


class ShortVideoAutomator:
    def __init__(self, config_file="config.json"):
        self.config = charger_config(config_file)

    def pipeline_complet(self, niche, style="informatif", publier=True, script_existant=None):
        """Exécute tout le pipeline et retourne un résumé (fichiers + liens publiés)."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dossier = os.path.join(self.config["dossier_sortie"], timestamp)
        os.makedirs(dossier, exist_ok=True)

        _titre_etape("📝 ÉTAPE 1 : Script")
        if script_existant:
            with open(script_existant, encoding="utf-8") as f:
                script = normaliser_script(json.load(f))
        else:
            script = generer_script(niche, style, self.config)
        _ecrire_json(os.path.join(dossier, "script.json"), script)
        print(f"Titre : {script['titre']}")

        _titre_etape("🎙️ ÉTAPE 2 : Voix")
        fichier_audio = generer_voix(script["texte_tts"], os.path.join(dossier, "voix.mp3"), self.config)

        _titre_etape("🖼️ ÉTAPE 3 : Visuels")
        nombre = self.config["visuels"]["nombre_clips"]
        if self.config["visuels"]["source"] == "ia":
            descriptions = [s.get("visuel") or s["texte"] for s in script.get("sections", [])]
            visuels = generer_images_ia(descriptions or script["mots_cles_visuels"], dossier, self.config)
        else:
            visuels = telecharger_videos_stock(script["mots_cles_visuels"], nombre, dossier, self.config)

        _titre_etape("🔤 ÉTAPE 4 : Transcription (Whisper)")
        mots = transcrire_audio(fichier_audio, self.config, texte_reference=script["texte_tts"])
        _ecrire_json(os.path.join(dossier, "mots.json"), mots)

        _titre_etape("🎬 ÉTAPE 5 : Montage")
        fichier_final = creer_short_complet(
            fichier_audio, visuels, mots, self.config,
            fichier_sortie=os.path.join(dossier, "short_final.mp4"),
        )

        resultat = {"niche": niche, "dossier": dossier, "fichier": fichier_final,
                    "titre": script["titre"], "publications": {}}
        if publier:
            _titre_etape("📤 ÉTAPE 6 : Publication")
            resultat["publications"] = self.publier(fichier_final, script)

        _ecrire_json(os.path.join(dossier, "resultat.json"), resultat)
        _titre_etape(f"🎉 PIPELINE TERMINÉ — fichiers dans {dossier}")
        return resultat

    def publier(self, fichier, script):
        """Publie sur chaque plateforme activée ; un échec n'empêche pas les autres."""
        pub = self.config["publication"]
        titre, description, hashtags = script["titre"], script["description"], script["hashtags"]
        taches = {
            "youtube": lambda: publish.publier_youtube_short(fichier, titre, description, hashtags, self.config),
            "tiktok": lambda: publish.publier_tiktok(fichier, description, hashtags, self.config),
            "instagram": lambda: publish.publier_instagram_reel(
                fichier, f"{titre}\n\n{description}\n\n{' '.join(hashtags)}", self.config),
        }
        liens = {}
        for plateforme, tache in taches.items():
            if not pub[plateforme]["enabled"]:
                continue
            try:
                liens[plateforme] = tache()
            except Exception as e:
                print(f"❌ {plateforme} : {e}")
                liens[plateforme] = f"erreur : {e}"
        return liens

    def production_en_masse(self, niches, nb_par_niche=3, style="informatif", publier=True):
        resultats = []
        for niche in niches:
            for i in range(nb_par_niche):
                print(f"\n{'🔥' * 20}\nVidéo {i + 1}/{nb_par_niche} pour « {niche} »\n{'🔥' * 20}")
                try:
                    resultats.append({**self.pipeline_complet(niche, style, publier), "status": "✅"})
                except Exception as e:
                    traceback.print_exc()
                    resultats.append({"niche": niche, "erreur": str(e), "status": "❌"})
        return resultats
