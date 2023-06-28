from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def counter():
    session['secret_key'] = 'keep it secret, keep it safe'
    session['contador'] = 0

    if 'secret_key' in session:
        print('la llave existe!')
        session['contador'] += 1
    else:
        print("la llave 'key_name' NO existe")
        session['contador'] = 0

    if 'contador' in session:
        session['contador'] += 1
        print(session['contador'])
    else:
        session['contador'] = 0

    return render_template('index.html')


@app.route('/destroy_session')
def destroy():
    session['secret_key'] = 'keep it secret, keep it safe'
    session.clear()		# borra todas las claves
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
