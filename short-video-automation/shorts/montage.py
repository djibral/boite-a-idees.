"""Étapes 4 et 6 : montage vertical 9:16 et assemblage final (MoviePy 2)."""

import os

from moviepy import (
    AudioFileClip, CompositeAudioClip, CompositeVideoClip, ImageClip,
    VideoFileClip, afx, concatenate_videoclips, vfx,
)

from .subtitles import creer_sous_titres

EXTENSIONS_IMAGE = (".png", ".jpg", ".jpeg", ".webp")


def recadrer_portrait(clip, largeur, hauteur):
    """Convertit n'importe quel clip au format cible (9:16) en recadrant au centre."""
    w, h = clip.size
    ratio_cible = largeur / hauteur
    if w / h > ratio_cible:  # trop large → on coupe les côtés
        clip = clip.cropped(x_center=w / 2, width=int(h * ratio_cible), height=h)
    elif w / h < ratio_cible:  # trop haut → on coupe haut et bas
        clip = clip.cropped(y_center=h / 2, width=w, height=int(w / ratio_cible))
    return clip.resized((largeur, hauteur))


def preparer_clip(fichier, duree, largeur, hauteur):
    """Charge une vidéo (bouclée/coupée) ou une image (zoom lent) à la bonne durée."""
    if fichier.lower().endswith(EXTENSIONS_IMAGE):
        image = recadrer_portrait(ImageClip(fichier).with_duration(duree), largeur, hauteur)
        zoom = image.resized(lambda t: 1 + 0.08 * t / duree)  # effet Ken Burns
        return CompositeVideoClip([zoom.with_position("center")], size=(largeur, hauteur)).with_duration(duree)

    clip = VideoFileClip(fichier, audio=False)
    if clip.duration < duree:
        clip = clip.with_effects([vfx.Loop(duration=duree)])
    else:
        clip = clip.subclipped(0, duree)
    return recadrer_portrait(clip, largeur, hauteur)


def assembler_clips(fichiers, duree_totale, largeur, hauteur):
    duree = duree_totale / len(fichiers)
    clips = [preparer_clip(f, duree, largeur, hauteur) for f in fichiers]
    return concatenate_videoclips(clips).with_duration(duree_totale)


def preparer_audio(fichier_voix, musique_fond, volume_musique):
    voix = AudioFileClip(fichier_voix)
    if not musique_fond or not os.path.exists(musique_fond):
        return voix
    musique = AudioFileClip(musique_fond).with_effects([
        afx.AudioLoop(duration=voix.duration),  # boucle si la musique est trop courte
        afx.MultiplyVolume(volume_musique),
        afx.AudioFadeOut(1.0),
    ])
    return CompositeAudioClip([voix, musique]).with_duration(voix.duration)


def creer_short_complet(fichier_audio, fichiers_visuels, mots, config,
                        fichier_sortie="short_final.mp4"):
    """Assemble visuels + voix + musique + sous-titres et exporte le MP4."""
    video_cfg = config["video"]
    largeur, hauteur = video_cfg["largeur"], video_cfg["hauteur"]

    audio = preparer_audio(fichier_audio, config["musique"].get("fichier"), config["musique"]["volume"])
    duree = audio.duration

    print("🎬 Préparation des clips vidéo...")
    base = assembler_clips(fichiers_visuels, duree, largeur, hauteur)

    print("📝 Création des sous-titres...")
    sous_titres = creer_sous_titres(mots, config, duree_max=duree)

    video = (CompositeVideoClip([base] + sous_titres, size=(largeur, hauteur))
             .with_duration(duree)
             .with_audio(audio))

    print("💾 Export de la vidéo...")
    dossier = os.path.dirname(os.path.abspath(fichier_sortie))
    video.write_videofile(
        fichier_sortie,
        fps=video_cfg["fps"],
        codec="libx264",
        audio_codec="aac",
        preset=video_cfg["preset"],
        bitrate=video_cfg["bitrate"],
        threads=os.cpu_count(),
        temp_audiofile=os.path.join(dossier, "temp_audio.m4a"),
        ffmpeg_params=["-pix_fmt", "yuv420p", "-movflags", "+faststart"],
        logger="bar",
    )
    video.close()
    audio.close()
    print(f"✅ Short créé : {fichier_sortie}")
    return fichier_sortie
