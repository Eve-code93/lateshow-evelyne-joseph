# resources.py

from flask_restful import Resource, reqparse
from flask import request
from models import db, Episode, Guest, Appearance

# Parser for POST /appearances
appearance_parser = reqparse.RequestParser()
appearance_parser.add_argument('rating', type=int, required=True, help='Rating is required and must be an integer')
appearance_parser.add_argument('episode_id', type=int, required=True, help='Episode ID is required')
appearance_parser.add_argument('guest_id', type=int, required=True, help='Guest ID is required')


# ---------------------- Episodes ----------------------

class EpisodeListResource(Resource):
    def get(self):
        episodes = Episode.query.all()
        return [e.to_dict() for e in episodes], 200


class EpisodeDetailResource(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if episode:
            return episode.to_dict(), 200
        return {"error": "Episode not found"}, 404

    def delete(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404

        db.session.delete(episode)
        db.session.commit()
        return {}, 204


# ---------------------- Guests ----------------------

class GuestListResource(Resource):
    def get(self):
        guests = Guest.query.all()
        return [g.to_dict() for g in guests], 200


# ---------------------- Appearances ----------------------

class AppearanceCreateResource(Resource):
    def post(self):
        args = appearance_parser.parse_args()
        rating = args['rating']
        episode_id = args['episode_id']
        guest_id = args['guest_id']

        # Validation: rating must be 1–5
        if rating < 1 or rating > 5:
            return {"errors": ["rating must be between 1 and 5"]}, 400

        episode = Episode.query.get(episode_id)
        guest = Guest.query.get(guest_id)

        if not episode or not guest:
            return {"errors": ["episode or guest not found"]}, 400

        appearance = Appearance(
            rating=rating,
            episode_id=episode_id,
            guest_id=guest_id
        )

        db.session.add(appearance)
        db.session.commit()

        return appearance.to_dict(nested=True), 201
