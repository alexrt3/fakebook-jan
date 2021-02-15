from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
import shortuuid


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, default=shortuuid.ShortUUID(alphabet='1234567890').random(length=6), unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    posts = db.relationship('Post', cascade='all, delete-orphan', backref='post', lazy=True)

    def __init__(self, first_name, last_name, password):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = f'{self.first_name}{self.last_name[0]}@codingtemple.com'.lower()

    def create_password_hash(self, password):
        self.password = generate_password_hash(password)

    def verify_password_hash(self, password):
        return check_password_hash(password)

    def save(self):
        self.create_password_hash(self.password)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<User: {self.email}>'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)