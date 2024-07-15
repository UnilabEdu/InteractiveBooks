from flask import render_template, Blueprint, request

from src.models import Book


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
@main_blueprint.route("/home")
def home():
    search = request.args.get("search")
    if search:
        books = Book.query.filter(Book.project_name == search)
    else:
        books = Book.query.all()
    return render_template("main/main.html", books=books)



