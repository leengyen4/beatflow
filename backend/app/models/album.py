from . import db

class Album(db.Model):
    __tablename__ = 'albums'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    creator = db.relationship("User", back_populates="albums")
    songs = db.relationship("Song", back_populates="album", cascade="all, delete-orphan")
