from app import create_app, db
from anime.model import Anime
from episode.model import Episode

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Anime': Anime,
        'Episode': Episode
    }
