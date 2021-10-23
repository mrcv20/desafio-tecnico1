from flask import request, jsonify
from flask.helpers import make_response
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
from ..model.User import User, Address
import jwt 
from ..config import Config

class AuthController:
    def signup_user():
        data = request.get_json()
        hashed_password = generate_password_hash(data['password'], method='sha256')
        print(len(data))
        print(len(data['addresses'][0]))
        if len(data) > 5 or len(data['addresses']) > 2:
            return jsonify({"message": "paylod incorret, please review the format"}), 400
        elif len(data['addresses'][0]) > 3 or len(data['addresses'][1]) > 3:
            return jsonify({"message": "payload incorret, please review the addresses param"}), 400
        elif len(data['password']) < 6:
            return jsonify({"message": "Password need at least 6 characters"}), 400
        elif len(data['firstName']) < 2:
            return jsonify({"message": "First name too short"}), 400
        else:
            try:
                new_address1 = Address(
                    street=data['addresses'][0]['street'],
                    number=data['addresses'][0]['number'],
                    city=data['addresses'][0]['city']
                )
                new_address2 = Address(
                    street=data['addresses'][1]['street'],
                    number=data['addresses'][1]['number'],
                    city=data['addresses'][1]['city']
                )
                db.session.add(new_address1)
                db.session.add(new_address2)
                db.session.commit()

                new_user = User(
                firstName=data['firstName'],
                lastName=data['lastName'],
                birthdate=data['birthdate'],
                password=hashed_password,
                id_address1=new_address1.id,
                id_address2=new_address2.id)
                db.session.add(new_user)
                db.session.commit()
            except Exception as error:
                if type(error) == KeyError:
                    return jsonify({"message_error": f"{error} param is required", 
                    f"message": f"Key {error} is invalid or incorrect"}), 400
                else:
                    return jsonify({"message": "could not verify"}), 500
        
       
        return jsonify({"message": "User registered successfully"})

    def login_user():
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!'})
        
        user = User.query.filter_by(firstName=auth.username).first()

        if not user:
            return jsonify({"messsage": "User not found"})
        
        if check_password_hash(user.password, auth.password):
            token = jwt.encode({"some": "payload"}, Config.SECRET_KEY, algorithm="HS256")
            print(token)
            return jsonify({"token": token})

        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!'})