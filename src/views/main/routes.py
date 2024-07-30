from flask import render_template, Blueprint, request, redirect, url_for,flash
from flask_login import login_user, logout_user

from src.utils import send_email
from src.views.main.forms import LoginForm, ResetRequestForm, ResetPasswordForm
from src.models import Book
from src.models import User

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
@main_blueprint.route("/home")
def home():
    search = request.args.get("search")

    if search:
        books = Book.query.filter(Book.project_name.ilike(f"%{search}%")).paginate(per_page=12, error_out=True)
    else:
        books = Book.query.paginate(per_page=12, error_out=True)

    return render_template("main/main.html", books=books, search=search)


@main_blueprint.route("/login", methods=["GET", "POST"])
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


@main_blueprint.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for("main.login"))


@main_blueprint.route("/reset_password", methods=["GET", "POST"])
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



@main_blueprint.route("/reset_password/<string:token>", methods=["GET", "POST"])
def reset_token(token):
    user = User.verify_key(token)

    if user is None:
        flash("That is invalid token or expired. Please try again!", "warning")
        return redirect(url_for("main.reset_request"))
    
    form = ResetPasswordForm()

    if form.validate_on_submit():
        new_password = form.password.data
        
        if new_password:
            user.password = new_password
            user.save()
            logout_user()
        
        return redirect(url_for("main.login"))
    
    return render_template("auth/change_password.html", form=form)
