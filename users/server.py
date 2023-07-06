from flask_app import app
from flask_app.controllers import users
app.secret_key = 'keep it secret, keep it safe'

if __name__ == "__main__":
    app.run(debug=True, port=5001)
