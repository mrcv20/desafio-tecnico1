from flask import Flask, render_template, request, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
from ..models.User import User
import uuid

def signup_user():
    data = request.get_json()

    new_user = User(
    firstName=data['firstName'],
    lastName=data['lastName'],
    birthdate=data['birthdate'],
    addresses=data['addresses'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "user registered successfully"})

def delete_user():
    user_to_delete = User.query.get_or_404(id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
    except Exception as error:
        return error
    return jsonify({"message": "User deleted sucessfully"})

def update_user():
    user_to_update = User.query.get_or_404(id)

    data = request.get_json()
    user_to_update.firstName = data['firstName']
    user_to_update.lastName = data['lastName']
    user_to_update.birthdate = data['birthdate']
    user_to_update.addresses = data['addresses']
    try:
        db.session.commit()
    except Exception as error:
        return error
    return jsonify({"message": "User updated sucessfully"})