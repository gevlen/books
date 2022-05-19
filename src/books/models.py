from flask_marshmallow import Marshmallow

from src.database.tables import Book, Author


ma = Marshmallow()


class AuthorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Author
        include_relationships = True
        load_instance = True

    id = ma.auto_field(dump_only=True)
    name = ma.auto_field(dump_only=True)


class BookSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Book
        include_relationships = True
        load_instance = True

    id = ma.auto_field(dump_only=True)
    title = ma.auto_field(required=False)
    created_at = ma.auto_field(dump_only=True)
    updated_at = ma.auto_field(dump_only=True)
    author_id = ma.auto_field(load_only=True, required=False)
    author = ma.Nested(AuthorSchema, dump_only=True)








