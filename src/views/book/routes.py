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
    page_num = int(request.args.get("page_num", default=1))

    if search:
        books = Book.query.filter(Book.project_name.ilike(f"%{search}%")).paginate(per_page=12,page=page_num, error_out=True)
    else:
        books = Book.query.paginate(per_page=12,page=page_num, error_out=True)

        # books = Book.query.all()
    return render_template("book_lab/book_list.html",page_num=page_num, books=books, search=search)
