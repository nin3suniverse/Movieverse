from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from flask_login import UserMixin
from datetime import datetime

watchlist_table= db.Table('watchlist',
        db.Column('user_id',db.Integer,db.ForeignKey('user.id'), primary_key=True),
        db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True)
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    role= db.Column(db.String(20), default="user")
    watchlist = db.relationship(
        'Movie',
        secondary=watchlist_table,
        backref=db.backref('watchlisted_by', lazy='dynamic'),
        lazy='dynamic'
    )
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    genre = db.Column(db.String(50))
    poster = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    description= db.Column(db.Text, nullable= False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_admin =db.Column(db.Boolean, default=False)
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    user = db.Relationship('User', backref="reviews", lazy=True)
    movie=db.Relationship('Movie', backref="reviews", lazy=True)
