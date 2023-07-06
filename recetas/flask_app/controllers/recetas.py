from flask import session, render_template, redirect, request, flash
from flask_app import app
from flask_app.models.receta import Receta


@app.route('/recipes')
def recetas():
    if 'nombre' not in session:
        return redirect('/')
    lista_recetas = Receta.obtener_todas_con_usuario()
    return render_template('recipes.html', lista_recetas=lista_recetas)


@app.route('/formulario/receta')
def desplegar_formulario_recetas():
    return render_template('formulario_receta.html')


@app.route('/crear/receta', methods=['POST'])
def nueva_receta():
    data = {
        **request.form,
        "id_usuario": session['id_usuario']
    }
    if Receta.validar_formulario_recetas(data) == False:
        return redirect('/formulario/receta')
    else:
        id_receta = Receta.crear_uno(data)
        return redirect('/recipes')


@app.route('/eliminar/receta/<int:id>', methods=['POST'])
def eliminar_receta(id):
    data = {
        'id': id
    }
    Receta.eliminar_uno(data)
    return redirect('/recipes')


@app.route('/receta/<int:id>', methods=['GET'])
def desplegar_receta(id):
    data = {
        'id': id
    }
    receta = Receta.obtener_uno_con_usuario(data)
    return render_template('receta.html', receta=receta)


@app.route('/formulario/receta/editar/<int:id>', methods=['GET'])
def desplegar_editar_receta(id):
    data = {
        'id': id
    }
    receta = Receta.obtener_uno(data)
    return render_template('editar_receta.html', receta=receta)


@app.route('/editar/receta/<int:id>', methods=['POST'])
def editar_receta(id):
    if Receta.validar_formulario_recetas(request.form) == False:
        return redirect(f'/formulario/receta/editar({id})')
    else:
        data = {
            **request.form,
            'id': id
        }
        Receta.editar_uno(data)
        return redirect('/recipes')


@app.route('/logout/receta')
def procesa_logout_receta():
    session.clear()
    return redirect('/')
