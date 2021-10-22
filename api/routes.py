import requests
from .controllers import usersController
from flask import Blueprint, jsonify, request, make_response
import datetime
import jwt
from .config import Config
from .middlewares.auth import token_required

bp_routes = Blueprint('routes', __name__)

@bp_routes.route('/users', methods=['GET'])
@token_required
def list_users():
    return jsonify({"message": 'this is a protected route'})

@bp_routes.route('/users', methods=['POST'])
def create_user():
    return 'nothing'

@bp_routes.route('/users', methods=['PUT'])
def update_user():
    return 'nothing'

@bp_routes.route('/users', methods=['DELETE'])
def delete_user():
    return 'nothing'

@bp_routes.route('/login', methods=['GET'])
def login():
    auth = request.authorization
    if auth and auth.password == 'password':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, Config.SECRET_KEY)

        return jsonify({'token': token})
    return make_response('could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required'})