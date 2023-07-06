from flask_app import app
from flask_app.controllers import controlador_usuarios

if __name__ == '__main__':
    app.run(debug=True, port=5001)
