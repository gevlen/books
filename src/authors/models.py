from flask_marshmallow import Marshmallow

from src.database.tables import Book, Author

ma = Marshmallow()


class BooksSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Book
        include_relationships = True
        load_instance = True

    id = ma.auto_field(dump_only=True)
    title = ma.auto_field(dump_only=True)


class AuthorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Author
        include_relationships = True
        load_instance = True

    id = ma.auto_field(dump_only=True)
    name = ma.auto_field(required=True)
    books = ma.Nested(BooksSchema, dump_only=True, many=True)
