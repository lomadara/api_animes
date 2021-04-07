from marshmallow import fields, Schema, EXCLUDE


class EpisodeSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    
    EPISODE_ID = fields.Integer(attribute='EPISODE_ID', required=True)
    EPISODE_URL = fields.String(attribute='EPISODE_URL', required=True)
    ANIME_ID = fields.Integer(attribute='ANIME_ID', required=True)