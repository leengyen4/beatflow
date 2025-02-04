from . import db

class PlaylistSong(db.Model):
    __tablename__ = 'playlist_songs'

    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)

    playlist = db.relationship("Playlist", back_populates="songs")
    song = db.relationship("Song")

    __table_args__ = (db.UniqueConstraint('playlist_id', 'song_id', name='unique_playlist_song'),)
