from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired


class AddBookForm(FlaskForm):
    title = StringField("წიგნის სახელი", validators=[DataRequired()])
    author = StringField("წიგნის ავტორი", validators=[DataRequired()])
    submit = SubmitField("დამატება", validators=[DataRequired()])
