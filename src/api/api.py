import os

from flask import Flask
from flask_restful import Api

from src.database import initialize_db, initialize_migrations
from src.api.books import initialize_book_api
from src.books.models import ma
from src.api.authors import initialize_author_api

app = Flask(__name__)
api = Api(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
                                        'sqlite:///' + os.path.join(basedir, '../database/books.db')

ma.init_app(app)

initialize_db(app)
initialize_migrations(app)
initialize_book_api(api)
initialize_author_api(api)

app.run()
