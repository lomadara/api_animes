from typing import List, Dict
from mypy_extensions import TypedDict


class EpisodeInterface(TypedDict, total=False):
    EPISODE_URL: str
    ANIME_ID: int