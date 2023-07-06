from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
from flask import flash


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO dojos(nombre)
                VALUES(%(nombre)s);
        """
        result = connectToMySQL("mydb").query_db(query, data)
        return result

    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM dojos;
        """
        result = connectToMySQL('mydb').query_db(query)
        dojos = []
        for item in result:
            dojos.append(Dojo(item))
        return dojos

    @classmethod
    def select(cls, data):
        query = """
            SELECT *
            FROM dojos
            LEFT JOIN ninjas
            ON dojos.id = ninjas.dojos_id
            WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL('mydb').query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            ninja_data = {
                'id': row['ninjas.id'],
                'nombre': row['ninjas.nombre'],
                'apellido': row['apellido'],
                'edad': row['edad'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at'],
                'dojos_id': row['dojos_id']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))

            print(dojo.nombre)
            print(dojo.ninjas)
            print(dojo)
        return dojo

    @staticmethod
    def validated_dojo(data):
        is_valid = True
        if len(data['nombre']) < 3:
            flash("El nombre debe tener como minimo 3 caracteres.", "error_name")
            is_valid = False
        return is_valid
