from flask_mail import Message
from flask import render_template

from src.extentions import mail
from src.config import Config


def send_email(user):
    token = user.create_key()
    html = render_template("auth/_activation_message.html", token=token)
    message = Message(
        "Password Reset Request", recipients=[user.email], sender=Config.MAIL_NAME, html=html
    )

    mail.send(message)
