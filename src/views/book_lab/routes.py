from flask import render_template, Blueprint

from src.models import Book


books_blueprint = Blueprint("books", __name__)


@books_blueprint.route("/book_laboratory")
def book_lab():
    books = Book.query.all()
    return render_template("book_lab/book_list.html", books=books)
