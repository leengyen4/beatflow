from . import db

class Like(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)

    user = db.relationship("User", back_populates="likes")
    song = db.relationship("Song", back_populates="likes")

    __table_args__ = (db.UniqueConstraint('user_id', 'song_id', name='unique_user_like'),)
