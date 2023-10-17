from flask import Flask, request
from db import db
from flask_migrate import Migrate
from controllers.categoria_controller import CategoriaController
from controllers.publicacion_controller import PublicacionController

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/documentacion_backend'

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'REST API funcionando! 😎'

@app.route('/publicacion/listar')
def listar_publicaciones():
    controller = PublicacionController()
    return controller.getAll()

@app.route('/publicacion/crear', methods=['POST'])
def crear_publicacion():
    json = request.get_json()
    controller = PublicacionController()
    return controller.create(json)

@app.route('/categoria/crear', methods=['POST'])
def crear_categoria():
    json = request.get_json()
    controller = CategoriaController()
    return controller.create(json)

@app.route('/categoria/listar')
def listar_categorias():
    controller = CategoriaController()
    return controller.getAll()

# if __name__ == '__main__':
#     app.run(debug=True)