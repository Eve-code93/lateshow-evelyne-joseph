# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

from models import db
from resources import EpisodeListResource, EpisodeDetailResource, GuestListResource, AppearanceCreateResource

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lateshow.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

# RESTful routes
api.add_resource(EpisodeListResource, "/episodes")
api.add_resource(EpisodeDetailResource, "/episodes/<int:id>")
api.add_resource(GuestListResource, "/guests")
api.add_resource(AppearanceCreateResource, "/appearances")

if __name__ == "__main__":
    app.run(debug=True)
# This is the main entry point for the application.