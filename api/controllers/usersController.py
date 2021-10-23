from re import A
from flask import request, jsonify
from .. import db
from api.model.User import Address, User
from sqlalchemy.orm import aliased


class UserController:

    def lista_usuario():
        from api.schema.userSchema import many_users_schema
        try:
            users = db.session.query(
            User.firstName,
            User.lastName,
            User.birthdate,
            Address.city,
            Address.number,
            Address.street).\
            join(Address, (Address.id == User.id_address1)).all()
        except Exception as error:
            return jsonify({"message": f"{error}"}), 500
        return jsonify({"users": many_users_schema.dump(users)}), 200

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

