from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['nombre']
        self.last_name = data['apellido']
        self.age = data['edad']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojos_id = data['dojos_id']

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO ninjas(nombre, apellido, edad, dojos_id)
                VALUES(%(nombre)s,%(apellido)s,%(edad)s,%(dojo_id)s);
        """
        result = connectToMySQL("mydb").query_db(query, data)
        return result
