from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.user import User


@app.route("/")
def index():
    user = User.get_all()
    return render_template("index.html", user=user)


@app.route("/user/new")
def new():
    return render_template("form.html")


@app.route("/add", methods=["POST"])
def add():

    data = {
        "name": request.form["name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.add(data)
    return redirect("/")


@app.route("/select/<int:id>", methods=["GET"])
def select(id):
    data = {
        "id": id
    }
    actual_user = User.select(data)
    return render_template("actual_form.html", actual_user=actual_user)


@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    data = {
        "id": id,
        "name": request.form["name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.update(data)
    return redirect("/")


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect("/")


@app.route("/show/<int:id>", methods=["GET"])
def show(id):
    data = {
        "id": id
    }
    actual_user = User.select(data)
    return render_template("show.html", actual_user=actual_user)
