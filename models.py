# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    number = db.Column(db.Integer)

    # One episode has many appearances
    appearances = db.relationship('Appearance', backref='episode', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'number': self.number,
            'appearances': [appearance.to_dict(nested=True) for appearance in self.appearances]
        }

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)

    # One guest has many appearances
    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'occupation': self.occupation
        }

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)

    # Foreign Keys
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))

    def to_dict(self, nested=False):
        base = {
            'id': self.id,
            'rating': self.rating,
            'episode_id': self.episode_id,
            'guest_id': self.guest_id,
        }

        if nested:
            base['episode'] = {
                'id': self.episode.id,
                'date': self.episode.date,
                'number': self.episode.number
            }
            base['guest'] = {
                'id': self.guest.id,
                'name': self.guest.name,
                'occupation': self.guest.occupation
            }

        return base
# This file defines the database models for the Late Show application.