from app import db
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager

# Object Relational Mapper
# Flask-SQLAlchemy

# Java
# Hibernate

# A - Q$FG^ETJZ

# HASHING - Algorithm where a particular character has a specified translation i.e. other random characters to represent it
# SALTING - Example: Two users have same password; Saved encrypted password will be different for both

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
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

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.Text)
    date_created = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    date_updated = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post: ID: [{self.id}] {self.title}>'

