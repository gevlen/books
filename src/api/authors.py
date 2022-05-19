from flask_restful import Resource, request

from src.authors.sercive import AuthorService


class AuthorsAPI(Resource):
    def get(self):
        author_service = AuthorService()
        return author_service.get_all_authors()

    def post(self):
        author_service = AuthorService()
        return author_service.add_author(request)


class AuthorAPI(Resource):
    def get(self, id):
        author_service = AuthorService()
        return author_service.get_author_by_id(id)

    def put(self, id):
        author_service = AuthorService()
        return author_service.update_author(id, request)

    def delete(self, id):
        author_service = AuthorService()
        return author_service.delete_author_by_id(id)


def initialize_author_api(api):
    api.add_resource(AuthorsAPI, '/api/authors')
    api.add_resource(AuthorAPI, '/api/authors/<int:id>')
