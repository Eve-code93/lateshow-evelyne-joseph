# seed.py
from app import app
from models import db, Episode, Guest, Appearance

with app.app_context():
    # Clear existing data
    print("Clearing existing data...")
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()

    # Create Episodes
    print("Seeding episodes...")
    ep1 = Episode(date='1/11/99', number=1)
    ep2 = Episode(date='1/12/99', number=2)

    # Create Guests
    print("Seeding guests...")
    guest1 = Guest(name='Michael J. Fox', occupation='actor')
    guest2 = Guest(name='Sandra Bernhard', occupation='comedian')
    guest3 = Guest(name='Tracey Ullman', occupation='television actress')

    # Create Appearances
    print("Seeding appearances...")
    appearance1 = Appearance(rating=4, episode=ep1, guest=guest1)
    appearance2 = Appearance(rating=5, episode=ep2, guest=guest3)

    # Add to session and commit
    db.session.add_all([ep1, ep2, guest1, guest2, guest3, appearance1, appearance2])
    db.session.commit()
    print("Done seeding ✅")
