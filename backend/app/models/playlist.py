from . import db

class Playlist(db.Model):
    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    owner = db.relationship("User", back_populates="playlists")
    songs = db.relationship("PlaylistSong", back_populates="playlist", cascade="all, delete-orphan")

