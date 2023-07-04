from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app import app


from flask_app import app


@app.route("/", methods=['GET'])
def index():
    dojos = Dojo.get_all()
    return render_template("index.html", dojos=dojos)


@app.route("/new", methods=["POST"])
def create():
    new_dojo = {
        "nombre": request.form["nombre"]
    }
    Dojo.create(new_dojo)
    return redirect('/')


@app.route("/home/<int:id>", methods=["GET"])
def home(id):
    data = {
        "id": id
    }
    dojo = Dojo.select(data)
    return render_template('home.html', dojo=dojo)
