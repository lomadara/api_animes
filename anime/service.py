from .model import Anime
from .interface import AnimeInterface

from typing import List
from app import db
from flask_sqlalchemy import Pagination
from sqlalchemy import asc, desc
from datetime import datetime
from flask import jsonify

class AnimeService():
    @staticmethod
    def get_all() -> List[Anime]:
        return Anime.query.filter_by().all()
    
    @staticmethod
    def get_by_id(ANIME_ID: int) -> Anime:
        return Anime.query.filter_by(ANIME_ID=ANIME_ID).first_or_404(description='não existem animes com o id {}'.format(ANIME_ID))
    
    @staticmethod
    def paginate(page: int, per_page: int = 50) -> Pagination:
        paginated_animes = Anime.query.filter()
        paginated_animes = paginated_animes.order_by(asc(Anime.ANIME_ID))
        return paginated_animes.paginate(page=page, per_page=per_page, max_per_page=100)
    
    @staticmethod
    def update(ANIME_ID: int, anime: AnimeInterface) -> Anime:
        existing_anime = Anime.query.filter_by(ANIME_ID=ANIME_ID).first_or_404(description='não existem animesx com o id {}'.formatr(ANIME_ID))
        existing_anime.update(anime)
        db.session.commit()
        return existing_anime
    
    @staticmethod
    def create(anime: AnimeInterface) -> Anime:
        existing_anime = Anime.query.filter_by(ANIME_URL=anime.get('ANIME_URL')).first()
        
        if bool(existing_anime):
            # resp = jsonify({'message': 'Já existe um cadastro para o anime com o id {} .'.format(existing_anime.ANIME_ID), 'id': existing_anime.ANIME_ID})
            # resp.status_code = 400
            return existing_anime
        
        new_anime = Anime(
            ANIME_NAME = anime.get('ANIME_NAME'),
            ANIME_NUM_EPISODES = anime.get('ANIME_NUM_EPISODES'),
            ANIME_THUMBNAILS = anime.get('ANIME_THUMBNAILS'),
            ANIME_URL = anime.get('ANIME_URL'),
            ANIME_DESCRIPTION = anime.get('ANIME_DESCRIPTION'),
            ANIME_IMAGE = anime.get('ANIME_IMAGE'),
            ANIME_LANGUAGE = anime.get('ANIME_LANGUAGE'),
            ANIME_STATUS = anime.get('ANIME_STATUS')
        )
        
        db.session.add(new_anime)
        db.session.commit()
        return new_anime
    
    @staticmethod
    def delete_by_id(ANIME_ID: int) -> List[str]:
        anime = Anime.query.filter_by(ANIME_ID=ANIME_ID).first_or_404(description='não existem animes com o id {}'.format(ANIME_ID))
        db.session.delete(anime)
        db.session.commit()
        return [ANIME_ID]
    
    
    
    