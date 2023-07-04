from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

from flask_app import app


@app.route('/add-ninja')
def new_ninja():
    list_dojos = Dojo.get_all()
    return render_template('new_ninja.html', list_dojos=list_dojos)


@app.route('/new-ninja', methods=["POST"])
def ninja():
    Ninja.create(request.form)
    return redirect('/')
