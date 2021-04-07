from .model import Episode
from .interface import EpisodeInterface

from typing import List
from app import db
from flask_sqlalchemy import Pagination
from sqlalchemy import asc, desc
from datetime import datetime
from flask import jsonify

class EpisodeService():
    @staticmethod
    def get_all() -> List[Episode]:
        episodes = Episode.query.filter_by().all()
        
        if bool(episodes):
            resp = jsonify({'message': 'não existe nenhum episodio cadastrado .'})
            resp.status_code = 400
            return resp
            
        return Episode.query.filter_by().all()
    
    @staticmethod
    def get_by_id(EPISODE_ID: int) -> Episode:
        return Episode.query.filter_by(EPISODE_ID=EPISODE_ID).first_or_404(description='não existem episodios com o id {}'.format(EPISODE_ID))
    
    
    