from flask import render_template, Blueprint, redirect, url_for, request, flash
from flask_login import login_user, logout_user

from src.views.auth.forms import LoginForm, ResetRequestForm, ResetPasswordForm
from src.models import User
from src.utils import send_email


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
            error_message = "Incorrect username or password! Please try again."

    return render_template(
        "auth/login.html",
        form=form,
        error_message=error_message,
    )


@auth_blueprint.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for("auth.login"))



@auth_blueprint.route("/reset_password", methods=["GET", "POST"])
def reset_request():
    form = ResetRequestForm()
    error_message = None
    success_message = None

    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()

        if user:
            send_email(user)
            success_message = "Email sent! Please check your inbox."
        else:
            error_message = "User doesn't exists! Please try again."

    return render_template("auth/send_email.html", form=form, success_message=success_message, error_message=error_message,)



@auth_blueprint.route("/reset_password/<string:token>", methods=["GET", "POST"])
def reset_token(token):
    user = User.verify_key(token)

    if user is None:
        flash("That is invalid token or expired. Please try again!", "warning")
        return redirect(url_for("auth.reset_request"))
    
    form = ResetPasswordForm()

    if form.validate_on_submit():
        new_password = form.password.data
        
        if new_password:
            user.password = new_password
            user.save()
            logout_user()
        
        return redirect(url_for("auth.login"))
    
    return render_template("auth/change_password.html", form=form)
