from flask import render_template, Blueprint, request

from src.models import Book


book_blueprint = Blueprint("book", __name__)


@book_blueprint.route("/book/<int:id>")
def book(id):
    book_id = Book.query.get(id)
    return render_template("book/book.html", book=book_id)


@book_blueprint.route("/book_laboratory")
def book_lab():
    search = request.args.get("search")
    if search:
        search = f"%{search}%"
        books = Book.query.filter(Book.project_name.ilike(search))
    else:
        books = Book.query.all()
    return render_template("book_lab/book_list.html", books=books)
