from app import db


class Anime(db.Model):
    ANIME_ID: int = db.Column(db.Integer, primary_key=True)
    ANIME_NAME: str = db.Column(db.String(200))
    ANIME_NUM_EPISODES: int = db.Column(db.Integer)
    ANIME_THUMBNAILS: str = db.Column(db.String(200))
    ANIME_URL: str = db.Column(db.String(200))
    ANIME_DESCRIPTION: str = db.Column(db.String(2000))
    ANIME_IMAGE: str = db.Column(db.String(200))
    ANIME_LANGUAGE: str = db.Column(db.String(45))
    ANIME_STATUS: str = db.Column(db.String(45))
    
    def update(self, ANIME_NAME: str, ANIME_NUM_EPISODES: int, ANIME_THUMBNAILS: str, ANIME_URL: str, ANIME_DESCRIPTION: str, ANIME_IMAGE: str, ANIME_LANGUAGE: str, ANIME_STATUS: str):
        self.ANIME_NAME = ANIME_NAME
        self.ANIME_NUM_EPISODES = ANIME_NUM_EPISODES
        self.ANIME_THUMBNAILS = ANIME_THUMBNAILS
        self.ANIME_URL = ANIME_URL
        self.ANIME_DESCRIPTION = ANIME_DESCRIPTION
        self.ANIME_IMAGE = ANIME_IMAGE
        self.ANIME_LANGUAGE = ANIME_LANGUAGE
        self.ANIME_STATUS = ANIME_STATUS