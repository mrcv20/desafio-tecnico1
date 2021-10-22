from .. import db
from typing import List

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, index=True)
    firstName = db.Column(db.String(20))
    lastName = db.Column(db.String(20))
    birthdate = db.Column(db.Date, index=True)
    addresses = db.relationship("Addresses", primaryjoin="User.id == Addresses.id_user", cascade='all, delete-orphan')

class Addresses(db.Model):
    __tablename__ = "addresses"

    id = db.Column(db.Integer, primary_key=True, index=True)
    street = db.Column(db.String(60))
    number = db.Column(db.Integer)
    city = db.Column(db.String(25))
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship("User", back_populates="addresses")