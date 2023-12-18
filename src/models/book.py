from src.extentions import db
from src.models.base import BaseModel


class BookMentor(BaseModel):
    __tablename__ = "mentors_book"

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
    mentor_id = db.Column(db.Integer, db.ForeignKey("mentors.id"))


class BookTeacher(BaseModel):
    __tablename__ = "teachers_book"

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"))


class Book(BaseModel):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String)
    student_fullname = db.Column(db.String)
    description = db.Column(db.String, nullable=True)
    school = db.Column(db.String)
    student_class = db.Column(db.String)
    project_link = db.Column(db.String)
    img = db.Column(db.String)

    mentors = db.relationship(
        "Mentor", secondary="mentors_book", back_populates="books"
    )
    teachers = db.relationship(
        "Teacher", secondary="teachers_book", back_populates="books"
    )

    def __repr__(self):
        return self.project_name


class Mentor(BaseModel):
    __tablename__ = "mentors"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String)

    books = db.relationship("Book", secondary="mentors_book", back_populates="mentors")

    def __repr__(self):
        return self.fullname


class Teacher(BaseModel):
    __tablename__ = "teachers"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String)

    books = db.relationship(
        "Book", secondary="teachers_book", back_populates="teachers"
    )

    def __repr__(self):
        return self.fullname
