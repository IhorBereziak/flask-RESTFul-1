from flask_restful import Resource, reqparse
from app.models import UserModel

class User(Resource):
    req = reqparse.RequestParser()
    req.add_argument('email', required=True, type=str, help='Email is required')
    req.add_argument('name', required=True, type=str, help='Name is required')

    def get(self, email):
        user = UserModel.get_by_email(email)
        if not user:
            return {'message': 'user not found'}, 404
        return user.json()

    def post(self):
        data = User.req.parse_args()
        if UserModel.get_by_email(data['email']):
            return {'massage': 'user with this email already exists'}, 400
        user = UserModel(**data)
        user.save_to_db()
        return {'massage': 'user created'}

    def delete(self, email):
        user = UserModel.get_by_email(email)
        user.delete_from_db()
        return {'message': 'user is deleted'}

    def put(self, email):
        data = User.req.parse_args()
        user = UserModel.get_by_email(email)
        if not user:
            user = UserModel(email, data['name'])
            user.save_to_db()
            return {'massage': f'user with email {email} created'}
        user.name = data['name']
        user.save_to_db()
        return {'massage': f'user name is changed'}, 200
