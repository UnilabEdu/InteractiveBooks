from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer

from src.models.base import BaseModel
from src.extentions import db
from src.config import Config



class User(BaseModel, UserMixin):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    _password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    

    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    role = db.relationship("Role", uselist=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    
    def check_password(self, password):
        result = check_password_hash(self.password, password)
        return result
    
    def is_admin(self):
        return self.role and self.role.name == "Admin"
    

    def create_key(self):
        serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
        key = serializer.dumps({"user_id": self.id})
        return key
    
    @staticmethod
    def verify_key(key):
        serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
        try:
            user_id = serializer.loads(key, max_age=300)["user_id"]
        except:
            return None

        return User.query.get(user_id)


class Role(BaseModel):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return self.name
