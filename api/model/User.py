from .. import db
from typing import List
from datetime import datetime


class Address(db.Model):
    __tablename__ = "addresses"

    id = db.Column(db.Integer, primary_key=True, index=True)
    street = db.Column(db.String(60))
    number = db.Column(db.Integer)
    city = db.Column(db.String(25))
    users = db.relationship("User", primaryjoin="Address.id == User.id_address1", cascade='all, delete-orphan')

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, index=True)
    firstName = db.Column(db.String(20))
    lastName = db.Column(db.String(20))
    birthdate = db.Column(db.String(10))
    password = db.Column(db.String(60))
    id_address1 = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=False)
    id_address2 = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=False)
    address1 = db.relationship("Address", foreign_keys='User.id_address1', back_populates="users")
    address2 = db.relationship("Address", foreign_keys='User.id_address2', back_populates="users")
