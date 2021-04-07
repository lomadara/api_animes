from typing import List, Dict
from mypy_extensions import TypedDict


class AnimeInterface(TypedDict, total=False):
    ANIME_NAME: str
    ANIME_NUM_EPISODES: int
    ANIME_THUMBNAILS: str
    ANIME_URL: str
    ANIME_DESCRIPTION: str
    ANIME_IMAGE: str
    ANIME_LANGUAGE: str
    ANIME_STATUS: str