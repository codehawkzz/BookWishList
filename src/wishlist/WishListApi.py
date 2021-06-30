"""

WishListAPI class - REST APIs for each operations to manage WishList resource

"""


from flask import jsonify, request
from flask_restful import Resource

from .dao import WishListDao
from ..book.dao import BookDao
from ..exception.CustomException import InvalidAPIUsage


class WishListGetAPI(Resource):

    def get(self, userid, id):
        if id and userid:
            wishlist_id = WishListDao.get_by_wishlistid(userid, id)
            if not wishlist_id:
                raise InvalidAPIUsage("Invalid wishlist id or user id", status_code=400)
        try:
            result = WishListDao.get_by_wishlistid(userid, id)
            response = jsonify();
            if result:
                return jsonify(result[0]);
            else:
                response.status_code = 404
            return response
        except Exception as e:
            raise InvalidAPIUsage(str(e), status_code=400)


class WishListCreateAPI(Resource):

    def post(self, userid):
        try:
            wishlist_details = request.get_json()
            name = wishlist_details["wishlistName"]
            description = wishlist_details["description"]
            result = WishListDao.insert_wishlist(name, description, userid)
            response = jsonify()
            if result:
                wishlist_id = WishListDao.get_wishlist_id(userid, name)
                response.status_code = 201
                response.headers['location'] = "/api/v1/users/" + str(userid) + "/wishlists/" + str(wishlist_id[0])
            else:
                raise InvalidAPIUsage("Invalid user", status_code=400)
            return response
        except Exception as e:
            print(e.with_traceback())
            raise InvalidAPIUsage(str(e), status_code=400)


class WishListUpdateAPI(Resource):

    def put(self, userid, id):
        if id and userid:
            wishlist_id = WishListDao.get_by_wishlistid(userid, id)
            if not wishlist_id:
                raise InvalidAPIUsage("Invalid wishlist id or user id", status_code=400)
            try:
                wishlist_details = request.get_json()
                name = wishlist_details["wishlistName"]
                description = wishlist_details["description"]
                result = WishListDao.update_wishlist(id, name, description, userid)
                response = jsonify()
                if result:
                    response.status_code = 204
                else:
                    raise InvalidAPIUsage("Invalid userid or name", status_code=400)
                return response
            except Exception as e:
                print(e.with_traceback())
                raise InvalidAPIUsage(str(e), status_code=400)


class WishListDeleteAPI(Resource):

    def delete(self, userid, id):
        if id and userid:
            wishlist_id = WishListDao.get_by_wishlistid(userid, id)
            if not wishlist_id:
                raise InvalidAPIUsage("Invalid wishlist id or user id", status_code=400)
            try:
                result = WishListDao.delete_wishlist(id, userid)
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


class WishListGetAllAPI(Resource):

    def get(self, userid):
        try:
            result = WishListDao.get_all_wishlist(userid)
            response = jsonify();
            if result:
                return jsonify(result);
            else:
                response.status_code = 404
            return response
        except Exception as e:
            raise InvalidAPIUsage(str(e), status_code=400)


class WishListGetAllBooksAPI(Resource):

    def get(self, userid, id):
        if id and userid:
            wishlist_books = WishListDao.get_by_wishlist_books(userid, id)
            if not wishlist_books:
                raise InvalidAPIUsage("Empty wishlist", status_code=404)
            try:
                result = BookDao.get_bookids(wishlist_books[0])
                if result:
                    return jsonify(result)
                else:
                    raise InvalidAPIUsage("Invalid userid or name", status_code=400)
            except Exception as e:
                raise InvalidAPIUsage(str(e), status_code=400)


class WishListAddBookAPI(Resource):

    def post(self, userid, id, bookid):
        if id and userid:
            wishlist_id = WishListDao.get_by_wishlistid(userid, id)
            if not wishlist_id:
                raise InvalidAPIUsage("Invalid wishlist id or user id", status_code=400)
            try:
                wishlist_books = WishListDao.get_by_wishlist_books(userid, id)
                bookslist_list = str(wishlist_books[0]).split(',')
                if 'None' in bookslist_list:
                    bookslist_list.remove('None')
                if '' in bookslist_list:
                    bookslist_list.remove('')
                if not (bookid in bookslist_list):
                    bookslist_list.append(bookid)
                bookids_str = ','.join(str(s) for s in bookslist_list)
                result = WishListDao.update_wishlist_bookids(id, userid, bookids_str)
                response = jsonify()
                if result:
                    response.status_code = 204
                else:
                    raise InvalidAPIUsage("Invalid userid or name", status_code=400)
                return response
            except Exception as e:
                raise InvalidAPIUsage(str(e), status_code=400)


class WishListDeleteBookAPI(Resource):

    def delete(self, userid, id, bookid):
        if id and userid:
            wishlist_id = WishListDao.get_by_wishlistid(userid, id)
            if not wishlist_id:
                raise InvalidAPIUsage("Invalid wishlist id or user id", status_code=400)
            try:
                wishlist_books = WishListDao.get_by_wishlist_books(userid, id)
                bookslist_list = str(wishlist_books[0]).split(',')
                if 'None' in bookslist_list:
                    bookslist_list.remove('None')
                if '' in bookslist_list:
                    bookslist_list.remove('')
                if bookid in bookslist_list:
                    bookslist_list.remove(bookid)
                bookids_str = ','.join(str(s) for s in bookslist_list)
                result = WishListDao.update_wishlist_bookids(id, userid, bookids_str)
                response = jsonify()
                if result:
                    response.status_code = 204
                else:
                    raise InvalidAPIUsage("Invalid userid or name", status_code=400)
                return response
            except Exception as e:
                raise InvalidAPIUsage(str(e), status_code=400)