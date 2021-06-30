"""

BookAPI class - REST APIs for each operations to manage Book resource

"""


from flask import jsonify, request
from flask_restful import Resource

from .dao import BookDao
from ..exception.CustomException import InvalidAPIUsage


class BookGetAPI(Resource):

    def get(self, id):
        if id:
            book_id = BookDao.get_by_id(id)
            if not book_id:
                raise InvalidAPIUsage("Book Not Found", status_code=404)
        try:
            result = BookDao.get_by_id(id)
            response = jsonify();
            if result:
                return jsonify(result[0]);
            else:
                response.status_code = 404
            return response
        except Exception as e:
            raise InvalidAPIUsage(str(e), status_code=400)


class BookCreateAPI(Resource):

    def post(self):
        try:
            book_details = request.get_json()
            title = book_details["title"]
            author = book_details["author"]
            isbn = book_details["isbn"]
            dop = book_details["dateOfPublication"]
            result = BookDao.insert_book(title,author,isbn,dop)
            response = jsonify()
            if result:
                book_id = BookDao.get_bookid(title)
                response.status_code = 201
                response.headers['location'] = "/api/v1/books/" + str(book_id[0])
            else:
                response.status_code = 400
            return response
        except Exception as e:
            raise InvalidAPIUsage(str(e), status_code=400)


class BookUpdateAPI(Resource):

    def put(self, id):
        if id:
            book_id = BookDao.get_by_id(id)
            if not book_id:
                raise InvalidAPIUsage("Book Not Found", status_code=404)
        try:
            book_details = request.get_json()
            title = book_details["title"]
            author = book_details["author"]
            isbn = book_details["isbn"]
            dop = book_details["dateOfPublication"]
            result = BookDao.update_book(id, title,author, isbn, dop)
            response = jsonify()
            if result:
                response.status_code = 204
            else:
                response.status_code = 400
            return response
        except Exception as e:
            raise InvalidAPIUsage(str(e), status_code=400)


class BookDeleteAPI(Resource):

    def delete(self, id):
        if id:
            book_id = BookDao.get_by_id(id)
            if not book_id:
                raise InvalidAPIUsage("Book Not Found", status_code=404)
        try:
            result = BookDao.delete_book(id)
            response = jsonify()
            if result:
                response.status_code = 204
            else:
                response.status_code = 400
            return response
        except Exception as e:
            raise InvalidAPIUsage(str(e), status_code=400)


class BookGetAllAPI(Resource):

    def get(self):
        try:
            result = BookDao.get_books()
            response = jsonify()
            if result:
                return jsonify(result)
            else:
                response.status_code = 404
            return response
        except Exception as e:
            raise InvalidAPIUsage(str(e), status_code=400)