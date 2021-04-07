from flask import g, request, Response
from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource

from .service import DownloadService

api = Namespace('Download')

@api.route('/')
class DownloadResource(Resource):
    def get(self):
        return Response(DownloadService.download("https://animesvision.biz/animes/toriko/episodio-03/legendado/download", '720'))