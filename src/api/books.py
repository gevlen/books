from flask_restful import Resource, request

from src.service.books.service import BookService


class BooksAPI(Resource):
    book_service = BookService()

    def get(self):
        return self.book_service.get_all_books()

    def post(self):
        return self.book_service.add_new_book(request), 201


class BookAPI(Resource):
    book_service = BookService()

    def get(self, id):
        return self.book_service.get_book_by_id(id)

    def put(self, id):
        return self.book_service.update_book(id, request)

    def delete(self, id):
        return self.book_service.delete_book_by_id(id)


def initialize_book_api(api):
    api.add_resource(BooksAPI, '/api/books')
    api.add_resource(BookAPI, '/api/books/<int:id>')
