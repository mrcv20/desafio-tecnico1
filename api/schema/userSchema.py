from ..model.User import Address, User
from .. import ma


class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ['id', 'street', 'number', 'city', 'user_id']
        model = Address
        load_instance = True
        include_fk = True
        #Fields to skip during serialization
        load_only = 'addresses'

address_schema = AddressSchema()    
addresses_schema = AddressSchema(many=True)

class UserSchema(ma.SQLAlchemyAutoSchema):
    addresses = ma.Nested(AddressSchema, only=('id', 'street', 'number', 'city'), many=True)
    class Meta:
        model = User
        load_instance = True
        include_fk = True

user_schema = UserSchema()
many_users_schema = UserSchema(many=True)