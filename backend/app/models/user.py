from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)

    songs = db.relationship("Song", back_populates="uploader", cascade="all, delete-orphan")
    albums = db.relationship("Album", back_populates="creator", cascade="all, delete-orphan")
    playlists = db.relationship("Playlist", back_populates="owner", cascade="all, delete-orphan")
    likes = db.relationship("Like", back_populates="user", cascade="all, delete-orphan")
