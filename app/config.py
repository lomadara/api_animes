import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    """Set Flask configuration vars."""

    # General Config
    ENV = os.environ.get('FLASK_ENV')
    DEBUG = os.environ.get('FLASK_DEBUG') is not None
    TESTING = os.environ.get('FLASK_TESTING') is not None

    # Postgresql Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

