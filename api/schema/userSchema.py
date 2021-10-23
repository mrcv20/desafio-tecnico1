from ..model.User import Address, User
from .. import ma

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ['id', 'firstName', 'lastName', 'birthdate', 'street', 'city', 'number']
        model = User
        load_instance = True
        include_fk = True
        #Fields to skip during serialization
        # load_only = 'met'
        
user_schema = UserSchema()
many_users_schema = UserSchema(many=True)

