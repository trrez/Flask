from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True, port=5001)
