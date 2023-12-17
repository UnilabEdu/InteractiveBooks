from flask import render_template, Blueprint


about_blueprint = Blueprint("about", __name__)


@about_blueprint.route("/about_page")
def about():
    return render_template("about/about.html")