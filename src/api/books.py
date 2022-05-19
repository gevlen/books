from flask_restful import Resource, request

from src.books.service import BookService


class BooksAPI(Resource):

    def get(self):
        book_service = BookService()
        return book_service.get_all_books()

    def post(self):
        book_service = BookService()
        return book_service.add_new_book(request)

class BookAPI(Resource):
    def get(self, id):
        book_service = BookService()
        return book_service.get_book_by_id(id)

    def put(self, id):
        book_service = BookService()
        return book_service.update_book(id, request)

    def delete(self, id):
        book_service = BookService()
        return book_service.delete_book_by_id(id)



def initialize_book_api(api):
    api.add_resource(BooksAPI, '/api/books')
    api.add_resource(BookAPI, '/api/books/<int:id>')