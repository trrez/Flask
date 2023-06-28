from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def counter():
    session['secret_key'] = 'keep it secret, keep it safe'
    if 'contador' in session:
        session['contador'] += 1
    else:
        session['contador'] = 0

    return render_template('index.html', contador=session['contador'])


@app.route('/increment', methods=['POST'])
def increment():
    if 'contador' in session:
        session['contador'] += 2
    else:
        session['contador'] = 0
    return redirect('/')


@app.route('/destroy_session', methods=['POST'])
def destroy():
    session.clear()  # borra todas las claves en la sesión
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
