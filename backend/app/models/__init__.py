from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from .config import Config
from .extensions import db
from .models import User, Song, Album, Playlist, Like, PlaylistSong
from .routes import register_routes  # Function to register all routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    CORS(app)  # Enable Cross-Origin Resource Sharing

    # Register routes
    register_routes(app)

    return app
