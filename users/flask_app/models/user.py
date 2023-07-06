from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.passw = data['passw']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM users;
        """

        result = connectToMySQL("mydb").query_db(query)
        users = []
        for user in result:
            users.append(User(user))
        print(users)
        return users

    @classmethod
    def add(cls, data):
        query = """
            INSERT INTO users(first_name, last_name, email, passw, created_at, updated_at)
            VALUES(%(name)s, %(last_name)s, %(email)s, %(passw)s, NOW(), NOW());
        """

        return connectToMySQL("mydb").query_db(query, data)

    @classmethod
    def select(cls, data):
        query = """
            SELECT * FROM users
            WHERE id=%(id)s;
        """
        result = connectToMySQL("mydb").query_db(query, data)
        actual_user = User(result[0])
        return actual_user

    @classmethod
    def update(cls, data):
        query = """
            UPDATE users
            SET first_name = %(name)s, last_name = %(last_name)s, email = %(email)s, pass = %(pass)s
            WHERE ID = %(id)s;
        """
        return connectToMySQL("mydb").query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = """
            DELETE FROM users
            WHERE ID = %(id)s;
        """
        return connectToMySQL("mydb").query_db(query, data)

    @staticmethod
    def validate_user(data):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('Ingrese un email valido', 'error_mail')
        return is_valid
