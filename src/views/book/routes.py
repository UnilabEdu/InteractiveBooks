from flask import render_template, Blueprint

from src.models import Book


book_blueprint = Blueprint("book", __name__)


@book_blueprint.route("/book/<int:id>")
def book(id):
    book_id = Book.query.get(id)
    return render_template("book/book.html", book=book_id)
