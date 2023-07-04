from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo


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
    informacion_dojo = Dojo.select(data)
    print(informacion_dojo)
    return render_template("home.html", informacion_dojo=informacion_dojo)
