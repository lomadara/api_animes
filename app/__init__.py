from flask import Flask, Blueprint
from flask_restx import Api
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    
    app.config.from_object('app.config.Config')

    db.init_app(app)
    
    CORS(app, resources={r"/v1/*": {"origins": "*"}})
    
    with app.app_context():
        from anime.controller import api as anime_ns
        from download.controller import api as download_ns
        from episode.controller import api as episode_ns
        
        blueprint = Blueprint('api', __name__, url_prefix='/v1')
        api = Api(
            blueprint,
            title='teste api v1',
            version='1.0',
            description='teste restful api',
        )
        app.register_blueprint(blueprint)
        
        api.add_namespace(anime_ns, path='/anime')
        api.add_namespace(download_ns, path='/download')
        api.add_namespace(episode_ns, path='/episode')
        
        return app
        