from . import db

class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    uploader_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'), nullable=True)
    url = db.Column(db.String(500), nullable=False)  # AWS S3 storage URL
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    uploader = db.relationship("User", back_populates="songs")
    album = db.relationship("Album", back_populates="songs")
    likes = db.relationship("Like", back_populates="song", cascade="all, delete-orphan")
