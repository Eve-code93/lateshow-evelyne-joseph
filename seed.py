# seed.py

from models import db, Episode, Guest, Appearance
from app import app

# Use the Flask app context to interact with the DB
with app.app_context():
    print("🌱 Clearing existing data...")
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    db.session.commit()

    print("🌱 Seeding episodes...")
    ep1 = Episode(id=1, date="1/11/99", number=1)
    ep2 = Episode(id=2, date="1/12/99", number=2)
    db.session.add_all([ep1, ep2])
    db.session.commit()

    print("🌱 Seeding guests...")
    g1 = Guest(id=1, name="Michael J. Fox", occupation="actor")
    g2 = Guest(id=2, name="Sandra Bernhard", occupation="Comedian")
    g3 = Guest(id=3, name="Tracey Ullman", occupation="television actress")
    db.session.add_all([g1, g2, g3])
    db.session.commit()

    print("🌱 Seeding appearances...")
    a1 = Appearance(rating=4, episode_id=1, guest_id=1)
    a2 = Appearance(rating=5, episode_id=2, guest_id=3)
    db.session.add_all([a1, a2])
    db.session.commit()

    print("✅ Done seeding!")
