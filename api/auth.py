from flask import Blueprint, request
from .controllers import authController


bp_auth = Blueprint('auth', __name__)

@bp_auth.route('/signup', methods=['POST'])
def register():
    data = request.get_json()
    return authController.signup_user()