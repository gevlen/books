from src.database.tables import Author, db

from src.service.authors.models import AuthorSchema


class AuthorService:
    def get_all_authors(self):
        schema = AuthorSchema(many=True)
        authors = Author.query.all()
        return schema.dump(authors)

    def add_author(self, author_data):
        schema = AuthorSchema()
        data = author_data.get_json()
        author = schema.load(data)
        db.session.add(author)
        db.session.commit()
        return schema.dump(Author.query.filter_by(name=author.name).first())

    def get_author_by_id(self, id):
        schema = AuthorSchema()
        author = Author.query.get_or_404(id)
        return schema.dump(author)

    def update_author(self, id, author_data):
        schema = AuthorSchema()
        data = author_data.get_json()
        author = schema.load(data, instance=Author().query.get_or_404(id))
        db.session.commit()
        return schema.dump(author)

    def delete_author_by_id(self, id):
        schema = AuthorSchema()
        author = Author.query.get_or_404(id)
        db.session.delete(author)
        db.session.commit()
        return schema.dump(author)
