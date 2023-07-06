from flask import session, render_template, redirect, request, flash
from flask_app import app
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def index():

    return render_template('login.html')


@app.route('/crear/usuario', methods=['POST'])
def crear_uno():
    data = {
        **request.form
    }
    usuario_existe = Usuario.obtener_uno_con_mail(data)
    if Usuario.validar_registro(data, usuario_existe) == False:
        return redirect('/')
    else:
        password_encriptado = bcrypt.generate_password_hash(data['password'])
        data['password'] = password_encriptado
        id_usuario = Usuario.crear_uno(data)
        session['nombre'] = data['nombre']
        session['apellido'] = data['apellido']
        session['id_usuario'] = id_usuario

        return redirect('/recipes')


@app.route('/login', methods=['POST'])
def procesa_login():

    data = {
        'email': request.form['email_login']
    }

    usuario = Usuario.obtener_uno_con_mail(data)

    if usuario == None:
        flash("Email invalido", "error_email_login")
        return redirect('/')
    else:
        if not bcrypt.check_password_hash(usuario.password, request.form['password_login']):
            flash('Credenciales incorrectas.', "error_password_login")
            return redirect('/')
        else:
            session['nombre'] = usuario.nombre
            session['apellido'] = usuario.apellido
            session['id_usuario'] = usuario.id
            return redirect('/recipes')


@app.route('/logout', methods=['POST'])
def procesa_logout():
    session.clear()
    return redirect('/')
