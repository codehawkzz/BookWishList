from flask.blueprints import Blueprint
from flask_restful import Api

from src.wishlist.WishListApi import WishListGetAPI, WishListCreateAPI, WishListDeleteAPI, WishListUpdateAPI, WishListGetAllAPI, WishListAddBookAPI, WishListDeleteBookAPI, WishListGetAllBooksAPI

wishlist_manager = Blueprint("wishlist", __name__)
api = Api(wishlist_manager)

api.add_resource(WishListGetAPI, "/api/v1/users/<userid>/wishlists/<id>")
api.add_resource(WishListCreateAPI, "/api/v1/users/<userid>/wishlists")
api.add_resource(WishListDeleteAPI, "/api/v1/users/<userid>/wishlists/<id>")
api.add_resource(WishListUpdateAPI, "/api/v1/users/<userid>/wishlists/<id>")
api.add_resource(WishListAddBookAPI, "/api/v1/users/<userid>/wishlists/<id>/books/<bookid>")
api.add_resource(WishListDeleteBookAPI, "/api/v1/users/<userid>/wishlists/<id>/books/<bookid>")
api.add_resource(WishListGetAllBooksAPI, "/api/v1/users/<userid>/wishlists/<id>/books")
api.add_resource(WishListGetAllAPI, "/api/v1/users/<userid>/wishlists/all")
