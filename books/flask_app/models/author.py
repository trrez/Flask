from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book
from flask_app.models import favorite


class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.author_favorites = []

    @classmethod
    def new(cls, data):
        query = """
            INSERT INTO authors(name)
            VALUES(%(name)s);
        """
        result = connectToMySQL("mydb").query_db(query, data)
        return result

    @classmethod
    def all(cls):
        query = """
                SELECT * FROM authors; 
        """
        result = connectToMySQL('mydb').query_db(query)
        authors = []
        for author in result:
            authors.append(Author(author))
        return authors

    @classmethod
    def select_author_with_favorite(cls, data):
        query = """
            SELECT *
            FROM authors
            LEFT JOIN favorites ON authors.id = favorites.author_id
            LEFT JOIN books ON books.id = favorites.book_id
            WHERE authors.id = %(id)s;
        """
        results = connectToMySQL('mydb').query_db(query, data)
        favorites = cls(results[0])
        for row_from_db in results:
            favorite_data = {
                "id": row_from_db["books.id"],
                "name": row_from_db["name"],
                "title": row_from_db["title"],
                "num_of_pages": row_from_db["num_of_pages"],
                "created_at": row_from_db["created_at"],
                "updated_at": row_from_db["updated_at"]
            }
            favorites.author_favorites.append(book.Book(favorite_data))

        return favorites
