from flask.cli import with_appcontext
import click

from src.extentions import db
from src.models import Book, User, Role


@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Database creation in progress")
    db.drop_all()
    db.create_all()
    click.echo("Database created!")


@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("Creating books")
    book_1 = Book(title="Book_1", author="Anano")
    book_2 = Book(title="Book_2", author="Nino")

    book_1.create()
    book_2.create()
    click.echo("Created books")

    click.echo("Creating roles")
    userrole = Role(name='User')
    adminrole = Role(name='Admin')
    userrole.create()
    adminrole.create()

    click.echo("Creating test users")
    user1 = User(username="Anano", password="Anano1234", role_id=userrole.id)
    user2 = User(username="adminuser", password="Admin1234", role_id=adminrole.id)
    user1.create()
    user2.create()

    click.echo("Database populated!")
