from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'esto es secreto'


@app.route('/')
def form():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return render_template('result.html')


@app.route('/home', methods=['GET'])
def home():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
