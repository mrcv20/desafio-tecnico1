from re import A
from flask import request, jsonify
from ..database.database  import session
from api.model.User import Address, User
from datetime import datetime

class UserController:
    def list_users():
        from api.schema.userSchema import many_users_schema
        try:
            users = session.query(User).join(Address, (User.id == Address.user_id)).all()
            if not users:
                return jsonify({"message": "users not found"})
        except Exception as error:
            return jsonify({"message": f"{error}"}), 500
        return jsonify({"users": many_users_schema.dump(users)}), 200

    def delete_user(id):
        user_to_delete = session.query(User).filter(User.id == id).first()
        if not user_to_delete:
            return jsonify({"message": "User not found"}), 400
        try:
            session.delete(user_to_delete)
            session.commit()
            session.close()
        except Exception as error:
            return error
        return jsonify({"message": "User deleted sucessfully"})

    def update_user(id):
        user_to_update = session.query(User).filter(User.id == id).first()
        if not user_to_update:
            return jsonify({"message": "User not found"}), 400
        data = request.get_json()
        print(len(data['birthdate']))
        if not data:
            return jsonify({"message": "missing payload"})
        try:
            birthdate_formated = datetime.strptime(data['birthdate'], '%Y-%m-%d')
            if len(data) > 3:
                data = list(request.get_json())
                return jsonify({"message": f"Operation invalid, maybe the data is incorrect"}), 400
            user_to_update.firstName = data['firstName']
            user_to_update.lastName = data['lastName']
            user_to_update.birthdate = birthdate_formated
            session.commit()
        except Exception as error:
            print(error)
            if type(error) == KeyError:
                return jsonify({"message": f"key {error} is missing or incorrect"}), 400
            elif type(error) == ValueError:
                if 'time data' in str(error):
                    return jsonify({"message": f"the birthdate format is incorrect"}), 400
                if 'unconverted data remains' in str(error):
                    return jsonify({"message": f"could not verify the birthdate format"}), 400
                print(error)
                return jsonify({"message": "Could not verify"}), 500
            
        return jsonify({"message": "User updated sucessfully"})


