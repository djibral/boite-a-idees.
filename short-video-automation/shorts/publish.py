"""Étape 7 : publication YouTube Shorts (API officielle), TikTok et Instagram (optionnels)."""

import os

from .config import secret

YOUTUBE_SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]


def autoriser_youtube(config):
    """Ouvre le navigateur une fois pour créer youtube_token.json (OAuth)."""
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow

    yt = config["publication"]["youtube"]
    creds = None
    if os.path.exists(yt["token"]):
        creds = Credentials.from_authorized_user_file(yt["token"], YOUTUBE_SCOPES)
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    elif not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(yt["client_secrets"], YOUTUBE_SCOPES)
        creds = flow.run_local_server(port=0)
    with open(yt["token"], "w", encoding="utf-8") as f:
        f.write(creds.to_json())
    return creds


def publier_youtube_short(fichier_video, titre, description, tags, config):
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload

    yt = config["publication"]["youtube"]
    youtube = build("youtube", "v3", credentials=autoriser_youtube(config))
    body = {
        "snippet": {
            "title": titre[:100],
            "description": f"{description}\n\n{' '.join(tags)} #Shorts"[:5000],
            "tags": [t.lstrip("#") for t in tags],
            "categoryId": yt["category_id"],
        },
        "status": {
            "privacyStatus": yt["privacy"],
            "selfDeclaredMadeForKids": False,
            "containsSyntheticMedia": yt["contenu_synthetique"],
        },
    }
    media = MediaFileUpload(fichier_video, mimetype="video/mp4", chunksize=8 << 20, resumable=True)
    requete = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
    reponse = None
    while reponse is None:
        statut, reponse = requete.next_chunk()
        if statut:
            print(f"   upload YouTube : {int(statut.progress() * 100)} %")
    url = f"https://youtube.com/shorts/{reponse['id']}"
    print(f"✅ YouTube : {url}")
    return url


def publier_tiktok(fichier_video, description, hashtags, config):
    # Bibliothèque non officielle (automatisation de navigateur) : à tes risques,
    # cf. README. L'API officielle « Content Posting » de TikTok demande un audit.
    from tiktok_uploader.upload import upload_video

    upload_video(
        fichier_video,
        description=f"{description} {' '.join(hashtags)}",
        cookies=config["publication"]["tiktok"]["cookies"],
        headless=True,
    )
    print("✅ TikTok publié")
    return "tiktok"


def publier_instagram_reel(fichier_video, caption, config):
    # Bibliothèque non officielle : risque de blocage du compte, cf. README.
    from instagrapi import Client

    session = "instagram_session.json"
    cl = Client()
    if os.path.exists(session):
        cl.load_settings(session)
    cl.login(secret(config, "instagram_username"), secret(config, "instagram_password"))
    cl.dump_settings(session)
    media = cl.clip_upload(fichier_video, caption=caption)
    url = f"https://instagram.com/reel/{media.code}"
    print(f"✅ Instagram : {url}")
    return url
