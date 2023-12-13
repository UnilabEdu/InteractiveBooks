from src.extentions import db
from src.models.base import BaseModel


class Book(BaseModel):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)

    def __repr__(self):
        return self.title
