from marshmallow import fields, Schema, EXCLUDE


class AnimeSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    
    ANIME_ID = fields.Integer(attribute='ANIME_ID', required=True)
    ANIME_NAME = fields.String(attribute='ANIME_NAME', required=True)
    ANIME_NUM_EPISODES = fields.Integer(attribute='ANIME_NUM_EPISODES', required=True)
    ANIME_THUMBNAILS = fields.String(attribute='ANIME_THUMBNAILS', required=True)
    ANIME_URL = fields.String(attribute='ANIME_URL', required=True)
    ANIME_DESCRIPTION = fields.String(attribute='ANIME_DESCRIPTION', required=True)
    ANIME_IMAGE = fields.String(attribute='ANIME_IMAGE', required=True)
    ANIME_LANGUAGE = fields.String(attribute='ANIME_LANGUAGE', required=True)
    ANIME_STATUS = fields.String(attribute='ANIME_STATUS', required=True)