from src.database.tables import Book, db

from src.books.models import BookSchema


class BookService:
    def get_all_books(self):
        schema = BookSchema(many=True)
        books = Book.query.all()
        return schema.dump(books)

    def add_new_book(self, book_data):
        schema = BookSchema()
        data = book_data.get_json()
        book = schema.load(data)
        db.session.add(book)
        db.session.commit()
        return schema.dump(Book.query.filter_by(title=book.title).first()), 201

    def get_book_by_id(self, id):
        schema = BookSchema()
        books = Book.query.get_or_404(id)
        return schema.dump(books)

    def update_book(self, id, book_data):
        schema = BookSchema()
        data = book_data.get_json()
        book = schema.load(data, instance=Book().query.get_or_404(id))
        db.session.commit()
        return schema.dump(book)

    def delete_book_by_id(self, id):
        schema = BookSchema()
        book = Book.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        return schema.dump(book)
