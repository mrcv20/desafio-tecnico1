from flask import Blueprint, jsonify, request, make_response
from .config import Config
from .middlewares.auth import token_required
from .controllers.usersController import UserController
from .controllers.authController import AuthController
from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin

bp_routes = Blueprint('routes', __name__)

@bp_routes.route('auth/signup', methods=['POST'])
def register():
    return AuthController.signup_user()
@bp_routes.route('/users', methods=['GET'])
@token_required
def list_users():
    return UserController.list_users()

@bp_routes.route('/users/<id>', methods=['PUT'])
@token_required
def update_user(id):
    return UserController.update_user(id=id)

@bp_routes.route('/users/<id>', methods=['DELETE'])
@token_required
def delete_user(id):
    return UserController.delete_user(id=id)

@bp_routes.route('/login', methods=['GET'])
def login():
    return AuthController.login_user()
