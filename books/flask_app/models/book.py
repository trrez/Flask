from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author


class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors_who_favorited = []

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
    def get_by_id(cls, data):
        query = """
            SELECT *
            FROM books
            LEFT JOIN favorites ON books.id = favorites.book_id
            LEFT JOIN authors ON authors.id = favorites.author_id
            WHERE books.id = %(id)s;
        """
        results = connectToMySQL('mydb').query_db(query, data)
        book = cls(results[0])
        for row in results:
            if row['authors.id'] == None:
                break
            data = {
                "id": row["authors.id"],
                "name": row["name"],
                "created_at": row["authors.created_at"],
                "updated_at": row["authors.updated_at"]
            }
            book.authors_who_favorited.append(author.Author(data))

        return book

    @classmethod
    def unfavorited_books(cls, data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );"
        results = connectToMySQL('mydb').query_db(query, data)
        books = []
        for row in results:
            books.append(cls(row))
        print(books)
        return books
