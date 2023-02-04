from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    category = db.Column(db.String(1000))
    place = db.Column(db.String(1000))
    start = db.Column(db.String(1000))
    end = db.Column(db.String(1000))
    mode = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, category, place, start, end, mode, user_id):
        self.name = name
        self.category = category
        self.place = place
        self.start = start
        self.end = end
        self.mode = mode
        self.user_id = user_id


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    contacts = db.relationship('Contact')


