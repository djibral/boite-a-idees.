"""Interface en ligne de commande : python -m shorts <commande>."""

import argparse
import json
import os
import time


def _automator(args):
    from .pipeline import ShortVideoAutomator
    return ShortVideoAutomator(args.config)


def cmd_run(args):
    _automator(args).pipeline_complet(
        args.niche, args.style, publier=not args.no_publish, script_existant=args.script)


def cmd_batch(args):
    resultats = _automator(args).production_en_masse(
        args.niches, args.nombre, args.style, publier=not args.no_publish)
    for r in resultats:
        print(r["status"], r["niche"], r.get("fichier") or r.get("erreur"))


def cmd_schedule(args):
    import schedule

    automator = _automator(args)
    plan = automator.config["planification"]
    niches = plan["niches"]
    # L'index de rotation est persisté pour survivre aux redémarrages.
    fichier_etat = os.path.join(automator.config["dossier_sortie"], "planification_etat.json")
    os.makedirs(automator.config["dossier_sortie"], exist_ok=True)

    def job():
        etat = {"index": 0}
        if os.path.exists(fichier_etat):
            with open(fichier_etat, encoding="utf-8") as f:
                etat = json.load(f)
        niche = niches[etat["index"] % len(niches)]
        print(f"⏰ Publication automatique : {niche}")
        try:
            automator.pipeline_complet(niche, plan["style"], publier=not args.no_publish)
        except Exception as e:
            print(f"❌ Échec du job planifié : {e}")
        etat["index"] += 1
        with open(fichier_etat, "w", encoding="utf-8") as f:
            json.dump(etat, f)

    for heure in plan["heures"]:
        schedule.every().day.at(heure).do(job)
    print(f"🤖 Planificateur démarré ({', '.join(plan['heures'])}). Ctrl+C pour arrêter.")
    while True:
        schedule.run_pending()
        time.sleep(30)


def cmd_auth_youtube(args):
    from .config import charger_config
    from .publish import autoriser_youtube

    autoriser_youtube(charger_config(args.config))
    print("✅ Jeton YouTube enregistré.")


def main():
    parser = argparse.ArgumentParser(prog="shorts", description="🎬 Automate de vidéos Shorts de A à Z")
    parser.add_argument("--config", default="config.json", help="fichier de configuration")
    sub = parser.add_subparsers(dest="commande", required=True)

    p = sub.add_parser("run", help="créer (et publier) un short")
    p.add_argument("--niche", required=True)
    p.add_argument("--style", default="informatif")
    p.add_argument("--script", help="réutiliser un script.json existant au lieu d'appeler le LLM")
    p.add_argument("--no-publish", action="store_true", help="créer la vidéo sans la publier")
    p.set_defaults(func=cmd_run)

    p = sub.add_parser("batch", help="production en masse")
    p.add_argument("--niches", nargs="+", required=True)
    p.add_argument("--nombre", type=int, default=3, help="shorts par niche")
    p.add_argument("--style", default="informatif")
    p.add_argument("--no-publish", action="store_true")
    p.set_defaults(func=cmd_batch)

    p = sub.add_parser("schedule", help="publier automatiquement aux heures de config.json")
    p.add_argument("--no-publish", action="store_true")
    p.set_defaults(func=cmd_schedule)

    p = sub.add_parser("auth-youtube", help="autoriser l'accès YouTube (une seule fois)")
    p.set_defaults(func=cmd_auth_youtube)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
