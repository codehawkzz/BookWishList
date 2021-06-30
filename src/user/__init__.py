from flask.blueprints import Blueprint
from flask_restful import Api

from src.user.UserApi import UserGetAPI, UserCreateAPI, UserDeleteAPI, UserUpdateAPI, UserGetAllAPI

user_manager = Blueprint("users", __name__)
api = Api(user_manager)

api.add_resource(UserGetAPI, "/api/v1/users/<id>")
api.add_resource(UserCreateAPI, "/api/v1/users")
api.add_resource(UserDeleteAPI, "/api/v1/users/<id>")
api.add_resource(UserUpdateAPI, "/api/v1/users/<id>")
api.add_resource(UserGetAllAPI, "/api/v1/users/all")
