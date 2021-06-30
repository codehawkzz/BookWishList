"""

Main program to start the application

"""


from flask import Flask, jsonify, json
from flask.blueprints import Blueprint
from werkzeug.exceptions import HTTPException

from src.book import book_manager
from src.exception.CustomException import InvalidAPIUsage
from src.user import user_manager
from src.wishlist import wishlist_manager
from database.db import create_tables, create_records

app = Flask(__name__)
application = Blueprint("application", __name__)
app.config["DEBUG"] = True

app.register_blueprint(application);
app.register_blueprint(book_manager);
app.register_blueprint(user_manager);
app.register_blueprint(wishlist_manager);

if __name__ == "__main__":
    create_tables()
    create_records()


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error=str(e)), 500


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(e):
    return jsonify(e.to_dict())


@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


app.run()
