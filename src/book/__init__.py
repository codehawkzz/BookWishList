from flask.blueprints import Blueprint
from flask_restful import Api

from src.book.BookApi import BookGetAPI,BookCreateAPI, BookDeleteAPI, BookUpdateAPI, BookGetAllAPI

book_manager = Blueprint("books", __name__)
api = Api(book_manager)

api.add_resource(BookGetAPI, "/api/v1/books/<id>")
api.add_resource(BookCreateAPI, "/api/v1/books")
api.add_resource(BookDeleteAPI, "/api/v1/books/<id>")
api.add_resource(BookUpdateAPI, "/api/v1/books/<id>")
api.add_resource(BookGetAllAPI, "/api/v1/books/all")