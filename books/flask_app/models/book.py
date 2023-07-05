from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author


class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.book_favorite = []

    @classmethod
    def new_book(cls, data):
        query = """
            INSERT INTO books(title, num_of_pages)
            VALUES(%(title)s,%(num_of_pages)s);
        """
        result = connectToMySQL("mydb").query_db(query, data)
        return result

    @classmethod
    def all_book(cls):
        query = """
                SELECT * FROM books; 
        """
        result = connectToMySQL('mydb').query_db(query)
        books = []
        for book in result:
            books.append(Book(book))
        return books

    @classmethod
    def select_book_with_author_favorite(cls, data):
        query = """
            SELECT *
            FROM books
            LEFT JOIN favorites ON books.id = favorites.book_id
            LEFT JOIN authors ON authors.id = favorites.author_id
            WHERE books.id = %(id)s;
        """
        results = connectToMySQL('mydb').query_db(query, data)
        favorites = cls(results[0])
        for row_from_db in results:
            favorite_data = {
                "id": row_from_db["authors.id"],
                "title": row_from_db["title"],
                "num_of_pages": row_from_db["num_of_pages"],
                "created_at": row_from_db["authors.created_at"],
                "updated_at": row_from_db["authors.updated_at"]
            }
            favorites.book_favorite.append(author.Author(favorite_data))
            print(favorites.id)
            print(favorites.book_favorite)

        return favorites
