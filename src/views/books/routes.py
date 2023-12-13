from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required

from src.views.books.forms import AddBookForm
from src.models import Book
from src.config import Config


book_blueprint = Blueprint("book", __name__)


@book_blueprint.route("/book/<int:id>")
def book(id):
    book_id = Book.query.get(id)
    return render_template("books/book.html", book=book_id)


@book_blueprint.route("/add_book", methods=["GET", "POST"])
@login_required
def add_book():
    form = AddBookForm()

    if form.validate_on_submit():
        new_book = Book()

        new_book.title = form.title.data
        new_book.author = form.author.data
        new_book.create()

        return redirect(url_for("main.home"))

    return render_template("books/add_book.html", form=form)
