from os import path
import os




class Config:
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    UPLOAD_PATH = path.join(BASE_DIRECTORY, "static", "img")
    SECRET_KEY = "abjdlhrjekls78akkjlllakqawss"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "database.db")
    FLASK_ADMIN_SWATCH = "pulse"
    
    # Flask_Mail
    MAIL_SERVER = 'sandbox.smtp.mailtrap.io'
    MAIL_NAME = 'test24@gmail.com'
    MAIL_USERNAME = 'cc020a0104ebaa'
    MAIL_PASSWORD = '465458f5f47b2f'
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    





