from flask import request, jsonify
from flask.helpers import make_response
from werkzeug.security import generate_password_hash, check_password_hash
from ..database.database import session
from ..model.User import User, Address
import jwt 
from ..config import Config
from datetime import datetime

class AuthController:
    def signup_user():
        data = request.get_json()
        if not data:
            return jsonify({"message": "missing payload"}), 400
        try:
            if len(data) > 5 or len(data['addresses']) > 2:
                return jsonify({"message": "paylod incorret, please check params"}), 400
            elif len(data['addresses'][0]) > 3 or len(data['addresses'][1]) > 3:
                return jsonify({"message": "payload incorret, please check the addresses param"}), 400
            elif len(data['firstName']) < 2:
                return jsonify({"message": "First name too short"}), 400
        except Exception as error:
            if type(error) == KeyError:
                return jsonify({"message": f"param {error} is missing or incorrectw"}), 400
            else:
                return jsonify({"message": "could not verify"}), 500
        try:
            birthdate_formated = datetime.strptime(data['birthdate'], '%Y-%m-%d')
            new_user = User(
            firstName=data['firstName'],
            lastName=data['lastName'],
            birthdate=birthdate_formated)
            session.add(new_user)
            session.commit()
            new_address1 = Address(
                street=data['addresses'][0]['street'],
                number=data['addresses'][0]['number'],
                city=data['addresses'][0]['city'],
                user_id=new_user.id
            )
            new_address2 = Address(
                street=data['addresses'][1]['street'],
                number=data['addresses'][1]['number'],
                city=data['addresses'][1]['city'],
                user_id=new_user.id
            )
            session.add(new_address1)
            session.add(new_address2)
            session.commit()
        except Exception as error:
            print(error)
            if type(error) == KeyError:
                if 'street' in str(error) or 'number' in str(error) or 'city' in str(error):
                    return jsonify({"message": f"param {error} is missing or is incorrect, check the addresses"}), 400
                return jsonify({"message": f"{error} is missing or incorrect"}), 400
            elif type(error) == ValueError:
                if 'time data' in str(error):
                    return jsonify({"message": f"the birthdate format is incorrect"}), 400
            else:
                return jsonify({"message", "Could not verify"}), 500
    
        token = jwt.encode({"user_id": new_user.id}, Config.SECRET_KEY, algorithm="HS256")
        print(token)
        return jsonify({"message": f"User {data['firstName']} registered successfully"},
        {"token": token}), 201

    def login_user():
        auth = request.authorization


        if not auth or not auth.username or not auth.password:
            return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!'})
        
        user = session.query(User).filter_by(firstName=auth.username).first()

        if not user:
            return jsonify({"messsage": "User not found"})
        
        if check_password_hash(user.password, auth.password):
            token = jwt.encode({"user_id": user.id}, Config.SECRET_KEY, algorithm="HS256")
            print(token)
            return jsonify({"token": token})

        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!'})