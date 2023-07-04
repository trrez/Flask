from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja


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
            FROM dojos d LEFT JOIN ninjas n
            ON d.id = n.dojos_id
            WHERE d.id = %(id)s;
        """
        result = connectToMySQL("mydb").query_db(query, data)
        informacion_dojo = Dojo(result[0])

        for reglon in result:
            if reglon['n.nombre'] != None:
                data_ninja = {
                    'nombre': reglon['n.nombre'],
                    'apellido': reglon['apellido'],
                    'edad': reglon['edad'],
                    'id': reglon['n.id'],
                    'dojos_id': reglon['dojos_id'],
                    'created_at': reglon['n.created_at'],
                    'updated_at': reglon['n.updated_at']
                }
                ninja_actual = Ninja(data_ninja)
                informacion_dojo.ninjas.append(ninja_actual)
        return informacion_dojo
