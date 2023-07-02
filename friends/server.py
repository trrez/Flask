from flask import Flask, render_template, request, redirect
# importar la clase de friend.py
from friend import Friend
app = Flask(__name__)


@app.route("/")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", friends=friends)


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/add", methods=["POST"])
def add():
    data = {
        "name": request.form["name"],
        "last_name": request.form["last_name"],
        "occupation": request.form["occupation"]
    }
    Friend.add(data)
    return redirect("/")


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    data = {
        "id": id
    }
    Friend.delete(data)
    return redirect("/")


@app.route("/select/<int:id>", methods=["GET"])
def select(id):
    data = {
        "id": id
    }
    friend_actual = Friend.select(data)
    return render_template("/edit.html", friend_actual=friend_actual)


@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    data = {
        "id": id,
        "name": request.form["name"],
        "last_name": request.form["last_name"],
        "occupation": request.form["occupation"]
    }
    Friend.update(data)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
