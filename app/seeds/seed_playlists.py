from app.models import db, Playlist, environment, SCHEMA
from sqlalchemy.sql import text

def seed_playlists():
    playlist1 = Playlist(
        title='Top 100 hits', user_id=1, image_url='http://example.com/playlist1.jpg')
    playlist2 = Playlist(
        title='Indie', user_id=2, image_url='http://example.com/playlist2.jpg')
    playlist3 = Playlist(
        title='Party Hits', user_id=3, image_url='http://example.com/playlist3.jpg')

    db.session.add(playlist1)
    db.session.add(playlist2)
    db.session.add(playlist3)
    db.session.commit()

def undo_playlists():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.playlists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM playlists"))

    db.session.commit()
