from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/4')
def table4():
    return render_template('index2.html')


@app.route('/<int:x>/<int:y>')
def table(x, y):
    return render_template('index3.html', x=x, y=y)


@app.route('/<int:x>/<int:y>/<string:color>/<string:color2>')
def color(x, y, color, color2):
    return render_template('index4.html', x=x, y=y, color=color, color2=color2)


if __name__ == '__main__':
    app.run(debug=True)
