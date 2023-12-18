from flask import render_template, Blueprint

from src.models import Book


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
@main_blueprint.route("/home")
def home():
    books = Book.query.all()
    return render_template("main/main.html", books=books)



