from flask import render_template, Blueprint, request

from src.models import Book


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
@main_blueprint.route("/home")
def home():

    page = request.args.get('page', 1, type=int)
    per_page = 6  # Number of products per page
    pagination = Book.query.paginate(page=page, per_page=per_page, error_out=False)
    products_on_page = pagination.items
    total_pages = pagination.pages

    return render_template('main/main.html', books=pagination, total_pages=total_pages, products_on_page=products_on_page, page=page)



