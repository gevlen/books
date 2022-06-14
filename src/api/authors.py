from flask_restful import Resource, request

from src.service.authors.sercive import AuthorService


class AuthorsAPI(Resource):
    author_service = AuthorService()

    def get(self):
        return self.author_service.get_all_authors()

    def post(self):
        return self.author_service.add_author(request), 201


class AuthorAPI(Resource):
    author_service = AuthorService()

    def get(self, id):
        return self.author_service.get_author_by_id(id)

    def put(self, id):
        return self.author_service.update_author(id, request)

    def delete(self, id):
        return self.author_service.delete_author_by_id(id)


def initialize_author_api(api):
    api.add_resource(AuthorsAPI, '/api/authors')
    api.add_resource(AuthorAPI, '/api/authors/<int:id>')
