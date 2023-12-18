from flask import Flask

from src.config import Config
from src.extentions import db, migrate 
from src.views import main_blueprint, book_blueprint, books_blueprint, about_blueprint
from src.commands import init_db, populate_db
from src.models import Book
from src.admin import admin, BookView


BLUEPRINTS = [book_blueprint, main_blueprint, books_blueprint, about_blueprint]


COMMANDS = [init_db, populate_db]


def create_app():
    app = Flask(__name__, template_folder="template")
    app.config.from_object(Config)

    register_extension(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extension(app):
    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)


    # Flask-Admin
    admin.init_app(app)
    admin.add_view(BookView(Book, db.session, endpoint="book_panel"))


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)
