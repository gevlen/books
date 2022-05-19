from datetime import date
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), unique=True, nullable=False, index=True)
    created_at = db.Column(db.Date, default=date.today)
    updated_at = db.Column(db.Date, default=None, onupdate=date.today())
    author_id = db.Column(db.Integer, db.ForeignKey("author.id", ondelete='SET NULL'), nullable=True)

    def __repr__(self):
        return f'{self.title}'


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False, index=True)
    books = db.relationship("Book", backref=db.backref("author", lazy="joined"))

    def __repr__(self):
        return f'{self.name}'
