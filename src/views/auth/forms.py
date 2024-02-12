from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, length, equal_to


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), length(min=8, max=64)])
    submit = SubmitField("Login")


class ResetRequestForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    submit = SubmitField('Send instructions')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Enter new password', validators=[DataRequired(), length(min=8, max=64)])
    confirm_password = PasswordField('Confirm new password', validators=[DataRequired(), equal_to("password", message="Your password and confirmation password do not match!")])
    submit = SubmitField("Reset Password")

