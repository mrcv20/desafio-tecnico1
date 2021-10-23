import requests
from .controllers import usersController
from flask import Blueprint, jsonify, request, make_response
import datetime
import jwt
from .config import Config
from .middlewares.auth import token_required
from .controllers.usersController import UserController
from .controllers.authController import AuthController

bp_routes = Blueprint('routes', __name__)

@bp_routes.route('/users', methods=['GET'])
@token_required
def list_users():
    return UserController.lista_usuario()

@bp_routes.route('/users', methods=['PUT'])
def update_user():
    return 'nothing'

@bp_routes.route('/users', methods=['DELETE'])
def delete_user():
    return 'nothing'

@bp_routes.route('/login', methods=['GET'])
def login():
    return AuthController.login_user()