"""Module with tools for service."""
import re
from io import BytesIO

import requests
from PIL import Image
from pytube import YouTube
from pytube.cli import on_progress


def get_preview_image(youtube_url: str) -> Image:
    """Get preview image from YouTube.

    @param youtube_url: YouTube video url
    @return: preview image
    """
    video_id_list = re.findall(r"=(\w+)", youtube_url)
    if video_id_list:
        if len(video_id_list) == 1:
            video_id = video_id_list[-1]
        else:
            video_id = video_id_list[0]
    else:
        video_id = ""

    link = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    raw_data = requests.get(link).content
    image = Image.open(BytesIO(raw_data))
    return image


def download_video(video_folder: str, youtube_url: str) -> None:
    """Download video from YouTube with filename as video name.

    @param video_folder: path to video
    @param youtube_url: vide url
    """
    yt = YouTube(youtube_url, on_progress_callback=on_progress)

    video_title = yt.title.replace("/", "") \
        .replace("  ", " ") \
        .replace(" ", "_")
    video_title = f"{video_title}.mp4"
    print(video_title)
    yt.streams \
        .filter(progressive=True, file_extension='mp4') \
        .order_by('resolution') \
        .desc() \
        .first() \
        .download(output_path=video_folder, filename=video_title)
