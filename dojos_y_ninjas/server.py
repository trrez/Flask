from flask_app.controllers import dojos, ninjas
from flask_app import app
app.secret_key = 'keep it secret, keep it safe'
if __name__ == '__main__':
    app.run(debug=True, port=5001)
