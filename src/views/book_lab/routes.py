from flask import render_template, Blueprint, request

from src.models import Book


books_blueprint = Blueprint("books", __name__)


@books_blueprint.route("/book_laboratory")
def book_lab():
    search = request.args.get("search")
    if search:
        books = Book.query.filter(Book.project_name == search)
    else:
        books = Book.query.all()
    return render_template("book_lab/book_list.html", books=books)
