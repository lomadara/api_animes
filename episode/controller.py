from flask import g, request, Response, jsonify
from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource
from typing import List, Dict

from .service import EpisodeService
from .model import Episode
from .schema import EpisodeSchema

api = Namespace('Episode')


@api.route('/')
class EpisodeResource(Resource):
    @responds(schema=EpisodeSchema(many=True))
    def get(self) -> List[Episode]:
        return EpisodeService.get_all()

@api.route('/<int:EPISODE_ID>')
class EpisodeIdResource(Resource):
    @responds(schema=EpisodeSchema)
    def get(self, EPISODE_ID: int) -> Episode:
        return EpisodeService.get_by_id(EPISODE_ID)