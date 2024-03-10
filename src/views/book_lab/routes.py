from flask import render_template, Blueprint, request

from src.models import Book


books_blueprint = Blueprint("books", __name__)


@books_blueprint.route("/book_laboratory")
def book_lab():
    
    page = request.args.get('page', 1, type=int)
    per_page = 1  # Number of products per page
    pagination = Book.query.paginate(page=page, per_page=per_page, error_out=False)
    products_on_page = pagination.items
    total_pages = pagination.pages

    return render_template('book_lab/book_list.html', books=pagination, total_pages=total_pages, products_on_page=products_on_page, page=page)
