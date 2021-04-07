from flask import g, request, Response, jsonify
from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource
from typing import List, Dict

from .service import AnimeService
from .model import Anime
from .schema import AnimeSchema

api = Namespace('Anime')

@api.route('/')
class AnimeResource(Resource):
    @responds(schema=AnimeSchema(many=True))
    def get(self) -> List[Anime]:
        return AnimeService.get_all()
    
    @responds(schema=AnimeSchema)
    def post(self) -> Anime:
        anime = request.json
        return AnimeService.create(anime)

@api.route('/<int:ANIME_ID>')
class AnimeIdResource(Resource):
    @responds(schema=AnimeSchema)
    def get(self, ANIME_ID: int) -> Anime:
        return AnimeService.get_by_id(ANIME_ID)
    
    def delete(self, ANIME_ID: int) -> Response:
        deleted_id = AnimeService.delete_by_id(ANIME_ID)
        return jsonify(dict(status='sucess', id=deleted_id))
    
    @responds(schema=AnimeSchema)
    def put(self) -> Anime:
        anime = request.json
        ANIME_ID = anime.get('ANIME_ID')
        return AnimeService.update(ANIME_ID, anime)

@api.route('/p/<int:page>')
class AnimePageResource(Resource):
    @responds(schema=AnimeSchema, api=api)
    def post(self, page) -> Dict:
        pagination = AnimeService.paginate(page)
        
        return {
            'page': pagination.page,
            'pages': pagination.pages,
            'items': pagination.items
        }