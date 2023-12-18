from flask.cli import with_appcontext
import click

from src.extentions import db
from src.models import Book, Teacher, Mentor


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
    click.echo("Creating mentors")
    mentor_1 = Mentor(fullname="ნიკა ტესტ")
    mentor_2 = Mentor(fullname="გიო ტესტ")
    mentor_1.create()
    mentor_2.create()

    click.echo("Creating teachers")
    teacher_1 = Teacher(fullname="მარი ტესტ")
    teacher_2 = Teacher(fullname="ნათია ტესტ")
    teacher_1.create()
    teacher_2.create()

    click.echo("Creating books")
    book_1 = Book(
        project_name="წიგნი_1",
        student_fullname="ანანო რობაქიძე",
        description="",
        school="სკოლა",
        student_class="მე-7",
        project_link="https://www.google.com/",
        img="fd4ae1b8-099c-401b-9e31-05cc09383078.webp",
        mentors=[mentor_1, mentor_2],
        teachers=[teacher_1]
    )
    book_2 = Book(
        project_name="წიგნი_2",
        student_fullname="ნინა ტესტ",
        description="",
        school="სკოლა",
        student_class="მე-9",
        project_link="https://www.google.com/",
        img="f059202d-3d1d-4db4-aa0a-4531473091c0.webp",
        mentors=[mentor_1, mentor_2],
        teachers=[teacher_2, teacher_1],
    )

    db.session.add_all([mentor_1, mentor_2, teacher_1, teacher_2, book_1, book_2])
    db.session.commit()

    book_1.create()
    book_2.create()

    click.echo("Created books")

    click.echo("Database populated!")
