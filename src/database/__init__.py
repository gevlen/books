from .tables import db, migrate


def initialize_db(app):
    db.init_app(app)

def initialize_migrations(app):
    migrate.init_app(app, db)
