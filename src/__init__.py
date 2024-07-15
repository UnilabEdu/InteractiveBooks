from flask import Flask

from src.config import Config
from src.extentions import db, migrate, login_manager, mail
from src.views import (
    main_blueprint,
    book_blueprint,
    books_blueprint,
    auth_blueprint,
)
from src.commands import init_db, populate_db
from src.models import Book, User, Teacher, Mentor
from src.admin import admin, BookView, UserView, MentorView, TeacherView


BLUEPRINTS = [
    book_blueprint,
    main_blueprint,
    books_blueprint,
    auth_blueprint,
]


COMMANDS = [init_db, populate_db]


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(Config)
    app.config['SECURITY_PASSWORD_HASH'] = 'scrypt'

    register_extension(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extension(app):
    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)

    # Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Flask-Admin
    admin.init_app(app)
    admin.add_view(BookView(Book, db.session, endpoint="book_panel", name="Books"))
    admin.add_view(UserView(User, db.session))
    admin.add_view(TeacherView(Teacher, db.session, category="Teacher/Mentor"))
    admin.add_view(MentorView(Mentor, db.session, category="Teacher/Mentor"))

    # Flask-Mail
    mail.init_app(app)
    


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)
