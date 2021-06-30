"""

UserAPI class - REST APIs for each operations to manage USer resource

"""


from flask import jsonify, request
from flask_restful import Resource

from .dao import UserDao
from ..exception.CustomException import InvalidAPIUsage


class UserGetAPI(Resource):

    def get(self, id):
        if id:
            wishlist_id = UserDao.get_by_id(id)
            if not wishlist_id:
                raise InvalidAPIUsage("User Not Found", status_code=404)
        if id:
            try:
                result = UserDao.get_by_id(id)
                response = jsonify();
                if result:
                    return jsonify(result[0]);
                else:
                    response.status_code = 404
                return response
            except Exception as e:
                raise InvalidAPIUsage(str(e), status_code=400)


class UserCreateAPI(Resource):

    def post(self):

        try:
            user_details = request.get_json()
            firstname = user_details["firstName"]
            lastname = user_details["lastName"]
            email = user_details["email"]
            password = user_details["password"]
            try:
                result = UserDao.insert_user(firstname, lastname, email, password, 'ACTIVE')
            except Exception as e:
                raise InvalidAPIUsage(str("User Not created: " + e), status_code=400)
            response = jsonify()
            if result:
                user_id = UserDao.get_by_email(email)
                response.status_code = 201
                response.headers['location'] = "/api/v1/users/" + str(user_id[0])
            else:
                response.status_code = 400
            return response
        except Exception as e:
            raise InvalidAPIUsage(str("User Not created: "+e), status_code=400)


class UserUpdateAPI(Resource):

    def put(self, id):

        if id:
            wishlist_id = UserDao.get_by_id(id)
            if not wishlist_id:
                raise InvalidAPIUsage("User Not Found", status_code=404)
        if id:
            try:
                user_details = request.get_json()
                firstname = user_details["firstName"]
                lastname = user_details["lastName"]
                email = user_details["email"]
                password = user_details["password"]
                result = UserDao.update_user(id, firstname, lastname, email, password)
                response = jsonify();
                if result:
                    response.status_code = 204
                else:
                    response.status_code = 400
                return response
            except Exception as e:
                raise InvalidAPIUsage(str(e), status_code=400)


class UserDeleteAPI(Resource):

    def delete(self, id):
        if id:
            wishlist_id = UserDao.get_by_id(id)
            if not wishlist_id:
                raise InvalidAPIUsage("User Not Found", status_code=404)
        if id:
            try:
                result = UserDao.delete_user(id)
                response = jsonify();
                if result:
                    response.status_code = 204
                else:
                    response.status_code = 400
                return response
            except Exception as e:
                raise InvalidAPIUsage(str(e), status_code=400)
        else:
            return jsonify({"Bad Request"}), 400


class UserGetAllAPI(Resource):

    def get(self):
        try:
            result = UserDao.get_users()
            response = jsonify();
            if result:
                return jsonify(result);
            else:
                response.status_code = 404
            return response
        except Exception as e:
            raise InvalidAPIUsage(str(e), status_code=400)
