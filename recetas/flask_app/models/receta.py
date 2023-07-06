from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.usuario import Usuario
from flask_app import BASE_DATOS
from flask import flash


class Receta:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.descripcion = data['descripcion']
        self.instrucciones = data['instrucciones']
        self.fecha_elaboracion = data['fecha_elaboracion']
        self.menos_treinta = data['menos_treinta']
        self.fecha_actualizacion = data['fecha_actualizacion']
        self.fecha_creacion = data['fecha_creacion']
        self.id_usuario = data['id_usuario']

    @classmethod
    def crear_uno(cls, data):
        query = """
            INSERT INTO recetas(nombre, descripcion, instrucciones, fecha_elaboracion, menos_treinta,  id_usuario)
            VALUES (%(nombre)s, %(descripcion)s, %(instrucciones)s, %(fecha_elaboracion)s, %(menos_treinta)s,%(id_usuario)s)
        """

        resultado = connectToMySQL(BASE_DATOS).query_db(query, data)
        return resultado

    @classmethod
    def obtener_todas_con_usuario(cls):
        query = """
            SELECT * FROM recetas r
            JOIN usuarios u
            ON r.id_usuario = u.id;
        """

        resultado = connectToMySQL(BASE_DATOS).query_db(query)
        lista_recetas = []
        for item in resultado:
            receta = Receta(item)
            data_usuario = {
                "id": item['u.id'],
                "nombre": item['u.nombre'],
                "apellido": item['apellido'],
                "email": item['email'],
                "password": item['password'],
                "fecha_creacion": item['u.fecha_creacion'],
                "fecha_actualizacion": item['u.fecha_actualizacion']
            }
            usuario = Usuario(data_usuario)
            receta.usuario = usuario
            lista_recetas.append(receta)

        return lista_recetas

    @classmethod
    def eliminar_uno(cls, data):
        query = """
            DELETE FROM recetas
            WHERE id = %(id)s;
        """
        return connectToMySQL(BASE_DATOS).query_db(query, data)

    @classmethod
    def obtener_uno_con_usuario(cls, data):
        query = """
            SELECT * FROM recetas r
            JOIN usuarios u
            ON r.id_usuario = u.id
            WHERE r.id = %(id)s;
        """

        resultado = connectToMySQL(BASE_DATOS).query_db(query, data)
        item = resultado[0]
        receta = Receta(item)
        data_usuario = {
            "id": item['u.id'],
            "nombre": item['u.nombre'],
            "apellido": item['apellido'],
            "email": item['email'],
            "password": item['password'],
            "fecha_creacion": item['u.fecha_creacion'],
            "fecha_actualizacion": item['u.fecha_actualizacion']
        }
        receta.usuario = Usuario(data_usuario)
        return receta

    @classmethod
    def obtener_uno(cls, data):
        query = """
            SELECT * FROM 
            recetas WHERE id = %(id)s;
        """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, data)
        receta = Receta(resultado[0])
        return receta

    @classmethod
    def editar_uno(cls, data):
        query = """
            UPDATE recetas
            SET nombre = %(nombre)s, descripcion = %(descripcion)s, instrucciones= %(instrucciones)s, fecha_elaboracion = %(fecha_elaboracion)s, menos_treinta = %(menos_treinta)s
            WHERE id = %(id)s;
        """
        return connectToMySQL(BASE_DATOS).query_db(query, data)

    @staticmethod
    def validar_formulario_recetas(data):
        es_valido = True
        if len(data['nombre']) < 3:
            es_valido = False
            flash("Debes de proporcionar el nombre de la receta.", "error_nombre")
        if len(data['descripcion']) < 3:
            es_valido = False
            flash("Debes de proporcionar una descripcion de la receta.",
                  "error_descripcion")
        if len(data['instrucciones']) < 3:
            es_valido = False
            flash("Debes de proporcionar las instrucciones de la receta.",
                  "error_instrucciones")
        if data['fecha_elaboracion'] == '':
            es_valido = False
            flash("Debes de proporcionar la fecha de elaboracion de la receta.",
                  "error_fecha_elaboracion")
        if "menos_treinta" not in data:
            es_valido = False
            flash("Debes de proporcionar si la receta se elabora en menos de 30 minutos.",
                  "error_menos_treinta")
        return es_valido
