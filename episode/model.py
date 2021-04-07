from app import db


class Episode(db.Model):
    EPISODE_ID: int = db.Column(db.Integer, primary_key=True)
    EPISODE_URL: str = db.Column(db.String(200))
    ANIME_ID: int = db.Column(db.Integer, db.ForeignKey('anime.ANIME_ID'))
    
    def update(self, EPISODE_URL: str):
        self.EPISODE_URL = EPISODE_URL