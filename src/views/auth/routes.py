from flask import render_template, Blueprint, redirect, url_for, request
from flask_login import login_user, logout_user

from src.views.auth.forms import LoginForm
from src.models import User


auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    error_message = None
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()

        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next", None)
            if next:
                return redirect(next)
            elif user.is_admin:
                return redirect(url_for("admin.index"))
            else:
                return redirect(url_for("main.home"))
        else:
            error_message = "Invalid username or password. Please try again."

    return render_template(
        "auth/login.html",
        form=form,
        error_message=error_message,
    )



@auth_blueprint.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


