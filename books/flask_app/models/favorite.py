from flask_app.config.mysqlconnection import connectToMySQL


class Favorite:
    def __init__(self, data):
        self.author_id = data['author_id']
        self.book_id = data['book_id']

    @classmethod
    def new_favorite(cls, data):
        query = """
            INSERT INTO favorite(author_id, book_id)
            VALUES(%(author_id)s, %(book_id)s);
        """
        result = connectToMySQL("mydb").query_db(query, data)
        return result
