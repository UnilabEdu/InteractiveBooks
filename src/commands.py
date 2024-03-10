from flask.cli import with_appcontext
import click

from src.extentions import db
from src.models import Role, User


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
    
    click.echo("Creating role")
    adminrole = Role(name="Admin")
    adminrole.create()

    click.echo("Creating test admin")
    user = User(
        username="adminuser",
        password="Admin1234",
        email="ananorobakidze24@gmail.com",
        role_id=adminrole.id,
    )
    user.create()

    click.echo("Database populated!")
